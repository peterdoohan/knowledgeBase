#!/usr/bin/env python3
"""Repair high-risk summaries using a proposal model plus an optional judge model."""

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

from normalize_summaries import REPO_ROOT, Summary, dump_frontmatter, load_summaries, parse_simple_yaml, split_frontmatter, write_yaml


DERIVED_DIR = REPO_ROOT / "derived"
RAW_MDS_DIR = REPO_ROOT / "raw" / "mds"
DOTENV_PATH = REPO_ROOT / ".env"
VALIDATION_PATH = DERIVED_DIR / "summary_repair_queue.yaml"
REPAIR_LOG_PATH = DERIVED_DIR / "summary_repair_judgments.jsonl"
REPAIR_REPORT_PATH = DERIVED_DIR / "summary_repair_report.yaml"
PROMPT_VERSION = "summary-repair-v1"

TARGET_SECTIONS = [
    "One-line summary",
    "Methods",
    "Prevailing model of the system under study",
    "What this paper contributes",
    "Limitations & open questions",
    "Brain regions & systems",
    "Connections & keywords",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("anthropic_api", "openai_api"), default="anthropic_api")
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--fallback-provider", choices=("anthropic_api", "openai_api"), default="openai_api")
    parser.add_argument("--fallback-model", default="gpt-5.4")
    parser.add_argument("--judge-provider", choices=("anthropic_api", "openai_api"), default="openai_api")
    parser.add_argument("--judge-model", default="gpt-5.4")
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--max-workers", type=int, default=6)
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


def parse_json_text(text: str) -> Dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if not match:
        raise RuntimeError(f"no JSON object in response: {text[:400]}")
    return json.loads(match.group(0))


