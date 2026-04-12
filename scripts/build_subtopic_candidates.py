#!/usr/bin/env python3
"""Build subtopic candidates inside the strongest field hubs."""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple

from normalize_summaries import DERIVED_DIR, parse_simple_yaml, write_yaml


PAPER_INDEX_PATH = DERIVED_DIR / "paper_index.yaml"
CITATION_EDGES_PATH = DERIVED_DIR / "citation_edges.yaml"
TOPIC_CANDIDATES_PATH = DERIVED_DIR / "topic_candidates.yaml"
SUBTOPIC_CANDIDATES_PATH = DERIVED_DIR / "subtopic_candidates.yaml"

GENERIC_KEYWORDS = {
    "learning",
    "cortex",
    "hippocampal",
    "hippocampus",
    "prefrontal",
    "prefrontal_cortex",
    "spatial",
    "navigation",
    "spatial_navigation",
    "reinforcement_learning",
    "cognitive_map",
}

SIMILARITY_WEIGHTS = {
    "direct_citation": 3.0,
    "shared_neighbor": 0.75,
    "framework": 2.0,
    "task": 1.5,
    "keyword": 1.0,
    "brain_region": 0.75,
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-parent-topics",
        type=int,
        default=5,
        help="How many primary field hubs to subdivide.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write derived/subtopic_candidates.yaml.",
    )
    return parser.parse_args()


def load_payloads() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    paper_index = parse_simple_yaml(PAPER_INDEX_PATH.read_text())
    citation_edges = parse_simple_yaml(CITATION_EDGES_PATH.read_text())
    topic_candidates = parse_simple_yaml(TOPIC_CANDIDATES_PATH.read_text())
    return paper_index, citation_edges, topic_candidates


def choose_parent_topics(topic_candidates: Dict[str, Any], max_parent_topics: int) -> List[Dict[str, Any]]:
    primary = [topic for topic in topic_candidates["topics"] if topic.get("tier") == "primary"]
    primary.sort(key=lambda topic: (-topic["source_signals"]["support_count"], topic["topic_id"]))
    return primary[:max_parent_topics]


def build_adjacency(edges: List[Dict[str, Any]]) -> Dict[str, Set[str]]:
    adjacency: Dict[str, Set[str]] = defaultdict(set)
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        adjacency[source].add(target)
        adjacency[target].add(source)
    return adjacency


def filtered_keywords(paper: Dict[str, Any]) -> Set[str]:
    return {term for term in (paper.get("keywords", []) or []) if term not in GENERIC_KEYWORDS}


def pair_similarity(
    a: str,
    b: str,
    papers: Dict[str, Dict[str, Any]],
    adjacency: Dict[str, Set[str]],
) -> float:
    paper_a = papers[a]
    paper_b = papers[b]
    neighbors_a = adjacency.get(a, set())
    neighbors_b = adjacency.get(b, set())

    score = 0.0
    if b in neighbors_a:
        score += SIMILARITY_WEIGHTS["direct_citation"]
    shared_neighbors = len(neighbors_a & neighbors_b)
    score += min(shared_neighbors, 4) * SIMILARITY_WEIGHTS["shared_neighbor"]
    score += len(set(paper_a.get("frameworks", []) or []) & set(paper_b.get("frameworks", []) or [])) * SIMILARITY_WEIGHTS["framework"]
    score += len(set(paper_a.get("tasks", []) or []) & set(paper_b.get("tasks", []) or [])) * SIMILARITY_WEIGHTS["task"]
    score += len(filtered_keywords(paper_a) & filtered_keywords(paper_b)) * SIMILARITY_WEIGHTS["keyword"]
    score += len(set(paper_a.get("brain_regions", []) or []) & set(paper_b.get("brain_regions", []) or [])) * SIMILARITY_WEIGHTS["brain_region"]
    return score


def pair_weight(pair_weights: Dict[Tuple[str, str], float], a: str, b: str) -> float:
    if a == b:
        return 0.0
    return pair_weights.get(tuple(sorted((a, b))), 0.0)


def desired_cluster_count(node_count: int) -> int:
    if node_count >= 90:
        return 6
    if node_count >= 70:
        return 5
    if node_count >= 55:
        return 4
    return 3


def compute_parent_centrality(
    nodes: List[str],
    pair_weights: Dict[Tuple[str, str], float],
    adjacency: Dict[str, Set[str]],
) -> Counter:
    node_set = set(nodes)
    centrality = Counter()
    for node in nodes:
        centrality[node] += 2 * len(adjacency.get(node, set()) & node_set)
    for (a, b), weight in pair_weights.items():
        if a in node_set and b in node_set:
            centrality[a] += weight
            centrality[b] += weight
    return centrality


