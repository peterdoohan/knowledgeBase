#!/usr/bin/env python3
"""Merge subtopic candidates with semantic judgments into a curated catalog."""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import DERIVED_DIR, parse_simple_yaml, write_yaml


SUBTOPIC_CANDIDATES_PATH = DERIVED_DIR / "subtopic_candidates.yaml"
SUBTOPIC_JUDGMENTS_PATH = DERIVED_DIR / "subtopic_judgments.jsonl"
SUBTOPIC_CATALOG_PATH = DERIVED_DIR / "subtopic_catalog.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write derived/subtopic_catalog.yaml.",
    )
    return parser.parse_args()


def load_judgments(path: Path) -> Dict[str, Dict[str, Any]]:
    judgments: Dict[str, Dict[str, Any]] = {}
    if not path.exists():
        return judgments
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        judgments[record["subtopic_id"]] = record
    return judgments


def merged_subtopic(subtopic: Dict[str, Any], judgment: Dict[str, Any] | None) -> OrderedDict[str, Any]:
    record = OrderedDict((key, value) for key, value in subtopic.items())
    if judgment is None:
        record["judgment_status"] = "pending"
        return record

    record["judgment_status"] = "judged"
    record["refined_label"] = judgment["refined_label"]
    record["page_type"] = judgment["page_type"]
    record["page_worthiness"] = judgment["page_worthiness"]
    record["keep"] = judgment["keep"]
    record["judge_summary"] = judgment["summary"]
    record["judge_reason_short"] = judgment["reason_short"]
    record["judge_metadata"] = OrderedDict(
        [
            ("judged_at", judgment["judged_at"]),
            ("provider", judgment["provider"]),
            ("model", judgment["model"]),
            ("prompt_version", judgment["prompt_version"]),
        ]
    )
    return record


def build_payload() -> OrderedDict[str, Any]:
    candidates = parse_simple_yaml(SUBTOPIC_CANDIDATES_PATH.read_text())
    judgments = load_judgments(SUBTOPIC_JUDGMENTS_PATH)

    merged = [merged_subtopic(subtopic, judgments.get(subtopic["subtopic_id"])) for subtopic in candidates["subtopics"]]
    selected = [subtopic for subtopic in merged if subtopic.get("keep")]
    selected.sort(
        key=lambda subtopic: (
            -int(subtopic.get("page_worthiness", 0)),
            subtopic.get("parent_topic_id", ""),
            subtopic["subtopic_id"],
        )
    )

    page_type_counts: Dict[str, int] = {}
    for subtopic in selected:
        page_type = str(subtopic.get("page_type", "unknown"))
        page_type_counts[page_type] = page_type_counts.get(page_type, 0) + 1

    parent_summary: List[OrderedDict[str, Any]] = []
    for parent in candidates["parent_topics"]:
        parent_id = parent["topic_id"]
        kept = [subtopic for subtopic in selected if subtopic["parent_topic_id"] == parent_id]
        parent_summary.append(
            OrderedDict(
                [
                    ("topic_id", parent_id),
                    ("label", parent["label"]),
                    ("candidate_subtopic_count", parent["subtopic_count"]),
                    ("selected_subtopic_count", len(kept)),
                    ("selected_subtopics", [subtopic["subtopic_id"] for subtopic in kept]),
                ]
            )
        )

    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("candidate_subtopic_count", len(merged)),
            ("selected_subtopic_count", len(selected)),
            ("selected_page_type_counts", OrderedDict(sorted(page_type_counts.items()))),
            ("parent_topics", parent_summary),
            ("selected_subtopics", selected),
            ("all_subtopics", merged),
        ]
    )


def main() -> int:
    args = parse_args()
    payload = build_payload()
    if args.write:
        write_yaml(SUBTOPIC_CATALOG_PATH, payload)
    print(
        f"Selected {payload['selected_subtopic_count']} subtopics "
        f"from {payload['candidate_subtopic_count']} candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
