#!/usr/bin/env python3
"""Judge raw summary quality with Anthropic or OpenAI and build a review queue."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import REPO_ROOT, Summary, dump_yaml, load_summaries, parse_frontmatter, split_frontmatter, write_yaml


DERIVED_DIR = REPO_ROOT / "derived"
DOTENV_PATH = REPO_ROOT / ".env"
JUDGMENTS_PATH = DERIVED_DIR / "summary_quality_judgments.jsonl"
REPORT_PATH = DERIVED_DIR / "summary_quality_report.yaml"
PROMPT_VERSION = "summary-quality-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("anthropic_api", "openai_api"), default="anthropic_api")
    parser.add_argument("--model", default="claude-opus-4-6")
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--max-workers", type=int, default=8)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--write", action="store_true")
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


def short(text: str, limit: int) -> str:
    cleaned = re.sub(r"\n{2,}", "\n", text.strip())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3].rstrip() + "..."


def build_prompt(summary: Summary) -> str:
    fm = summary.frontmatter
    sections = summary.sections
    return "\n".join(
        [
            "You are judging the quality of a neuroscience paper summary for inclusion in a persistent research wiki.",
            "Be strict. Penalize vagueness, polluted keywords, weak traceability, and generic theoretical claims.",
            "Return strict JSON with keys:",
            "paper_id, overall_score, clarity_score, specificity_score, traceability_score, metadata_quality_score, action, rationale_short, top_issues, suggested_fix",
            "Use 1-5 integers for all scores.",
            "Set action to one of: keep, light_edit, revise.",
            "Keep rationale_short under 35 words.",
            "Return at most 3 top_issues, each under 8 words.",
            "Keep suggested_fix under 20 words.",
            "Return JSON only. No markdown fences.",
            "",
            f"paper_id: {fm.get('paper_id', summary.path.stem)}",
            f"title: {fm.get('title', '')}",
            f"year: {fm.get('year', '')}",
            f"paper_type: {fm.get('paper_type', '')}",
            f"contribution_type: {fm.get('contribution_type', '')}",
            f"one_line_summary: {sections.get('One-line summary', '')}",
            f"methods: {short(sections.get('Methods', ''), 900)}",
            f"key_findings: {short(sections.get('Key findings', ''), 1100)}",
            f"what_this_paper_contributes: {short(sections.get('What this paper contributes', ''), 700)}",
            f"limitations: {short(sections.get('Limitations & open questions', ''), 600)}",
            f"connections_keywords: {short(sections.get('Connections & keywords', ''), 500)}",
            f"brain_regions: {', '.join(fm.get('brain_regions', []) or [])}",
            f"frameworks: {', '.join(fm.get('frameworks', []) or [])}",
            f"wiki_pages: {', '.join(fm.get('wiki_pages', []) or [])}",
            "",
            "Judge whether this summary would be reliable and useful for future synthesis without reopening the paper.",
        ]
    )


def parse_json_text(text: str) -> Dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if not match:
        raise RuntimeError(f"no JSON object in response: {text[:400]}")
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON response: {text[:400]}") from exc


def run_anthropic_api(prompt: str, model: str) -> Dict[str, Any]:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")
    payload = {
        "model": model,
        "max_tokens": 420,
        "temperature": 0,
        "messages": [{"role": "user", "content": prompt}],
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
        with urllib.request.urlopen(request, timeout=180) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"anthropic api error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"anthropic api request failed: {exc}") from exc
    parsed = json.loads(body)
    parts = parsed.get("content", []) or []
    text = "\n".join(part.get("text", "") for part in parts if part.get("type") == "text").strip()
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
        with urllib.request.urlopen(request, timeout=180) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"openai api error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"openai api request failed: {exc}") from exc
    parsed = json.loads(body)
    texts: List[str] = []
    for item in parsed.get("output", []) or []:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text":
                texts.append(content.get("text", ""))
    text = "\n".join(chunk for chunk in texts if chunk).strip()
    if not text:
        raise RuntimeError("openai api returned no text content")
    return parse_json_text(text)


def load_existing(path: Path) -> Dict[str, Dict[str, Any]]:
    records: Dict[str, Dict[str, Any]] = {}
    if not path.exists():
        return records
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        records[record["paper_id"]] = record
    return records


def append_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    if not records:
        return
    with path.open("a") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")


def rewrite_jsonl(path: Path, records: Dict[str, Dict[str, Any]]) -> None:
    with path.open("w") as handle:
        for paper_id in sorted(records):
            handle.write(json.dumps(records[paper_id], sort_keys=True) + "\n")


def judge_one(summary: Summary, provider: str, model: str) -> Dict[str, Any]:
    paper_id = str(summary.frontmatter.get("paper_id", summary.path.stem))
    if provider == "anthropic_api":
        result = run_anthropic_api(build_prompt(summary), model)
    else:
        result = run_openai_api(build_prompt(summary), model)
    def as_int(key: str) -> int:
        raw = result.get(key, 0)
        if isinstance(raw, str):
            match = re.search(r"\d+", raw)
            return int(match.group(0)) if match else 0
        return int(raw or 0)
    top_issues = result.get("top_issues", [])
    if isinstance(top_issues, str):
        top_issues = [top_issues]
    return {
        "paper_id": paper_id,
        "overall_score": as_int("overall_score"),
        "clarity_score": as_int("clarity_score"),
        "specificity_score": as_int("specificity_score"),
        "traceability_score": as_int("traceability_score"),
        "metadata_quality_score": as_int("metadata_quality_score"),
        "action": str(result.get("action", "")).strip(),
        "rationale_short": str(result.get("rationale_short", "")).strip(),
        "top_issues": [str(item).strip() for item in list(top_issues)[:3] if str(item).strip()],
        "suggested_fix": str(result.get("suggested_fix", "")).strip(),
        "judge_model": model,
        "provider": provider,
        "prompt_version": PROMPT_VERSION,
        "judged_at": datetime.now(timezone.utc).isoformat(),
    }


def build_report(judgments: Dict[str, Dict[str, Any]], summaries: List[Summary]) -> OrderedDict:
    entries: List[OrderedDict[str, Any]] = []
    action_counts: Dict[str, int] = {}
    score_counts: Dict[str, int] = {}
    for summary in summaries:
        paper_id = str(summary.frontmatter.get("paper_id", summary.path.stem))
        judgment = judgments.get(paper_id)
        if not judgment:
            continue
        action = judgment["action"] or "unknown"
        action_counts[action] = action_counts.get(action, 0) + 1
        score_counts[str(judgment["overall_score"])] = score_counts.get(str(judgment["overall_score"]), 0) + 1
        entries.append(
            OrderedDict(
                [
                    ("paper_id", paper_id),
                    ("title", str(summary.frontmatter.get("title", ""))),
                    ("overall_score", judgment["overall_score"]),
                    ("action", action),
                    ("clarity_score", judgment["clarity_score"]),
                    ("specificity_score", judgment["specificity_score"]),
                    ("traceability_score", judgment["traceability_score"]),
                    ("metadata_quality_score", judgment["metadata_quality_score"]),
                    ("rationale_short", judgment["rationale_short"]),
                    ("top_issues", judgment["top_issues"]),
                    ("suggested_fix", judgment["suggested_fix"]),
                ]
            )
        )
    entries.sort(
        key=lambda item: (
            item["overall_score"],
            0 if item["action"] == "revise" else 1,
            item["metadata_quality_score"],
            item["paper_id"],
        )
    )
    review_queue = entries[:40]
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("prompt_version", PROMPT_VERSION),
            ("judged_summary_count", len(entries)),
            ("action_counts", OrderedDict(sorted(action_counts.items()))),
            ("overall_score_counts", OrderedDict(sorted(score_counts.items(), key=lambda kv: kv[0]))),
            ("review_queue", review_queue),
        ]
    )


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    wanted = set(args.paper_id)
    summaries = [summary for summary in load_summaries() if not wanted or str(summary.frontmatter.get("paper_id", summary.path.stem)) in wanted]
    existing = load_existing(JUDGMENTS_PATH)
    if args.refresh:
        if wanted:
            for paper_id in wanted:
                existing.pop(paper_id, None)
        else:
            existing = {}
    pending = [summary for summary in summaries if str(summary.frontmatter.get("paper_id", summary.path.stem)) not in existing]

    new_records: List[Dict[str, Any]] = []
    failed = 0
    if pending:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
            futures = {
                executor.submit(judge_one, summary, args.provider, args.model): summary
                for summary in pending
            }
            for future in concurrent.futures.as_completed(futures):
                summary = futures[future]
                paper_id = str(summary.frontmatter.get("paper_id", summary.path.stem))
                try:
                    record = future.result()
                except Exception as exc:
                    failed += 1
                    print(f"{paper_id} error={exc}", file=sys.stderr)
                    continue
                new_records.append(record)
                existing[paper_id] = record
                print(f"{paper_id} overall={record['overall_score']} action={record['action']}")
                sys.stdout.flush()

    report = build_report(existing, summaries)
    if args.write:
        if args.refresh:
            rewrite_jsonl(JUDGMENTS_PATH, existing)
        else:
            append_jsonl(JUDGMENTS_PATH, new_records)
        write_yaml(REPORT_PATH, report)
        print(f"Wrote {REPORT_PATH.relative_to(REPO_ROOT)} and appended {len(new_records)} judgments")
    else:
        print("\n".join(dump_yaml(report)))
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
