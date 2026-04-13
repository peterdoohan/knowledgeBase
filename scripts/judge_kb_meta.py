#!/usr/bin/env python3
"""Get a second-model meta review of the current knowledge-base state."""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import REPO_ROOT, dump_yaml, load_summaries, parse_simple_yaml, write_yaml


DERIVED_DIR = REPO_ROOT / "derived"
WIKI_DIR = REPO_ROOT / "wiki"
DOTENV_PATH = REPO_ROOT / ".env"
OUTPUT_PATH = DERIVED_DIR / "kb_meta_review.yaml"
PROMPT_VERSION = "kb-meta-review-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("anthropic_api", "openai_api"), default="anthropic_api")
    parser.add_argument("--model", default="claude-opus-4-6")
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


def run_anthropic_api(prompt: str, model: str) -> Dict[str, Any]:
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
    with urllib.request.urlopen(request, timeout=180) as response:
        body = response.read().decode("utf-8")
    parsed = json.loads(body)
    text = "\n".join(part.get("text", "") for part in parsed.get("content", []) if part.get("type") == "text").strip()
    return parse_json_text(text)


def run_openai_api(prompt: str, model: str) -> Dict[str, Any]:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    payload = {"model": model, "input": prompt, "text": {"verbosity": "low"}, "reasoning": {"effort": "medium"}}
    request = urllib.request.Request(
        url="https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "content-type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        body = response.read().decode("utf-8")
    parsed = json.loads(body)
    texts: List[str] = []
    for item in parsed.get("output", []) or []:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text":
                texts.append(content.get("text", ""))
    return parse_json_text("\n".join(texts))


def load_stats() -> Dict[str, Any]:
    paper_index = parse_simple_yaml((DERIVED_DIR / "paper_index.yaml").read_text())
    citation_edges = parse_simple_yaml((DERIVED_DIR / "citation_edges.yaml").read_text())
    editorial_audit = parse_simple_yaml((DERIVED_DIR / "wiki_editorial_audit.yaml").read_text())
    page_quality = parse_simple_yaml((DERIVED_DIR / "wiki_page_quality_report.yaml").read_text())
    summary_quality = parse_simple_yaml((DERIVED_DIR / "summary_quality_report.yaml").read_text())
    summaries = load_summaries()
    represented = {
        str(summary.frontmatter.get("paper_id", summary.path.stem))
        for summary in summaries
        if list(summary.frontmatter.get("wiki_pages", []) or [])
    }

    topic_count = len(list((WIKI_DIR / "topics").glob("*.md")))
    debate_count = len(list((WIKI_DIR / "debates").glob("*.md")))
    return {
        "paper_count": len(paper_index.get("papers", [])),
        "citation_edge_count": int(citation_edges.get("edge_count", 0) or 0),
        "coverage_represented_papers": len(represented),
        "coverage_total_papers": len(summaries),
        "topic_page_count_on_disk": topic_count,
        "debate_page_count_on_disk": debate_count,
        "editorial_decision_counts": editorial_audit.get("decision_counts", {}),
        "page_action_counts": page_quality.get("action_counts", {}),
        "summary_action_counts": summary_quality.get("action_counts", {}),
        "page_revision_queue": page_quality.get("revision_queue", [])[:8],
        "summary_review_queue": summary_quality.get("review_queue", [])[:8],
    }


def build_prompt(stats: Dict[str, Any]) -> str:
    return "\n".join(
        [
            "You are performing a meta-level critical review of a neuroscience knowledge-base pipeline and wiki.",
            "Return strict JSON with keys:",
            "overall_status, strongest_assets, weakest_points, highest_priority_actions, cautions",
            "Use short arrays of strings. Be concrete and critical.",
            "Keep each item under 20 words.",
            "Return at most 4 items in each array.",
            "Return JSON only. No markdown fences.",
            "",
            f"paper_count: {stats['paper_count']}",
            f"citation_edge_count: {stats['citation_edge_count']}",
            f"coverage_represented_papers: {stats['coverage_represented_papers']}",
            f"coverage_total_papers: {stats['coverage_total_papers']}",
            f"topic_page_count_on_disk: {stats['topic_page_count_on_disk']}",
            f"debate_page_count_on_disk: {stats['debate_page_count_on_disk']}",
            f"editorial_decision_counts: {json.dumps(stats['editorial_decision_counts'])}",
            f"page_action_counts: {json.dumps(stats['page_action_counts'])}",
            f"summary_action_counts: {json.dumps(stats['summary_action_counts'])}",
            f"page_revision_queue: {json.dumps(stats['page_revision_queue'])}",
            f"summary_review_queue: {json.dumps(stats['summary_review_queue'])}",
            "",
            "Judge the current system as a serious research wiki, not a software demo.",
        ]
    )


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    stats = load_stats()
    if args.provider == "anthropic_api":
        result = run_anthropic_api(build_prompt(stats), args.model)
    else:
        result = run_openai_api(build_prompt(stats), args.model)
    payload = OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("prompt_version", PROMPT_VERSION),
            ("provider", args.provider),
            ("model", args.model),
            ("overall_status", result.get("overall_status", "")),
            ("strongest_assets", result.get("strongest_assets", [])),
            ("weakest_points", result.get("weakest_points", [])),
            ("highest_priority_actions", result.get("highest_priority_actions", [])),
            ("cautions", result.get("cautions", [])),
        ]
    )
    if args.write:
        write_yaml(OUTPUT_PATH, payload)
        print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    else:
        print("\n".join(dump_yaml(payload)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