def run_api(provider: str, model: str, prompt: str) -> Dict[str, Any]:
    if provider == "anthropic_api":
        api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        payload = {
            "model": model,
            "max_tokens": 900,
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
    else:
        api_key = os.environ.get("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        payload = {
            "model": model,
            "input": prompt,
            "text": {"verbosity": "low"},
            "reasoning": {"effort": "medium"},
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
        with urllib.request.urlopen(request, timeout=240) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{provider} error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"{provider} request failed: {exc}") from exc

    parsed = json.loads(body)
    if provider == "anthropic_api":
        text = "\n".join(part.get("text", "") for part in parsed.get("content", []) if part.get("type") == "text").strip()
    else:
        chunks: List[str] = []
        for item in parsed.get("output", []) or []:
            if item.get("type") != "message":
                continue
            for content in item.get("content", []) or []:
                if content.get("type") == "output_text":
                    chunks.append(content.get("text", ""))
        text = "\n".join(chunks).strip()
    if not text:
        raise RuntimeError(f"{provider} returned no text content")
    return parse_json_text(text)


def select_targets(queue: List[Dict[str, Any]], paper_ids: List[str], limit: int) -> List[Dict[str, Any]]:
    if paper_ids:
        wanted = set(paper_ids)
        return [entry for entry in queue if entry["paper_id"] in wanted]
    filtered = [entry for entry in queue if entry.get("source_quality") not in {"missing", "poor"}]
    return filtered[:limit]


def summaries_by_id() -> Dict[str, Summary]:
    return {str(summary.frontmatter.get("paper_id", summary.path.stem)): summary for summary in load_summaries()}


def source_excerpt(path: Path, limit: int = 22000) -> str:
    text = path.read_text(errors="replace")
    if len(text) <= limit:
        return text
    head = text[:16000]
    tail = text[-5000:]
    return head + "\n\n[...source omitted for length...]\n\n" + tail


def build_proposal_prompt(entry: Dict[str, Any], summary: Summary, source_text: str) -> str:
    sections = summary.sections
    frontmatter = summary.frontmatter
    return "\n".join(
        [
            "You are repairing a neuroscience paper summary used in a persistent research wiki.",
            "Be conservative. Prefer deleting wrong metadata over inventing uncertain metadata.",
            "If the source is too damaged to support repair, return decision=quarantine.",
            "Return strict JSON with keys:",
            "paper_id, decision, rationale_short, frontmatter, section_updates",
            "decision must be one of: repair, quarantine, keep",
            "frontmatter must be a minimal patch and may include only keys you are changing.",
            "Allowed frontmatter keys: title, authors, year, journal, paper_type, contribution_type, species, tasks, methods, brain_regions, frameworks, keywords",
            "If a field is uncertain, omit it from frontmatter rather than guessing.",
            "section_updates may include only: One-line summary, Methods, Prevailing model of the system under study, What this paper contributes, Limitations & open questions, Brain regions & systems, Connections & keywords",
            "Only include a section in section_updates if it is clearly wrong, truncated, or materially misleading in the current summary.",
            "Return JSON only. No markdown fences.",
            "",
            f"paper_id: {entry['paper_id']}",
            f"validator_issues: {', '.join(entry.get('issues', []))}",
            f"existing_title: {frontmatter.get('title', '')}",
            f"existing_frontmatter: {json.dumps({k: frontmatter.get(k) for k in ['authors','year','journal','paper_type','contribution_type','species','tasks','methods','brain_regions','frameworks','keywords']}, ensure_ascii=False)}",
            f"existing_one_line_summary: {sections.get('One-line summary', '')}",
            f"existing_methods: {sections.get('Methods', '')}",
            f"existing_prevailing_model: {sections.get('Prevailing model of the system under study', '')}",
            f"existing_contribution: {sections.get('What this paper contributes', '')}",
            f"existing_limitations: {sections.get('Limitations & open questions', '')}",
            f"existing_brain_regions_section: {sections.get('Brain regions & systems', '')}",
            f"existing_connections: {sections.get('Connections & keywords', '')}",
            "",
            "Source markdown excerpt:",
            source_text,
        ]
    )


def build_judge_prompt(entry: Dict[str, Any], proposal: Dict[str, Any], summary: Summary) -> str:
    return "\n".join(
        [
            "You are judging whether a proposed summary repair is safe and useful.",
            "Return strict JSON with keys: accept, confidence, rationale_short",
            "accept must be yes or no. Use confidence 1-5.",
            "Return JSON only. No markdown fences.",
            "",
            f"paper_id: {entry['paper_id']}",
            f"validator_issues: {', '.join(entry.get('issues', []))}",
            f"existing_title: {summary.frontmatter.get('title', '')}",
            f"existing_brain_regions: {', '.join(summary.frontmatter.get('brain_regions', []) or [])}",
            f"existing_frameworks: {', '.join(summary.frontmatter.get('frameworks', []) or [])}",
            f"proposal_decision: {proposal.get('decision', '')}",
            f"proposal_frontmatter: {json.dumps(proposal.get('frontmatter', {}), ensure_ascii=False)}",
            f"proposal_sections: {json.dumps(proposal.get('section_updates', {}), ensure_ascii=False)}",
            "Approve only if the proposal removes obvious errors and does not invent unsupported claims.",
        ]
    )


def replace_or_append_section(body: str, section_name: str, replacement: str) -> str:
    marker = f"### {section_name}"
    section_text = f"{marker}\n{replacement.strip()}\n"
    if marker in body:
        start = body.index(marker)
        remainder = body[start:]
        next_header = remainder.find("\n### ", len(marker))
        end = start + next_header + 1 if next_header != -1 else len(body)
        new_body = body[:start].rstrip() + "\n\n" + section_text.strip() + "\n"
        if end < len(body):
            new_body += "\n" + body[end:].lstrip("\n")
        return new_body
    return body.rstrip() + "\n\n" + section_text


def apply_repair(summary: Summary, proposal: Dict[str, Any]) -> str:
    updated = OrderedDict(summary.frontmatter)
    frontmatter = proposal.get("frontmatter", {})
    for key, value in frontmatter.items():
        if key == "authors":
            updated[key] = list(value or [])
        elif isinstance(value, list):
            updated[key] = [item for item in value if item]
        elif value not in (None, ""):
            updated[key] = value
        else:
            updated.pop(key, None)
    if proposal.get("decision") == "quarantine":
        updated["ingest_status"] = "needs_source_verification"
        updated["wiki_pages"] = []
    body = summary.body.rstrip() + "\n"
    for section_name, replacement in (proposal.get("section_updates", {}) or {}).items():
        if section_name in TARGET_SECTIONS and replacement:
            body = replace_or_append_section(body, section_name, str(replacement))
    return dump_frontmatter(updated) + body.lstrip("\n")


def load_existing_log() -> List[Dict[str, Any]]:
    if not REPAIR_LOG_PATH.exists():
        return []
    return [json.loads(line) for line in REPAIR_LOG_PATH.read_text().splitlines() if line.strip()]


def append_log(records: List[Dict[str, Any]]) -> None:
    if not records:
        return
    with REPAIR_LOG_PATH.open("a") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")


def build_report(records: List[Dict[str, Any]]) -> OrderedDict:
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("prompt_version", PROMPT_VERSION),
            ("record_count", len(records)),
            ("records", records),
        ]
    )


