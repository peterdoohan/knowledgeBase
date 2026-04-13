#!/usr/bin/env python3
"""Judge active wiki page quality with Anthropic or OpenAI and build a revision queue."""

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

from normalize_summaries import REPO_ROOT, dump_yaml, parse_frontmatter, split_frontmatter, write_yaml


DERIVED_DIR = REPO_ROOT / "derived"
WIKI_DIR = REPO_ROOT / "wiki"
DOTENV_PATH = REPO_ROOT / ".env"
JUDGMENTS_PATH = DERIVED_DIR / "wiki_page_quality_judgments.jsonl"
REPORT_PATH = DERIVED_DIR / "wiki_page_quality_report.yaml"
PROMPT_VERSION = "wiki-page-quality-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("anthropic_api", "openai_api"), default="anthropic_api")
    parser.add_argument("--model", default="claude-opus-4-6")
    parser.add_argument("--subtopic-id", action="append", default=[])
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


def extract_section(body: str, name: str) -> str:
    pattern = rf"(?ms)^## {re.escape(name)}\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, body)
    return match.group(1).strip() if match else ""


def load_active_pages() -> List[Dict[str, Any]]:
    pages: List[Dict[str, Any]] = []
    for page_type, directory in (("topic", WIKI_DIR / "topics"), ("debate", WIKI_DIR / "debates")):
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            frontmatter_block, body = split_frontmatter(path.read_text())
            frontmatter = parse_frontmatter(frontmatter_block)
            if str(frontmatter.get("status", "")).strip() == "deprecated":
                continue
            subtopic_id = str(frontmatter.get("subtopic_id", "")).strip()
            if not subtopic_id:
                continue
            title = str(frontmatter.get("title", "")).strip() or path.stem
            lead = ""
            lines = [line.rstrip() for line in body.splitlines()]
            paragraph: List[str] = []
            saw_title = False
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("# "):
                    saw_title = True
                    continue
                if not saw_title:
                    continue
                if not stripped:
                    if paragraph:
                        break
                    continue
                if stripped.startswith("## "):
                    break
                paragraph.append(stripped)
            lead = " ".join(paragraph).strip()
            pages.append(
                {
                    "subtopic_id": subtopic_id,
                    "page_type": page_type,
                    "title": title,
                    "path": path,
                    "relative_path": str(path.relative_to(REPO_ROOT).with_suffix("")),
                    "lead": lead,
                    "current_view": short(extract_section(body, "Current view"), 1400),
                    "strongest_evidence": short(extract_section(body, "Strongest evidence"), 1400),
                    "boundaries_and_tensions": short(extract_section(body, "Boundaries and tensions"), 1100),
                    "open_questions": short(extract_section(body, "Open questions"), 900),
                    "related_wiki_pages": list(frontmatter.get("related_wiki_pages", []) or []),
                    "anchor_papers": list(frontmatter.get("anchor_papers", []) or []),
                    "core_papers": list(frontmatter.get("core_papers", []) or []),
                }
            )
    return pages