def choose_seed_papers(
    nodes: List[str],
    pair_weights: Dict[Tuple[str, str], float],
    centrality: Counter,
    cluster_count: int,
) -> List[str]:
    ranked = sorted(nodes, key=lambda pid: (centrality[pid], pid), reverse=True)
    seeds = [ranked[0]]
    while len(seeds) < min(cluster_count, len(nodes)):
        best_pid = None
        best_score = None
        for pid in ranked:
            if pid in seeds:
                continue
            max_similarity = max(pair_weight(pair_weights, pid, seed) for seed in seeds)
            score = centrality[pid] - 1.5 * max_similarity
            if best_score is None or score > best_score:
                best_score = score
                best_pid = pid
        if best_pid is None:
            break
        seeds.append(best_pid)
    return seeds


def assign_to_medoids(
    nodes: List[str],
    medoids: List[str],
    pair_weights: Dict[Tuple[str, str], float],
    centrality: Counter,
) -> Dict[str, List[str]]:
    clusters: Dict[str, List[str]] = {medoid: [medoid] for medoid in medoids}
    for node in nodes:
        if node in medoids:
            continue
        best_medoid = max(
            medoids,
            key=lambda medoid: (pair_weight(pair_weights, node, medoid), centrality[medoid], medoid),
        )
        clusters[best_medoid].append(node)
    for members in clusters.values():
        members.sort()
    return clusters


def choose_medoid(cluster: List[str], pair_weights: Dict[Tuple[str, str], float], centrality: Counter) -> str:
    return max(
        cluster,
        key=lambda pid: (
            sum(pair_weight(pair_weights, pid, other) for other in cluster if other != pid),
            centrality[pid],
            pid,
        ),
    )


def cluster_by_seeds(
    nodes: List[str],
    pair_weights: Dict[Tuple[str, str], float],
    adjacency: Dict[str, Set[str]],
) -> Tuple[List[List[str]], List[str], int]:
    cluster_count = desired_cluster_count(len(nodes))
    centrality = compute_parent_centrality(nodes, pair_weights, adjacency)
    medoids = choose_seed_papers(nodes, pair_weights, centrality, cluster_count)

    for _ in range(3):
        clusters = assign_to_medoids(nodes, medoids, pair_weights, centrality)
        medoids = [choose_medoid(cluster, pair_weights, centrality) for cluster in clusters.values()]

    clusters = assign_to_medoids(nodes, medoids, pair_weights, centrality)
    large_clusters = [sorted(cluster) for cluster in clusters.values() if len(cluster) >= 3]
    small_clusters = [cluster for cluster in clusters.values() if len(cluster) < 3]
    orphans: List[str] = []

    for cluster in small_clusters:
        for node in cluster:
            if not large_clusters:
                orphans.append(node)
                continue
            best_cluster = max(
                large_clusters,
                key=lambda members: sum(pair_weight(pair_weights, node, member) for member in members) / len(members),
            )
            best_score = sum(pair_weight(pair_weights, node, member) for member in best_cluster) / len(best_cluster)
            if best_score >= 1.5:
                best_cluster.append(node)
                best_cluster.sort()
            else:
                orphans.append(node)

    large_clusters = [sorted(cluster) for cluster in large_clusters if len(cluster) >= 3]
    large_clusters.sort(key=len, reverse=True)
    return large_clusters, sorted(orphans), cluster_count


def internal_edge_count(cluster_set: Set[str], edges: List[Dict[str, Any]]) -> int:
    return sum(1 for edge in edges if edge["source"] in cluster_set and edge["target"] in cluster_set)


