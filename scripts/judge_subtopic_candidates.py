#!/usr/bin/env python3
"""Judge subtopic candidates for page-worthiness and refine labels."""

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
from typing import Any, Dict, List

from normalize_summaries import DERIVED_DIR, parse_simple_yaml


SUBTOPIC_CANDIDATES_PATH = DERIVED_DIR / "subtopic_candidates.yaml"
PAPER_INDEX_PATH = DERIVED_DIR / "paper_index.yaml"
JUDGMENTS_PATH = DERIVED_DIR / "subtopic_judgments.jsonl"
DOTENV_PATH = DERIVED_DIR.parent / ".env"
PROMPT_VERSION = "subtopic-judge-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        choices=("openai_api",),
        default="openai_api",
        help="Judge backend to use.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4",
        help="Judge model name.",
    )
    parser.add_argument(
        "--subtopic-id",
        action="append",
        default=[],
        help="Restrict judging to one or more subtopic IDs.",
    )
    parser.add_argument(
        "--subtopic-candidates-path",
        default=str(SUBTOPIC_CANDIDATES_PATH),
        help="Path to the subtopic candidate YAML file to judge.",
    )
    parser.add_argument(
        "--judgments-path",
        default=str(JUDGMENTS_PATH),
        help="Path to the JSONL file where judgments should be appended.",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=None,
        help="Limit the number of subtopics judged in this run.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Number of concurrent judge requests to run.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rejudge subtopics even if a judgment already exists.",
    )
    return parser.parse_args()


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip().strip('"').strip("'")


def load_jsonl(path: Path) -> Dict[str, Dict[str, Any]]:
    if not path.exists():
        return {}
    records: Dict[str, Dict[str, Any]] = {}
    for line in path.read_text().splitlines():
        if line.strip():
            record = json.loads(line)
            records[record["subtopic_id"]] = record
    return records


def append_jsonl(path: Path, record: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def load_payloads(subtopic_candidates_path: Path) -> tuple[Dict[str, Any], Dict[str, Dict[str, Any]]]:
    subtopics = parse_simple_yaml(subtopic_candidates_path.read_text())
    paper_index = parse_simple_yaml(PAPER_INDEX_PATH.read_text())
    papers = {paper["paper_id"]: paper for paper in paper_index["papers"]}
    return subtopics, papers


def build_prompt(subtopic: Dict[str, Any], papers: Dict[str, Dict[str, Any]]) -> str:
    anchor_blocks = []
    for paper_id in subtopic["anchor_papers"][:5]:
        paper = papers[paper_id]
        anchor_blocks.append(
            "\n".join(
                [
                    f"paper_id: {paper_id}",
                    f"title: {paper.get('title', '')}",
                    f"year: {paper.get('year', '')}",
                    f"one_line_summary: {paper.get('one_line_summary', '')}",
                ]
            )
        )
    return "\n\n".join(
        [
            "You are judging whether this subtopic is a good wiki page candidate.",
            "Be conservative. Prefer narrow, evidence-dense pages over broad fields.",
            "Return JSON only with this schema:",
            '{"refined_label": string, "page_type": "topic"|"debate"|"methods"|"tooling"|"reject", "page_worthiness": 1-5, "keep": boolean, "summary": string, "reason_short": string}',
            "",
            f"Parent topic: {subtopic['parent_label']}",
            f"Subtopic ID: {subtopic['subtopic_id']}",
            f"Provisional label: {subtopic['provisional_label']}",
            f"Support count: {subtopic['source_signals']['support_count']}",
            f"Internal citation edges: {subtopic['source_signals']['internal_citation_edges']}",
            f"Top frameworks: {', '.join(subtopic['top_terms']['frameworks'])}",
            f"Top brain regions: {', '.join(subtopic['top_terms']['brain_regions'])}",
            f"Top tasks: {', '.join(subtopic['top_terms']['tasks'])}",
            f"Top keywords: {', '.join(subtopic['top_terms']['keywords'])}",
            "",
            "Anchor papers:",
            "\n\n".join(anchor_blocks),
        ]
    )


def parse_json_text(text: str) -> Dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].strip()
    return json.loads(cleaned)


def run_openai_api(prompt: str, model: str) -> Dict[str, Any]:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    payload = {
        "model": model,
        "input": prompt,
        "text": {"verbosity": "low"},
        "reasoning": {"effort": "low"},
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


def judge_subtopic(subtopic: Dict[str, Any], papers: Dict[str, Dict[str, Any]], model: str) -> OrderedDict[str, Any]:
    result = run_openai_api(build_prompt(subtopic, papers), model)
    return OrderedDict(
        [
            ("subtopic_id", subtopic["subtopic_id"]),
            ("judged_at", datetime.now(timezone.utc).isoformat()),
            ("provider", "openai_api"),
            ("model", model),
            ("prompt_version", PROMPT_VERSION),
            ("refined_label", str(result["refined_label"]).strip()),
            ("page_type", str(result["page_type"]).strip()),
            ("page_worthiness", int(result["page_worthiness"])),
            ("keep", bool(result["keep"])),
            ("summary", str(result["summary"]).strip()),
            ("reason_short", str(result["reason_short"]).strip()),
        ]
    )


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    subtopic_candidates_path = Path(args.subtopic_candidates_path)
    judgments_path = Path(args.judgments_path)
    payload, papers = load_payloads(subtopic_candidates_path)
    existing = load_jsonl(judgments_path)
    requested = set(args.subtopic_id)

    subtopics = payload["subtopics"]
    pending = []
    for subtopic in subtopics:
        if requested and subtopic["subtopic_id"] not in requested:
            continue
        if not args.force and subtopic["subtopic_id"] in existing:
            continue
        pending.append(subtopic)
    if args.max_candidates is not None:
        pending = pending[: args.max_candidates]
    if not pending:
        print("No subtopics require judgment.")
        return 0

    judged = 0
    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
        futures = {
            executor.submit(judge_subtopic, subtopic, papers, args.model): subtopic
            for subtopic in pending
        }
        for future in concurrent.futures.as_completed(futures):
            subtopic = futures[future]
            try:
                record = future.result()
            except Exception as exc:
                failed += 1
                print(f"[{judged + failed}/{len(pending)}] {subtopic['subtopic_id']} error={exc}", file=sys.stderr)
                continue
            append_jsonl(judgments_path, record)
            judged += 1
            print(
                f"[{judged + failed}/{len(pending)}] {subtopic['subtopic_id']} keep={record['keep']} "
                f"type={record['page_type']} worthiness={record['page_worthiness']}"
            )
            sys.stdout.flush()

    print(f"Completed subtopic judgments: {judged} succeeded, {failed} failed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