def build_prompt(page: Dict[str, Any]) -> str:
    return "\n".join(
        [
            "You are judging the quality of a neuroscience wiki page in a persistent research knowledge base.",
            "Be critical about page boundaries, evidence density, and whether the lead makes a crisp claim.",
            "Return strict JSON with keys:",
            "subtopic_id, overall_score, lead_clarity_score, evidence_density_score, boundary_clarity_score, navigability_score, redundancy_risk_score, action, rationale_short, revision_notes",
            "Use 1-5 integers for all scores. Higher redundancy_risk means worse.",
            "Set action to one of: keep, revise, consider_merge.",
            "Keep rationale_short under 35 words.",
            "Keep revision_notes under 30 words.",
            "Return JSON only. No markdown fences.",
            "",
            f"subtopic_id: {page['subtopic_id']}",
            f"title: {page['title']}",
            f"page_type: {page['page_type']}",
            f"lead: {page['lead']}",
            f"current_view: {page['current_view']}",
            f"strongest_evidence: {page['strongest_evidence']}",
            f"boundaries_and_tensions: {page['boundaries_and_tensions']}",
            f"open_questions: {page['open_questions']}",
            f"related_wiki_pages: {', '.join(page['related_wiki_pages'])}",
            f"anchor_papers: {', '.join(page['anchor_papers'][:5])}",
            f"core_paper_count: {len(page['core_papers'])}",
            "",
            "Judge whether this page is sharp, well-bounded, and worth keeping as a canonical wiki entry.",
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
        records[record["subtopic_id"]] = record
    return records


def append_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    if not records:
        return
    with path.open("a") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")


def rewrite_jsonl(path: Path, records: Dict[str, Dict[str, Any]]) -> None:
    with path.open("w") as handle:
        for subtopic_id in sorted(records):
            handle.write(json.dumps(records[subtopic_id], sort_keys=True) + "\n")


def judge_one(page: Dict[str, Any], provider: str, model: str) -> Dict[str, Any]:
    if provider == "anthropic_api":
        result = run_anthropic_api(build_prompt(page), model)
    else:
        result = run_openai_api(build_prompt(page), model)
    def as_int(key: str) -> int:
        raw = result.get(key, 0)
        if isinstance(raw, str):
            match = re.search(r"\d+", raw)
            return int(match.group(0)) if match else 0
        return int(raw or 0)
    return {
        "subtopic_id": page["subtopic_id"],
        "overall_score": as_int("overall_score"),
        "lead_clarity_score": as_int("lead_clarity_score"),
        "evidence_density_score": as_int("evidence_density_score"),
        "boundary_clarity_score": as_int("boundary_clarity_score"),
        "navigability_score": as_int("navigability_score"),
        "redundancy_risk_score": as_int("redundancy_risk_score"),
        "action": str(result.get("action", "")).strip(),
        "rationale_short": str(result.get("rationale_short", "")).strip(),
        "revision_notes": str(result.get("revision_notes", "")).strip(),
        "judge_model": model,
        "provider": provider,
        "prompt_version": PROMPT_VERSION,
        "judged_at": datetime.now(timezone.utc).isoformat(),
    }


def build_report(judgments: Dict[str, Dict[str, Any]], pages: List[Dict[str, Any]]) -> OrderedDict:
    entries: List[OrderedDict[str, Any]] = []
    action_counts: Dict[str, int] = {}
    score_counts: Dict[str, int] = {}
    for page in pages:
        judgment = judgments.get(page["subtopic_id"])
        if not judgment:
            continue
        action = judgment["action"] or "unknown"
        action_counts[action] = action_counts.get(action, 0) + 1
        score_counts[str(judgment["overall_score"])] = score_counts.get(str(judgment["overall_score"]), 0) + 1
        entries.append(
            OrderedDict(
                [
                    ("subtopic_id", page["subtopic_id"]),
                    ("title", page["title"]),
                    ("path", page["relative_path"]),
                    ("page_type", page["page_type"]),
                    ("overall_score", judgment["overall_score"]),
                    ("action", action),
                    ("lead_clarity_score", judgment["lead_clarity_score"]),
                    ("evidence_density_score", judgment["evidence_density_score"]),
                    ("boundary_clarity_score", judgment["boundary_clarity_score"]),
                    ("navigability_score", judgment["navigability_score"]),
                    ("redundancy_risk_score", judgment["redundancy_risk_score"]),
                    ("rationale_short", judgment["rationale_short"]),
                    ("revision_notes", judgment["revision_notes"]),
                ]
            )
        )
    entries.sort(
        key=lambda item: (
            item["overall_score"],
            0 if item["action"] == "revise" else 1,
            -item["redundancy_risk_score"],
            item["title"],
        )
    )
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("prompt_version", PROMPT_VERSION),
            ("judged_page_count", len(entries)),
            ("action_counts", OrderedDict(sorted(action_counts.items()))),
            ("overall_score_counts", OrderedDict(sorted(score_counts.items(), key=lambda kv: kv[0]))),
            ("revision_queue", entries),
        ]
    )


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    wanted = set(args.subtopic_id)
    pages = [page for page in load_active_pages() if not wanted or page["subtopic_id"] in wanted]
    existing = load_existing(JUDGMENTS_PATH)
    if args.refresh:
        if wanted:
            for subtopic_id in wanted:
                existing.pop(subtopic_id, None)
        else:
            existing = {}
    pending = [page for page in pages if page["subtopic_id"] not in existing]

    new_records: List[Dict[str, Any]] = []
    failed = 0
    if pending:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
            futures = {
                executor.submit(judge_one, page, args.provider, args.model): page
                for page in pending
            }
            for future in concurrent.futures.as_completed(futures):
                page = futures[future]
                try:
                    record = future.result()
                except Exception as exc:
                    failed += 1
                    print(f"{page['subtopic_id']} error={exc}", file=sys.stderr)
                    continue
                new_records.append(record)
                existing[page["subtopic_id"]] = record
                print(f"{page['subtopic_id']} overall={record['overall_score']} action={record['action']}")
                sys.stdout.flush()

    report = build_report(existing, pages)
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
