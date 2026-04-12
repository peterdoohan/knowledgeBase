#!/usr/bin/env python3
"""Judge ambiguous citation candidates with a single LLM pass."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from normalize_summaries import DERIVED_DIR, PAPER_INDEX_PATH, parse_simple_yaml


CITATION_CANDIDATES_PATH = DERIVED_DIR / "citation_candidates.yaml"
JUDGMENTS_PATH = DERIVED_DIR / "citation_judgments.jsonl"
PROMPT_VERSION = "citation-judge-v1"
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "accept": {"type": "boolean"},
        "best_target": {"type": ["string", "null"]},
        "confidence": {"type": "integer", "minimum": 1, "maximum": 5},
        "reason_short": {"type": "string"},
    },
    "required": ["accept", "best_target", "confidence", "reason_short"],
    "additionalProperties": False,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        choices=("claude",),
        default="claude",
        help="Judge backend to use.",
    )
    parser.add_argument(
        "--candidate-id",
        action="append",
        default=[],
        help="Restrict judging to one or more candidate IDs.",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=None,
        help="Limit the number of candidates judged in this run.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rejudge candidates even if a judgment already exists.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    records: List[Dict[str, Any]] = []
    for line in path.read_text().splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def load_paper_index() -> Dict[str, Dict[str, Any]]:
    payload = parse_simple_yaml(PAPER_INDEX_PATH.read_text())
    papers = payload.get("papers", []) or []
    return {paper["paper_id"]: paper for paper in papers}


def load_candidates() -> List[Dict[str, Any]]:
    payload = parse_simple_yaml(CITATION_CANDIDATES_PATH.read_text())
    return payload.get("candidates", []) or []


def should_judge(candidate: Dict[str, Any]) -> bool:
    return not (
        candidate.get("deterministic_confidence") == "high"
        and len(candidate.get("candidate_targets", [])) == 1
    )


def build_prompt(candidate: Dict[str, Any], paper_index: Dict[str, Dict[str, Any]]) -> str:
    source = paper_index[candidate["source"]]
    target_blocks = []
    for target_id in candidate["candidate_targets"]:
        target = paper_index[target_id]
        target_blocks.append(
            "\n".join(
                [
                    f"Target paper_id: {target_id}",
                    f"Title: {target.get('title', '')}",
                    f"Authors: {', '.join(target.get('authors', []) or [])}",
                    f"Year: {target.get('year', '')}",
                    f"One-line summary: {target.get('one_line_summary', '')}",
                ]
            )
        )
    return "\n\n".join(
        [
            "You are judging whether an in-corpus citation candidate is a real citation to one of the candidate target papers.",
            "Be conservative. Reject if the evidence is too weak or the target is unclear.",
            "Return JSON only.",
            "Decision rules:",
            "- accept=true only if the excerpt plausibly cites the exact target paper",
            "- best_target must be one of the provided candidate target paper_ids or null",
            "- confidence is 1-5",
            "- keep reason_short under 20 words",
            "",
            f"Source paper_id: {candidate['source']}",
            f"Source title: {source.get('title', '')}",
            f"Source one-line summary: {source.get('one_line_summary', '')}",
            f"Section: {candidate['section']}",
            f"Mention text: {candidate['mention_text']}",
            f"Evidence excerpt: {candidate['evidence_excerpt']}",
            f"Extraction method: {candidate['extraction_method']}",
            f"Deterministic confidence: {candidate['deterministic_confidence']}",
            "",
            "Candidate targets:",
            "\n\n".join(target_blocks),
        ]
    )


def run_claude(prompt: str) -> Dict[str, Any]:
    cmd = [
        "claude",
        "-p",
        "--output-format",
        "json",
        "--json-schema",
        json.dumps(JUDGE_SCHEMA),
        prompt,
    ]
    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("claude call timed out") from exc
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "claude call failed")
    output = completed.stdout.strip()
    if not output:
        raise RuntimeError("claude returned empty output")
    return json.loads(output)


def main() -> int:
    args = parse_args()
    paper_index = load_paper_index()
    candidates = load_candidates()
    existing = {record["candidate_id"]: record for record in load_jsonl(JUDGMENTS_PATH)}
    requested = set(args.candidate_id)

    pending: List[Dict[str, Any]] = []
    for candidate in candidates:
        if requested and candidate["candidate_id"] not in requested:
            continue
        if not should_judge(candidate):
            continue
        if not args.force and candidate["candidate_id"] in existing:
            continue
        pending.append(candidate)

    if args.max_candidates is not None:
        pending = pending[: args.max_candidates]

    if not pending:
        print("No citation candidates require judgment.")
        return 0

    judged = 0
    for candidate in pending:
        prompt = build_prompt(candidate, paper_index)
        result = run_claude(prompt)
        record = OrderedDict(
            [
                ("candidate_id", candidate["candidate_id"]),
                ("judged_at", datetime.now(timezone.utc).isoformat()),
                ("provider", args.provider),
                ("prompt_version", PROMPT_VERSION),
                ("accept", bool(result["accept"])),
                ("best_target", result["best_target"]),
                ("confidence", int(result["confidence"])),
                ("reason_short", str(result["reason_short"]).strip()),
            ]
        )
        append_jsonl(JUDGMENTS_PATH, record)
        judged += 1
        print(
            f"[{judged}/{len(pending)}] {candidate['candidate_id']} "
            f"accept={record['accept']} target={record['best_target']} conf={record['confidence']}"
        )
        sys.stdout.flush()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