def repair_one(entry: Dict[str, Any], summary: Summary, args: argparse.Namespace) -> Dict[str, Any]:
    source_path = RAW_MDS_DIR / f"{entry['paper_id']}.md"
    prompt = build_proposal_prompt(entry, summary, source_excerpt(source_path))
    proposal_provider = args.provider
    proposal_model = args.model
    try:
        proposal = run_api(proposal_provider, proposal_model, prompt)
    except Exception:
        proposal_provider = args.fallback_provider
        proposal_model = args.fallback_model
        proposal = run_api(proposal_provider, proposal_model, prompt)
    judge = run_api(args.judge_provider, args.judge_model, build_judge_prompt(entry, proposal, summary))
    accept = str(judge.get("accept", "")).strip().lower() == "yes"
    if str(proposal.get("decision", "")).strip() == "keep":
        accept = True
    return {
        "paper_id": entry["paper_id"],
        "proposal_provider": proposal_provider,
        "proposal_model": proposal_model,
        "proposal_decision": proposal.get("decision", ""),
        "judge_accept": accept,
        "judge_confidence": int(re.search(r"\d+", str(judge.get("confidence", 0))).group(0)) if re.search(r"\d+", str(judge.get("confidence", 0))) else 0,
        "proposal": proposal,
        "judge_rationale_short": str(judge.get("rationale_short", "")).strip(),
        "repaired_at": datetime.now(timezone.utc).isoformat(),
    }


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    queue = parse_simple_yaml(VALIDATION_PATH.read_text()).get("entries", [])
    selected = select_targets(queue, args.paper_id, args.limit)
    summaries = summaries_by_id()
    records: List[Dict[str, Any]] = []
    failures = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
        futures = {
            executor.submit(repair_one, entry, summaries[entry["paper_id"]], args): entry
            for entry in selected
            if entry["paper_id"] in summaries
        }
        for future in concurrent.futures.as_completed(futures):
            entry = futures[future]
            try:
                record = future.result()
            except Exception as exc:
                failures += 1
                print(f"{entry['paper_id']} error={exc}", file=sys.stderr)
                continue
            records.append(record)
            print(
                f"{record['paper_id']} proposal={record['proposal_decision']} "
                f"accepted={record['judge_accept']}"
            )
            sys.stdout.flush()

    if args.write:
        applied = 0
        for record in records:
            paper_id = record["paper_id"]
            proposal = record["proposal"]
            if not record["judge_accept"]:
                continue
            if str(proposal.get("decision", "")).strip() not in {"repair", "quarantine", "keep"}:
                continue
            summary = summaries[paper_id]
            new_text = apply_repair(summary, proposal)
            if summary.path.read_text() != new_text:
                summary.path.write_text(new_text)
                applied += 1
        append_log(records)
        write_yaml(REPAIR_REPORT_PATH, build_report(records))
        print(
            f"Wrote {REPAIR_REPORT_PATH.relative_to(REPO_ROOT)}, "
            f"logged {len(records)} repairs, applied {applied}"
        )
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
