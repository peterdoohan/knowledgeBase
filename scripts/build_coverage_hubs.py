#!/usr/bin/env python3
"""Audit wiki coverage and define second-wave parent hubs for undercovered domains."""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Set, Tuple

from normalize_summaries import DERIVED_DIR, parse_simple_yaml, write_yaml


PAPER_INDEX_PATH = DERIVED_DIR / "paper_index.yaml"
SUBTOPIC_CATALOG_PATH = DERIVED_DIR / "subtopic_catalog.yaml"
CITATION_EDGES_PATH = DERIVED_DIR / "citation_edges.yaml"
COVERAGE_AUDIT_PATH = DERIVED_DIR / "coverage_audit.yaml"
COVERAGE_HUBS_PATH = DERIVED_DIR / "coverage_parent_hubs.yaml"

CATEGORY_WEIGHTS = {
    "frameworks": 4.0,
    "keywords": 3.0,
    "tasks": 2.5,
    "brain_regions": 2.0,
    "methods": 1.5,
    "species": 1.0,
}

GENERIC_KEYWORDS = {
    "learning",
    "navigation",
    "spatial_navigation",
    "reinforcement_learning",
    "cognitive_map",
    "hippocampus",
    "prefrontal_cortex",
}

PARENT_HUB_BLUEPRINTS: List[Dict[str, Any]] = [
    {
        "topic_id": "prefrontal_goal_representation_and_control",
        "label": "Prefrontal Goal Representation and Cognitive Control",
        "terms": {
            "brain_regions": [
                "prefrontal_cortex",
                "medial_prefrontal_cortex",
                "prelimbic_cortex",
                "infralimbic_cortex",
                "dorsolateral_prefrontal_cortex",
            ],
            "keywords": [
                "goal_coding",
                "cognitive_control",
                "detour",
                "wayfinding",
                "planning",
            ],
            "tasks": ["detour_task", "virtual_navigation", "navigation_task", "two_step_task"],
        },
        "requires": [("brain_regions", ["prefrontal_cortex", "medial_prefrontal_cortex", "prelimbic_cortex", "infralimbic_cortex"])],
        "min_score": 6.0,
        "min_seed_matches": 2,
        "min_uncovered_count": 10,
    },
    {
        "topic_id": "ofc_task_state_and_value_maps",
        "label": "Orbitofrontal Task-State and Value Maps",
        "terms": {
            "brain_regions": ["orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "medial_orbitofrontal_cortex"],
            "frameworks": ["model_based_rl", "successor_representation", "bayesian_inference"],
            "keywords": ["task_state", "value", "cognitive_map", "latent_state", "state_representation"],
            "tasks": ["two_step_task", "probabilistic_reversal_learning"],
        },
        "requires": [("brain_regions", ["orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "medial_orbitofrontal_cortex"])],
        "min_score": 5.5,
        "min_seed_matches": 2,
        "min_uncovered_count": 6,
    },
    {
        "topic_id": "anterior_cingulate_future_state_and_model_based_control",
        "label": "Anterior Cingulate Future-State and Model-Based Control",
        "terms": {
            "brain_regions": ["anterior_cingulate_cortex", "prefrontal_cortex", "dorsomedial_striatum"],
            "frameworks": ["model_based_rl", "reinforcement_learning", "temporal_difference_learning"],
            "keywords": ["state_prediction", "future_state", "action_outcome", "credit_assignment"],
            "tasks": ["two_step_task"],
        },
        "requires": [("brain_regions", ["anterior_cingulate_cortex"])],
        "min_score": 5.5,
        "min_seed_matches": 2,
        "min_uncovered_count": 5,
    },
    {
        "topic_id": "hippocampal_prefrontal_coordination_and_planning",
        "label": "Hippocampal-Prefrontal Coordination and Planning",
        "terms": {
            "brain_regions": ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex"],
            "keywords": ["replay", "theta_sequences", "planning", "coordination", "vicarious_trial_and_error"],
            "tasks": ["t_maze", "detour_task", "navigation_task"],
        },
        "requires": [
            ("brain_regions", ["hippocampus", "hippocampus_ca1", "hippocampus_ca3"]),
            ("brain_regions", ["prefrontal_cortex", "medial_prefrontal_cortex", "prelimbic_cortex", "orbitofrontal_cortex"]),
        ],
        "min_score": 7.0,
        "min_seed_matches": 2,
        "min_uncovered_count": 8,
    },
    {
        "topic_id": "striatal_and_dopaminergic_reinforcement_learning",
        "label": "Striatal and Dopaminergic Reinforcement Learning",
        "terms": {
            "brain_regions": ["striatum", "ventral_striatum", "dorsomedial_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra"],
            "frameworks": ["model_free_rl", "model_based_rl", "temporal_difference_learning", "reinforcement_learning"],
            "keywords": ["reward_prediction_error", "dopamine", "policy_learning", "credit_assignment"],
            "tasks": ["two_step_task", "probabilistic_reversal_learning"],
        },
        "requires": [
            ("brain_regions", ["striatum", "ventral_striatum", "dorsomedial_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra"]),
            ("frameworks", ["model_free_rl", "temporal_difference_learning", "reinforcement_learning"]),
        ],
        "min_score": 6.0,
        "min_seed_matches": 2,
        "min_uncovered_count": 8,
    },
    {
        "topic_id": "clinical_and_computational_psychiatry",
        "label": "Clinical and Computational Psychiatry",
        "terms": {
            "species": ["human"],
            "frameworks": ["bayesian_inference", "active_inference", "successor_representation"],
            "keywords": ["schizophrenia", "psychosis", "computational_psychiatry", "delusions", "belief_updating"],
            "brain_regions": ["prefrontal_cortex", "striatum", "hippocampus"],
        },
        "requires": [("keywords", ["schizophrenia", "psychosis", "computational_psychiatry", "delusions"])],
        "min_score": 5.0,
        "min_seed_matches": 2,
        "min_uncovered_count": 6,
    },
    {
        "topic_id": "behavioral_paradigms_and_navigation_tasks",
        "label": "Behavioral Paradigms and Navigation Tasks",
        "terms": {
            "tasks": ["two_step_task", "detour_task", "virtual_navigation", "hexmaze", "foraging_task", "navigation_task"],
            "keywords": ["detour", "shortcut", "wayfinding", "navigation", "vicarious_trial_and_error"],
            "brain_regions": ["prefrontal_cortex", "hippocampus"],
        },
        "requires": [("tasks", ["two_step_task", "detour_task", "virtual_navigation", "hexmaze", "foraging_task", "navigation_task"])],
        "min_score": 5.0,
        "min_seed_matches": 2,
        "min_uncovered_count": 10,
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write audit and parent hub files.")
    return parser.parse_args()


def load_payloads() -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    paper_index = parse_simple_yaml(PAPER_INDEX_PATH.read_text())
    catalog = parse_simple_yaml(SUBTOPIC_CATALOG_PATH.read_text())
    citation_edges = parse_simple_yaml(CITATION_EDGES_PATH.read_text())
    return paper_index, catalog, citation_edges


def selected_paper_sets(catalog: Dict[str, Any]) -> Tuple[Set[str], Set[str]]:
    represented: Set[str] = set()
    anchor_or_core: Set[str] = set()
    for subtopic in catalog.get("selected_subtopics", []):
        for paper_id in subtopic.get("candidate_papers", []) or []:
            represented.add(paper_id)
        for paper_id in (subtopic.get("anchor_papers", []) or []) + (subtopic.get("core_papers", []) or []):
            anchor_or_core.add(paper_id)
    return represented, anchor_or_core


def has_required_groups(paper: Dict[str, Any], blueprint: Dict[str, Any]) -> bool:
    for category, terms in blueprint.get("requires", []):
        values = set(paper.get(category, []) or [])
        if not values.intersection(terms):
            return False
    return True


def score_paper(paper: Dict[str, Any], blueprint: Dict[str, Any]) -> Tuple[float, int]:
    score = 0.0
    seed_matches = 0
    for category, terms in blueprint["terms"].items():
        values = set(paper.get(category, []) or [])
        overlap = values.intersection(terms)
        if overlap:
            seed_matches += len(overlap)
            score += len(overlap) * CATEGORY_WEIGHTS[category]
    return score, seed_matches


def internal_edge_count(candidate_set: Set[str], edges: List[Dict[str, Any]]) -> int:
    return sum(1 for edge in edges if edge["source"] in candidate_set and edge["target"] in candidate_set)


def top_terms(paper_ids: Iterable[str], papers: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    counters = {
        "brain_regions": Counter(),
        "frameworks": Counter(),
        "tasks": Counter(),
        "keywords": Counter(),
    }
    for paper_id in paper_ids:
        paper = papers[paper_id]
        for category, counter in counters.items():
            for value in paper.get(category, []) or []:
                if category == "keywords" and value in GENERIC_KEYWORDS:
                    continue
                counter[value] += 1
    return OrderedDict((category, [term for term, _ in counter.most_common(8)]) for category, counter in counters.items())


def anchor_papers(candidate_ids: List[str], papers: Dict[str, Dict[str, Any]], edges: List[Dict[str, Any]]) -> List[str]:
    candidate_set = set(candidate_ids)
    inbound = Counter()
    outbound = Counter()
    for edge in edges:
        if edge["target"] in candidate_set:
            inbound[edge["target"]] += 1
        if edge["source"] in candidate_set:
            outbound[edge["source"]] += 1
    ranked = sorted(
        candidate_ids,
        key=lambda paper_id: (
            inbound[paper_id],
            outbound[paper_id],
            papers[paper_id].get("year") if isinstance(papers[paper_id].get("year"), int) else 0,
            paper_id,
        ),
        reverse=True,
    )
    return ranked[:5]


def dimension_rows(
    papers: Dict[str, Dict[str, Any]],
    represented: Set[str],
    uncovered: Set[str],
    category: str,
    min_total_count: int,
) -> List[OrderedDict[str, Any]]:
    total = Counter()
    represented_counter = Counter()
    uncovered_counter = Counter()
    for paper_id, paper in papers.items():
        values = paper.get(category, []) or []
        for value in values:
            total[value] += 1
            if paper_id in represented:
                represented_counter[value] += 1
            if paper_id in uncovered:
                uncovered_counter[value] += 1
    rows = []
    for value, total_count in total.most_common():
        if total_count < min_total_count:
            continue
        uncovered_count = uncovered_counter[value]
        rows.append(
            OrderedDict(
                [
                    ("term", value),
                    ("total_count", total_count),
                    ("represented_count", represented_counter[value]),
                    ("uncovered_count", uncovered_count),
                    ("coverage_ratio", round(represented_counter[value] / total_count, 3)),
                ]
            )
        )
    return rows[:20]


def build_hubs(
    papers: Dict[str, Dict[str, Any]],
    represented: Set[str],
    uncovered: Set[str],
    edges: List[Dict[str, Any]],
) -> List[OrderedDict[str, Any]]:
    hubs: List[OrderedDict[str, Any]] = []
    for blueprint in PARENT_HUB_BLUEPRINTS:
        candidate_ids: List[str] = []
        uncovered_ids: List[str] = []
        for paper_id, paper in papers.items():
            if not has_required_groups(paper, blueprint):
                continue
            score, seed_matches = score_paper(paper, blueprint)
            if score < blueprint["min_score"] or seed_matches < blueprint["min_seed_matches"]:
                continue
            candidate_ids.append(paper_id)
            if paper_id in uncovered:
                uncovered_ids.append(paper_id)
        if len(uncovered_ids) < blueprint["min_uncovered_count"]:
            continue
        candidate_ids.sort()
        uncovered_ids.sort()
        candidate_set = set(candidate_ids)
        hubs.append(
            OrderedDict(
                [
                    ("topic_id", blueprint["topic_id"]),
                    ("label", blueprint["label"]),
                    ("tier", "coverage"),
                    ("candidate_papers", candidate_ids),
                    ("uncovered_candidate_papers", uncovered_ids),
                    ("anchor_papers", anchor_papers(candidate_ids, papers, edges)),
                    (
                        "source_signals",
                        OrderedDict(
                            [
                                ("support_count", len(candidate_ids)),
                                ("uncovered_support_count", len(uncovered_ids)),
                                ("uncovered_ratio", round(len(uncovered_ids) / len(candidate_ids), 3)),
                                ("internal_citation_edges", internal_edge_count(candidate_set, edges)),
                            ]
                        ),
                    ),
                    ("top_terms", top_terms(uncovered_ids or candidate_ids, papers)),
                    (
                        "rationale",
                        f"Coverage hub for an underrepresented domain with {len(uncovered_ids)} uncovered papers "
                        f"out of {len(candidate_ids)} total candidates.",
                    ),
                ]
            )
        )
    hubs.sort(
        key=lambda hub: (
            -hub["source_signals"]["uncovered_support_count"],
            -hub["source_signals"]["support_count"],
            hub["topic_id"],
        )
    )
    return hubs


def build_audit_payload(
    papers: Dict[str, Dict[str, Any]],
    represented: Set[str],
    anchor_or_core: Set[str],
    hubs: List[OrderedDict[str, Any]],
) -> OrderedDict[str, Any]:
    all_paper_ids = set(papers)
    uncovered = all_paper_ids - represented
    support_only = represented - anchor_or_core
    high_signal_uncovered = sorted(
        uncovered,
        key=lambda paper_id: (
            len(papers[paper_id].get("brain_regions", []) or []),
            len(papers[paper_id].get("frameworks", []) or []),
            papers[paper_id].get("year") if isinstance(papers[paper_id].get("year"), int) else 0,
            paper_id,
        ),
        reverse=True,
    )[:25]
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("paper_count", len(all_paper_ids)),
            ("represented_paper_count", len(represented)),
            ("anchor_or_core_paper_count", len(anchor_or_core)),
            ("support_only_paper_count", len(support_only)),
            ("uncovered_paper_count", len(uncovered)),
            ("coverage_ratio", round(len(represented) / len(all_paper_ids), 3)),
            ("high_signal_uncovered_papers", high_signal_uncovered),
            (
                "undercovered_dimensions",
                OrderedDict(
                    [
                        ("brain_regions", dimension_rows(papers, represented, uncovered, "brain_regions", 10)),
                        ("frameworks", dimension_rows(papers, represented, uncovered, "frameworks", 6)),
                        ("tasks", dimension_rows(papers, represented, uncovered, "tasks", 5)),
                        ("methods", dimension_rows(papers, represented, uncovered, "methods", 8)),
                    ]
                ),
            ),
            (
                "recommended_parent_hubs",
                [
                    OrderedDict(
                        [
                            ("topic_id", hub["topic_id"]),
                            ("label", hub["label"]),
                            ("support_count", hub["source_signals"]["support_count"]),
                            ("uncovered_support_count", hub["source_signals"]["uncovered_support_count"]),
                            ("uncovered_ratio", hub["source_signals"]["uncovered_ratio"]),
                        ]
                    )
                    for hub in hubs
                ],
            ),
        ]
    )


def main() -> int:
    args = parse_args()
    paper_index, catalog, citation_edges = load_payloads()
    papers = {paper["paper_id"]: paper for paper in paper_index["papers"]}
    edges = citation_edges["edges"]
    represented, anchor_or_core = selected_paper_sets(catalog)
    uncovered = set(papers) - represented

    hubs = build_hubs(papers, represented, uncovered, edges)
    audit_payload = build_audit_payload(papers, represented, anchor_or_core, hubs)
    hubs_payload = OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("represented_paper_count", len(represented)),
            ("uncovered_paper_count", len(uncovered)),
            ("parent_hub_count", len(hubs)),
            ("parent_hubs", hubs),
        ]
    )

    if args.write:
        write_yaml(COVERAGE_AUDIT_PATH, audit_payload)
        write_yaml(COVERAGE_HUBS_PATH, hubs_payload)

    print(
        f"Coverage audit: {audit_payload['represented_paper_count']} represented / "
        f"{audit_payload['paper_count']} total papers; {hubs_payload['parent_hub_count']} parent hubs proposed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
