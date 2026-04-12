#!/usr/bin/env python3
"""Build first-pass topic candidates from the citation graph and paper index."""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

from normalize_summaries import DERIVED_DIR, parse_simple_yaml, write_yaml


PAPER_INDEX_PATH = DERIVED_DIR / "paper_index.yaml"
CITATION_EDGES_PATH = DERIVED_DIR / "citation_edges.yaml"
TOPIC_CANDIDATES_PATH = DERIVED_DIR / "topic_candidates.yaml"


CATEGORY_WEIGHTS = {
    "frameworks": 4.0,
    "keywords": 3.0,
    "tasks": 2.5,
    "brain_regions": 2.0,
    "methods": 1.5,
}

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
}


TOPIC_BLUEPRINTS: List[Dict[str, Any]] = [
    {
        "topic_id": "cognitive_maps",
        "label": "Cognitive Maps",
        "tier": "primary",
        "terms": {
            "keywords": ["cognitive_map", "spatial_navigation", "spatial_memory"],
            "frameworks": ["tolman_eichenbaum_machine"],
            "tasks": ["navigation_task", "virtual_navigation", "detour_task", "hexmaze"],
            "brain_regions": ["hippocampus", "entorhinal_cortex"],
        },
        "min_score": 7.0,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "predictive_maps_and_successor_representation",
        "label": "Predictive Maps and Successor Representation",
        "tier": "primary",
        "terms": {
            "frameworks": ["successor_representation", "temporal_difference_learning"],
            "keywords": ["successor_representation"],
            "brain_regions": ["hippocampus", "entorhinal_cortex"],
            "tasks": ["detour_task", "two_step_task"],
        },
        "min_score": 7.0,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "hippocampal_replay",
        "label": "Hippocampal Replay",
        "tier": "primary",
        "terms": {
            "keywords": ["replay", "hippocampal_replay", "sharp_wave_ripples", "memory_consolidation"],
            "brain_regions": ["hippocampus", "hippocampus_ca1", "hippocampus_ca3"],
            "tasks": ["linear_track", "t_maze"],
        },
        "min_score": 7.0,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "grid_cells_and_path_integration",
        "label": "Grid Cells and Path Integration",
        "tier": "primary",
        "terms": {
            "keywords": ["grid_cells", "path_integration"],
            "frameworks": ["attractor_networks"],
            "brain_regions": ["entorhinal_cortex", "medial_entorhinal_cortex"],
            "tasks": ["foraging_task", "navigation_task"],
        },
        "min_score": 7.0,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "model_based_and_model_free_rl",
        "label": "Model-Based and Model-Free Reinforcement Learning",
        "tier": "primary",
        "terms": {
            "frameworks": ["model_based_rl", "model_free_rl", "temporal_difference_learning"],
            "keywords": ["model_based_reinforcement_learning"],
            "tasks": ["two_step_task", "probabilistic_reversal_learning"],
        },
        "min_score": 6.5,
        "min_seed_matches": 2,
        "requires": [
            ("frameworks", ["model_based_rl", "model_free_rl", "temporal_difference_learning"]),
        ],
    },
    {
        "topic_id": "ofc_task_space_maps",
        "label": "OFC Task-Space Maps",
        "tier": "primary",
        "terms": {
            "brain_regions": ["orbitofrontal_cortex", "ventromedial_prefrontal_cortex"],
            "frameworks": ["model_based_rl"],
            "keywords": ["cognitive_map", "successor_representation", "model_based_reinforcement_learning"],
        },
        "min_score": 5.0,
        "min_seed_matches": 2,
        "requires": [
            ("brain_regions", ["orbitofrontal_cortex", "ventromedial_prefrontal_cortex"]),
        ],
    },
    {
        "topic_id": "hippocampal_prefrontal_coordination",
        "label": "Hippocampal-Prefrontal Coordination",
        "tier": "primary",
        "terms": {
            "brain_regions": ["hippocampus", "prefrontal_cortex", "medial_prefrontal_cortex"],
            "keywords": ["replay", "sharp_wave_ripples"],
        },
        "min_score": 7.5,
        "min_seed_matches": 2,
        "requires": [
            ("brain_regions", ["hippocampus", "hippocampus_ca1", "hippocampus_ca3"]),
            ("brain_regions", ["prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex"]),
        ],
    },
    {
        "topic_id": "dopamine_reward_prediction",
        "label": "Dopamine and Reward Prediction",
        "tier": "primary",
        "terms": {
            "brain_regions": ["ventral_tegmental_area", "substantia_nigra", "nucleus_accumbens", "ventral_striatum"],
            "frameworks": ["temporal_difference_learning", "model_free_rl"],
        },
        "min_score": 4.5,
        "min_seed_matches": 2,
        "requires": [
            ("brain_regions", ["ventral_tegmental_area", "substantia_nigra", "nucleus_accumbens", "ventral_striatum"]),
            ("frameworks", ["temporal_difference_learning", "model_free_rl"]),
        ],
    },
    {
        "topic_id": "hierarchical_planning_and_abstraction",
        "label": "Hierarchical Planning and Abstraction",
        "tier": "primary",
        "terms": {
            "frameworks": ["hierarchical_rl", "mixed_selectivity", "bayesian_inference"],
            "keywords": ["cognitive_map"],
            "brain_regions": ["prefrontal_cortex", "dorsolateral_prefrontal_cortex"],
            "tasks": ["two_step_task", "virtual_navigation"],
        },
        "min_score": 7.0,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "schemas_and_generalization",
        "label": "Schemas and Generalization",
        "tier": "primary",
        "terms": {
            "frameworks": ["tolman_eichenbaum_machine", "compositionality"],
            "keywords": ["cognitive_map", "memory_consolidation", "successor_representation"],
            "brain_regions": ["hippocampus", "orbitofrontal_cortex", "prefrontal_cortex"],
        },
        "min_score": 6.5,
        "min_seed_matches": 2,
    },
    {
        "topic_id": "astrocyte_gap_junction_networks",
        "label": "Astrocyte Gap-Junction Networks",
        "tier": "secondary",
        "terms": {
            "keywords": ["astrocytes", "gap_junctions"],
            "brain_regions": ["hippocampus_ca1", "hippocampus_ca3"],
        },
        "min_score": 5.0,
        "min_seed_matches": 1,
    },
    {
        "topic_id": "brain_atlas_and_registration",
        "label": "Brain Atlas and Registration Tooling",
        "tier": "secondary",
        "terms": {
            "keywords": [
                "image_registration",
                "neuroanatomy",
                "histological_brain_registration",
                "rodent_brain_atlas",
                "serial_two_photon_tomography",
            ],
        },
        "min_score": 3.0,
        "min_seed_matches": 1,
    },
    {
        "topic_id": "neuropixels_and_spike_sorting",
        "label": "Neuropixels and Spike Sorting",
        "tier": "secondary",
        "terms": {
            "keywords": ["neuropixels", "spike_sorting"],
            "methods": [],
        },
        "min_score": 3.0,
        "min_seed_matches": 1,
    },
    {
        "topic_id": "scientific_computing_practices",
        "label": "Scientific Computing Practices",
        "tier": "secondary",
        "terms": {
            "keywords": ["scientific_computing", "version_control", "data_management"],
        },
        "min_score": 3.0,
        "min_seed_matches": 1,
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write derived/topic_candidates.yaml.",
    )
    return parser.parse_args()


def load_payloads() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    paper_index = parse_simple_yaml(PAPER_INDEX_PATH.read_text())
    citation_edges = parse_simple_yaml(CITATION_EDGES_PATH.read_text())
    return paper_index, citation_edges


def normalize_topic_terms(blueprint: Dict[str, Any]) -> Dict[str, Set[str]]:
    normalized: Dict[str, Set[str]] = {}
    for category, terms in blueprint["terms"].items():
        normalized[category] = set(terms)
    return normalized


def has_required_groups(paper: Dict[str, Any], blueprint: Dict[str, Any]) -> bool:
    groups = blueprint.get("requires", [])
    if not groups:
        return True
    for category, terms in groups:
        values = set(paper.get(category, []) or [])
        if not values.intersection(terms):
            return False
    return True


def paper_topic_score(paper: Dict[str, Any], blueprint: Dict[str, Any]) -> Tuple[float, Dict[str, List[str]]]:
    matched: Dict[str, List[str]] = {}
    score = 0.0
    terms_by_category = normalize_topic_terms(blueprint)
    for category, seed_terms in terms_by_category.items():
        values = set(paper.get(category, []) or [])
        hits = sorted(values.intersection(seed_terms))
        if hits:
            matched[category] = hits
            score += CATEGORY_WEIGHTS.get(category, 1.0) * len(hits)
    if not has_required_groups(paper, blueprint):
        return 0.0, {}
    if matched and len(matched) >= 2:
        score += 1.0
    return score, matched


def citation_stats(edges: List[Dict[str, Any]]) -> Tuple[Counter, Counter, defaultdict]:
    inbound: Counter = Counter()
    outbound: Counter = Counter()
    adjacency: defaultdict = defaultdict(set)
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        outbound[source] += 1
        inbound[target] += 1
        adjacency[source].add(target)
        adjacency[target].add(source)
    return inbound, outbound, adjacency


def support_term_stats(candidate_ids: List[str], papers: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    counters = {
        "frameworks": Counter(),
        "brain_regions": Counter(),
        "tasks": Counter(),
        "keywords": Counter(),
    }
    for pid in candidate_ids:
        paper = papers[pid]
        for category, counter in counters.items():
            for term in paper.get(category, []) or []:
                if category == "keywords" and term in GENERIC_KEYWORDS:
                    continue
                counter[term] += 1
    result: Dict[str, List[str]] = {}
    for category, counter in counters.items():
        result[category] = [term for term, _ in counter.most_common(8)]
    return result


def internal_edge_count(candidate_set: Set[str], edges: List[Dict[str, Any]]) -> int:
    return sum(1 for edge in edges if edge["source"] in candidate_set and edge["target"] in candidate_set)


def topic_rationale(blueprint: Dict[str, Any], top_terms: Dict[str, List[str]], support_count: int, internal_edges: int) -> str:
    fragments = [f"{support_count} papers"]
    if internal_edges:
        fragments.append(f"{internal_edges} internal citation links")
    terms = []
    for category in ("frameworks", "brain_regions", "tasks", "keywords"):
        terms.extend(top_terms.get(category, [])[:2])
    if terms:
        fragments.append("dominant signals: " + ", ".join(terms[:6]))
    return f"{blueprint['label']} is a coherent candidate topic backed by " + "; ".join(fragments) + "."


def build_topic_candidates() -> OrderedDict[str, Any]:
    paper_index, citation_edges = load_payloads()
    papers = {paper["paper_id"]: paper for paper in paper_index["papers"]}
    edges = citation_edges["edges"]
    inbound, outbound, _ = citation_stats(edges)
    active_papers = set(inbound) | set(outbound)

    topics: List[OrderedDict[str, Any]] = []
    for blueprint in TOPIC_BLUEPRINTS:
        scored: List[Tuple[float, int, int, str, Dict[str, List[str]]]] = []
        for paper_id in active_papers:
            paper = papers[paper_id]
            score, matched = paper_topic_score(paper, blueprint)
            if score < blueprint["min_score"]:
                continue
            seed_match_count = sum(len(values) for values in matched.values())
            if seed_match_count < blueprint["min_seed_matches"]:
                continue
            scored.append((score, inbound[paper_id], outbound[paper_id], paper_id, matched))

        if len(scored) < 3:
            continue

        scored.sort(key=lambda item: (item[0], item[1], item[2], item[3]), reverse=True)
        candidate_ids = [paper_id for _, _, _, paper_id, _ in scored]
        candidate_set = set(candidate_ids)
        top_terms = support_term_stats(candidate_ids, papers)
        internal_edges = internal_edge_count(candidate_set, edges)
        density = round(internal_edges / max(len(candidate_ids), 1), 2)
        anchor_ids = [paper_id for _, _, _, paper_id, _ in sorted(scored, key=lambda item: (item[1], item[0], item[2]), reverse=True)[:5]]
        core_ids = candidate_ids[: min(10, len(candidate_ids))]
        supporting_ids = candidate_ids[10: min(25, len(candidate_ids))]

        keyword_hits = sum(1 for _, _, _, _, matched in scored if matched.get("keywords"))
        framework_hits = sum(1 for _, _, _, _, matched in scored if matched.get("frameworks"))
        region_hits = sum(1 for _, _, _, _, matched in scored if matched.get("brain_regions"))
        task_hits = sum(1 for _, _, _, _, matched in scored if matched.get("tasks"))

        seed_terms = []
        for category_terms in blueprint["terms"].values():
            seed_terms.extend(category_terms)

        topic = OrderedDict(
            [
                ("topic_id", blueprint["topic_id"]),
                ("label", blueprint["label"]),
                ("tier", blueprint["tier"]),
                ("seed_terms", seed_terms),
                ("candidate_papers", candidate_ids),
                ("anchor_papers", anchor_ids),
                ("core_papers", core_ids),
                ("supporting_papers", supporting_ids),
                (
                    "source_signals",
                    OrderedDict(
                        [
                            ("support_count", len(candidate_ids)),
                            ("internal_citation_edges", internal_edges),
                            ("edge_density", density),
                            ("framework_hits", framework_hits),
                            ("brain_region_hits", region_hits),
                            ("task_hits", task_hits),
                            ("keyword_hits", keyword_hits),
                        ]
                    ),
                ),
                ("top_terms", OrderedDict((category, terms) for category, terms in top_terms.items())),
                ("rationale", topic_rationale(blueprint, top_terms, len(candidate_ids), internal_edges)),
            ]
        )
        topics.append(topic)

    topics.sort(
        key=lambda topic: (
            topic["tier"] != "primary",
            -topic["source_signals"]["support_count"],
            -topic["source_signals"]["internal_citation_edges"],
            topic["topic_id"],
        )
    )

    by_id = {topic["topic_id"]: topic for topic in topics}
    candidate_sets = {topic["topic_id"]: set(topic["candidate_papers"]) for topic in topics}
    for topic in topics:
        overlaps = []
        current = candidate_sets[topic["topic_id"]]
        for other in topics:
            if other["topic_id"] == topic["topic_id"]:
                continue
            other_set = candidate_sets[other["topic_id"]]
            union = current | other_set
            if not union:
                continue
            jaccard = len(current & other_set) / len(union)
            if jaccard >= 0.5:
                overlaps.append(
                    OrderedDict(
                        [
                            ("topic_id", other["topic_id"]),
                            ("jaccard_overlap", round(jaccard, 2)),
                        ]
                    )
                )
        if overlaps:
            overlaps.sort(key=lambda item: (-item["jaccard_overlap"], item["topic_id"]))
            topic["review_flags"] = OrderedDict([("high_overlap_topics", overlaps)])

    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("topic_count", len(topics)),
            ("topics", topics),
        ]
    )


def main() -> int:
    args = parse_args()
    payload = build_topic_candidates()
    if args.write:
        write_yaml(TOPIC_CANDIDATES_PATH, payload)
    print(f"Built {payload['topic_count']} topic candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