def cluster_top_terms(cluster: List[str], papers: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    counters = {
        "frameworks": Counter(),
        "brain_regions": Counter(),
        "tasks": Counter(),
        "keywords": Counter(),
    }
    for pid in cluster:
        paper = papers[pid]
        for category, counter in counters.items():
            terms = paper.get(category, []) or []
            if category == "keywords":
                terms = [term for term in terms if term not in GENERIC_KEYWORDS]
            for term in terms:
                counter[term] += 1
    return {category: [term for term, _ in counter.most_common(6)] for category, counter in counters.items()}


def anchor_papers_for_cluster(
    cluster: List[str],
    edges: List[Dict[str, Any]],
    papers: Dict[str, Dict[str, Any]],
) -> List[str]:
    cluster_set = set(cluster)
    internal_degree = Counter()
    inbound = Counter()
    outbound = Counter()
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        if source in cluster_set:
            outbound[source] += 1
        if target in cluster_set:
            inbound[target] += 1
        if source in cluster_set and target in cluster_set:
            internal_degree[source] += 1
            internal_degree[target] += 1
    ranked = sorted(
        cluster,
        key=lambda pid: (
            internal_degree[pid],
            inbound[pid],
            outbound[pid],
            papers[pid].get("year") if isinstance(papers[pid].get("year"), int) else 0,
            pid,
        ),
        reverse=True,
    )
    return ranked[:5]


def provisional_label(parent_label: str, top_terms: Dict[str, List[str]]) -> str:
    parts: List[str] = []
    for category in ("keywords", "frameworks", "brain_regions", "tasks"):
        for term in top_terms.get(category, []):
            if term and term not in parts:
                parts.append(term)
            if len(parts) >= 3:
                break
        if len(parts) >= 3:
            break
    if not parts:
        return f"{parent_label} Subtopic"
    return f"{parent_label}: " + ", ".join(part.replace("_", " ") for part in parts[:3])


def build_subtopics_for_parent(
    parent: Dict[str, Any],
    papers: Dict[str, Dict[str, Any]],
    edges: List[Dict[str, Any]],
    adjacency: Dict[str, Set[str]],
) -> Tuple[List[OrderedDict[str, Any]], List[str], int]:
    nodes = list(parent["candidate_papers"])
    pair_weights: Dict[Tuple[str, str], float] = {}
    for idx, a in enumerate(nodes):
        for b in nodes[idx + 1 :]:
            weight = pair_similarity(a, b, papers, adjacency)
            if weight > 0:
                pair_weights[(a, b)] = weight

    clusters, orphans, cluster_count = cluster_by_seeds(nodes, pair_weights, adjacency)
    subtopics: List[OrderedDict[str, Any]] = []
    for idx, cluster in enumerate(sorted(clusters, key=len, reverse=True), start=1):
        cluster_set = set(cluster)
        top_terms = cluster_top_terms(cluster, papers)
        anchor_ids = anchor_papers_for_cluster(cluster, edges, papers)
        internal_edges = internal_edge_count(cluster_set, edges)
        avg_pair_weight = 0.0
        weights = []
        for i, a in enumerate(cluster):
            for b in cluster[i + 1 :]:
                weights.append(pair_weights.get(tuple(sorted((a, b))), 0.0))
        if weights:
            avg_pair_weight = round(sum(weights) / len(weights), 2)

        subtopics.append(
            OrderedDict(
                [
                    ("subtopic_id", f"{parent['topic_id']}__{idx:02d}"),
                    ("parent_topic_id", parent["topic_id"]),
                    ("parent_label", parent["label"]),
                    ("provisional_label", provisional_label(parent["label"], top_terms)),
                    ("candidate_papers", cluster),
                    ("anchor_papers", anchor_ids),
                    ("core_papers", cluster[: min(8, len(cluster))]),
                    ("supporting_papers", cluster[8: min(15, len(cluster))]),
                    (
                        "source_signals",
                        OrderedDict(
                            [
                                ("support_count", len(cluster)),
                                ("internal_citation_edges", internal_edges),
                                ("average_pair_weight", avg_pair_weight),
                                ("target_cluster_count", cluster_count),
                            ]
                        ),
                    ),
                    ("top_terms", OrderedDict((category, terms) for category, terms in top_terms.items())),
                    (
                        "rationale",
                        f"Sub-cluster inside {parent['label']} with {len(cluster)} papers and {internal_edges} internal citation edges.",
                    ),
                ]
            )
        )
    return subtopics, orphans, cluster_count


def build_payload(max_parent_topics: int) -> OrderedDict[str, Any]:
    paper_index, citation_edges, topic_candidates = load_payloads()
    papers = {paper["paper_id"]: paper for paper in paper_index["papers"]}
    edges = citation_edges["edges"]
    adjacency = build_adjacency(edges)
    parents = choose_parent_topics(topic_candidates, max_parent_topics)

    parent_summaries: List[OrderedDict[str, Any]] = []
    all_subtopics: List[OrderedDict[str, Any]] = []
    for parent in parents:
        subtopics, orphans, target_cluster_count = build_subtopics_for_parent(parent, papers, edges, adjacency)
        parent_summaries.append(
            OrderedDict(
                [
                    ("topic_id", parent["topic_id"]),
                    ("label", parent["label"]),
                    ("support_count", parent["source_signals"]["support_count"]),
                    ("subtopic_count", len(subtopics)),
                    ("orphan_papers", orphans),
                    ("target_cluster_count", target_cluster_count),
                ]
            )
        )
        all_subtopics.extend(subtopics)

    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("parent_topic_count", len(parent_summaries)),
            ("subtopic_count", len(all_subtopics)),
            ("parent_topics", parent_summaries),
            ("subtopics", all_subtopics),
        ]
    )


def main() -> int:
    args = parse_args()
    payload = build_payload(args.max_parent_topics)
    if args.write:
        write_yaml(SUBTOPIC_CANDIDATES_PATH, payload)
    print(
        f"Built {payload['subtopic_count']} subtopic candidates from {payload['parent_topic_count']} parent topics"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
