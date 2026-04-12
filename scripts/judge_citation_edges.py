#!/usr/bin/env python3
"""Judge ambiguous citation candidates with a single LLM pass."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import sys
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from normalize_summaries import DERIVED_DIR, PAPER_INDEX_PATH, parse_simple_yaml


CITATION_CANDIDATES_PATH = DERIVED_DIR / "citation_candidates.yaml"
JUDGMENTS_PATH = DERIVED_DIR / "citation_judgments.jsonl"
DOTENV_PATH = DERIVED_DIR.parent / ".env"
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
        choices=("anthropic_api", "openai_api", "claude"),
        default="anthropic_api",
        help="Judge backend to use.",
    )
    parser.add_argument(
        "--model",
        default="claude-opus-4-6",
        help="Judge model name. Defaults to Claude Opus 4.6; pass gpt-5.4 for OpenAI.",
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
        "--max-workers",
        type=int,
        default=4,
        help="Number of concurrent judge requests to run.",
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


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ[key] = value


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


def parse_json_text(text: str) -> Dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].strip()
    return json.loads(cleaned)


def run_claude(prompt: str) -> Dict[str, Any]:
    import subprocess

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


def run_anthropic_api(prompt: str, model: str) -> Dict[str, Any]:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    payload = {
        "model": model,
        "max_tokens": 256,
        "temperature": 0,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }
    request = urllib.request.Request(
        url="https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"anthropic api error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"anthropic api request failed: {exc}") from exc

    parsed = json.loads(body)
    parts = parsed.get("content", []) or []
    text_chunks = [part.get("text", "") for part in parts if part.get("type") == "text"]
    text = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    if not text:
        raise RuntimeError("anthropic api returned no text content")
    return parse_json_text(text)


def run_openai_api(prompt: str, model: str) -> Dict[str, Any]:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    payload = {
        "model": model,
        "input": prompt,
        "text": {
            "verbosity": "low",
        },
        "reasoning": {
            "effort": "low",
        },
    }
    request = urllib.request.Request(
        url="https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"openai api error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"openai api request failed: {exc}") from exc

    parsed = json.loads(body)
    output = parsed.get("output", []) or []
    text_chunks = []
    for item in output:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text":
                text_chunks.append(content.get("text", ""))
    text = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    if not text:
        raise RuntimeError("openai api returned no text content")
    return parse_json_text(text)


def judge_candidate(
    candidate: Dict[str, Any],
    paper_index: Dict[str, Dict[str, Any]],
    provider: str,
    model: str,
) -> OrderedDict[str, Any]:
    prompt = build_prompt(candidate, paper_index)
    if provider == "anthropic_api":
        result = run_anthropic_api(prompt, model)
    elif provider == "openai_api":
        result = run_openai_api(prompt, model)
    else:
        result = run_claude(prompt)
    return OrderedDict(
        [
            ("candidate_id", candidate["candidate_id"]),
            ("judged_at", datetime.now(timezone.utc).isoformat()),
            ("provider", provider),
            ("model", model),
            ("prompt_version", PROMPT_VERSION),
            ("accept", bool(result["accept"])),
            ("best_target", result["best_target"]),
            ("confidence", int(result["confidence"])),
            ("reason_short", str(result["reason_short"]).strip()),
        ]
    )


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
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

    max_workers = max(1, args.max_workers)
    judged = 0
    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(judge_candidate, candidate, paper_index, args.provider, args.model): candidate
            for candidate in pending
        }
        for future in concurrent.futures.as_completed(futures):
            candidate = futures[future]
            try:
                record = future.result()
            except Exception as exc:
                failed += 1
                print(
                    f"[{judged + failed}/{len(pending)}] {candidate['candidate_id']} error={exc}",
                    file=sys.stderr,
                )
                sys.stderr.flush()
                continue

            append_jsonl(JUDGMENTS_PATH, record)
            judged += 1
            print(
                f"[{judged + failed}/{len(pending)}] {candidate['candidate_id']} "
                f"accept={record['accept']} target={record['best_target']} conf={record['confidence']}"
            )
            sys.stdout.flush()

    print(f"Completed judgments: {judged} succeeded, {failed} failed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
