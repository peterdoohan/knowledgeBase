#!/usr/bin/env python3
"""Deprecate overlapping wiki pages in favor of a smaller canonical set."""

from __future__ import annotations

import argparse
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import REPO_ROOT, dump_yaml, parse_frontmatter, split_frontmatter, write_yaml


WIKI_DIR = REPO_ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
PRUNE_PLAN_PATH = REPO_ROOT / "derived" / "wiki_prune_plan.yaml"

REDUNDANCY_MAP: List[Dict[str, str]] = [
    {
        "deprecated": "wiki/topics/successor_representation_accounts_of_hippocampal_place_cells_and_entorhinal_grid_cells.md",
        "canonical": "wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md",
        "reason": "Overlaps heavily with the broader hippocampal predictive-maps synthesis and adds little unique structure.",
    },
    {
        "deprecated": "wiki/topics/successor_representation_as_a_predictive_map_account_of_hippocampal_place_cells.md",
        "canonical": "wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md",
        "reason": "Too narrow relative to the broader predictive-maps page and largely rephrases the same place-cell argument.",
    },
    {
        "deprecated": "wiki/topics/successor_representations_in_hippocampal_entorhinal_cognitive_maps.md",
        "canonical": "wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md",
        "reason": "Semantically duplicates the hippocampal-entorhinal predictive-maps page with weaker boundaries.",
    },
    {
        "deprecated": "wiki/topics/successor_representations_and_grid_cell_predictive_maps_in_spatial_navigation.md",
        "canonical": "wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md",
        "reason": "Spatial-navigation framing overlaps with the predictive-maps page and does not justify a separate canonical entry.",
    },
    {
        "deprecated": "wiki/topics/successor_representation_and_hierarchical_planning_in_navigation.md",
        "canonical": "wiki/topics/hierarchical_planning_and_successor_representations_in_prefrontal_hippocampal_cognitive_control.md",
        "reason": "The navigation-specific page is thinner than the broader hierarchical-planning synthesis and splits the same argument across two pages.",
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write deprecation stubs and prune plan.")
    return parser.parse_args()


def page_title(path: Path) -> str:
    frontmatter_block, body = split_frontmatter(path.read_text())
    frontmatter = parse_frontmatter(frontmatter_block)
    title = str(frontmatter.get("title", "")).strip()
    if title:
        return title
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def prune_stub(deprecated_path: Path, canonical_path: Path, reason: str) -> str:
    deprecated_title = page_title(deprecated_path)
    canonical_title = page_title(canonical_path)
    frontmatter_block, _ = split_frontmatter(deprecated_path.read_text())
    old_frontmatter = parse_frontmatter(frontmatter_block)
    payload = OrderedDict(
        [
            ("title", deprecated_title),
            ("status", "deprecated"),
            ("deprecated_at", datetime.now(timezone.utc).isoformat()),
            ("superseded_by", str(canonical_path.relative_to(REPO_ROOT).with_suffix(""))),
            ("generated_by", "prune_wiki_redundancy.py"),
        ]
    )
    for key in ("subtopic_id", "parent_topic_id", "page_type"):
        value = old_frontmatter.get(key)
        if value:
            payload[key] = value
    body = "\n".join(
        [
            f"# {deprecated_title}",
            "",
            f"This page was deprecated in the merge/prune pass because it overlapped too heavily with [[{canonical_path.relative_to(REPO_ROOT).with_suffix('')}|{canonical_title}]].",
            "",
            f"Reason: {reason}",
            "",
            f"Canonical page: [[{canonical_path.relative_to(REPO_ROOT).with_suffix('')}|{canonical_title}]]",
            "",
        ]
    )
    return "---\n" + "\n".join(dump_yaml(payload)) + "\n---\n\n" + body


def build_prune_plan() -> OrderedDict[str, Any]:
    entries: List[OrderedDict[str, Any]] = []
    for mapping in REDUNDANCY_MAP:
        deprecated_path = REPO_ROOT / mapping["deprecated"]
        canonical_path = REPO_ROOT / mapping["canonical"]
        entries.append(
            OrderedDict(
                [
                    ("deprecated", mapping["deprecated"]),
                    ("canonical", mapping["canonical"]),
                    ("deprecated_title", page_title(deprecated_path)),
                    ("canonical_title", page_title(canonical_path)),
                    ("reason", mapping["reason"]),
                ]
            )
        )
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("deprecated_page_count", len(entries)),
            ("entries", entries),
        ]
    )


def main() -> int:
    args = parse_args()
    plan = build_prune_plan()
    if args.write:
        write_yaml(PRUNE_PLAN_PATH, plan)
        for mapping in REDUNDANCY_MAP:
            deprecated_path = REPO_ROOT / mapping["deprecated"]
            canonical_path = REPO_ROOT / mapping["canonical"]
            deprecated_path.write_text(prune_stub(deprecated_path, canonical_path, mapping["reason"]))
    print(f"Prepared prune plan for {plan['deprecated_page_count']} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
