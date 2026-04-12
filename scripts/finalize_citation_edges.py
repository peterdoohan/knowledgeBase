#!/usr/bin/env python3
"""Finalize citation_edges.yaml from candidates and judge outputs."""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from normalize_summaries import DERIVED_DIR, parse_simple_yaml, write_yaml


CITATION_CANDIDATES_PATH = DERIVED_DIR / "citation_candidates.yaml"
JUDGMENTS_PATH = DERIVED_DIR / "citation_judgments.jsonl"
CITATION_EDGES_PATH = DERIVED_DIR / "citation_edges.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write derived/citation_edges.yaml.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> Dict[str, Dict[str, Any]]:
    if not path.exists():
        return {}
    records: Dict[str, Dict[str, Any]] = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        records[record["candidate_id"]] = record
    return records


def edge_rank(confidence: str) -> int:
    return {"high": 3, "medium": 2, "low": 1}.get(confidence, 0)


def finalize_edges() -> OrderedDict[str, Any]:
    payload = parse_simple_yaml(CITATION_CANDIDATES_PATH.read_text())
    candidates = payload.get("candidates", []) or []
    judgments = load_jsonl(JUDGMENTS_PATH)

    edge_map: Dict[Tuple[str, str], Dict[str, Any]] = {}
    auto_accept_count = 0
    judged_accept_count = 0
    unresolved_count = 0

    for candidate in candidates:
        source = candidate["source"]
        target = None
        confidence = None
        judge_status = "not_judged"

        if candidate.get("deterministic_confidence") == "high" and len(candidate.get("candidate_targets", [])) == 1:
            target = candidate["candidate_targets"][0]
            confidence = "high"
            judge_status = "skipped_deterministic"
            auto_accept_count += 1
        else:
            judgment = judgments.get(candidate["candidate_id"])
            if judgment and judgment.get("accept") and judgment.get("best_target") in candidate.get("candidate_targets", []):
                target = judgment["best_target"]
                confidence = "high" if int(judgment.get("confidence", 0)) >= 5 else "medium"
                judge_status = "accepted_by_judge"
                judged_accept_count += 1
            else:
                unresolved_count += 1
                continue

        if not target or target == source:
            unresolved_count += 1
            continue

        key = (source, target)
        evidence = OrderedDict(
            [
                ("section", candidate["section"]),
                ("mention_text", candidate["mention_text"]),
                ("evidence_excerpt", candidate["evidence_excerpt"]),
                ("extraction_method", candidate["extraction_method"]),
                ("judge_status", judge_status),
            ]
        )

        if key not in edge_map:
            edge_map[key] = {
                "source": source,
                "target": target,
                "type": "cites",
                "confidence": confidence,
                "mention_count": 1,
                "evidence": evidence,
            }
            continue

        edge_map[key]["mention_count"] += 1
        if edge_rank(confidence) > edge_rank(edge_map[key]["confidence"]):
            edge_map[key]["confidence"] = confidence
            edge_map[key]["evidence"] = evidence

    edges = []
    for key in sorted(edge_map):
        edge = edge_map[key]
        edges.append(
            OrderedDict(
                [
                    ("source", edge["source"]),
                    ("target", edge["target"]),
                    ("type", edge["type"]),
                    ("confidence", edge["confidence"]),
                    ("mention_count", edge["mention_count"]),
                    ("evidence", edge["evidence"]),
                ]
            )
        )

    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("edge_count", len(edges)),
            ("auto_accept_count", auto_accept_count),
            ("judged_accept_count", judged_accept_count),
            ("unresolved_count", unresolved_count),
            ("edges", edges),
        ]
    )


def main() -> int:
    payload = finalize_edges()
    if args := parse_args():
        if args.write:
            write_yaml(CITATION_EDGES_PATH, payload)
    print(
        f"Finalized {payload['edge_count']} citation edges "
        f"({payload['auto_accept_count']} auto, {payload['judged_accept_count']} judged, "
        f"{payload['unresolved_count']} unresolved)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
