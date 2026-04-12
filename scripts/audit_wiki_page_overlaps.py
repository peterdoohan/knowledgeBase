#!/usr/bin/env python3
"""Audit active wiki-page overlap and judge whether pairs should merge or crosslink."""

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
from typing import Any, Dict, List, Tuple

from normalize_summaries import REPO_ROOT, dump_yaml, parse_frontmatter, parse_simple_yaml, split_frontmatter, write_yaml


DERIVED_DIR = REPO_ROOT / "derived"
WIKI_DIR = REPO_ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
DEBATES_DIR = WIKI_DIR / "debates"
DOTENV_PATH = REPO_ROOT / ".env"
PROMPT_VERSION = "wiki-overlap-audit-v1"
JUDGMENTS_PATH = DERIVED_DIR / "wiki_editorial_judgments.jsonl"
AUDIT_PATH = DERIVED_DIR / "wiki_editorial_audit.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("openai_api",), default="openai_api")
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--max-workers", type=int, default=8)
    parser.add_argument("--write", action="store_true", help="Write judgments and audit YAML.")
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


def load_active_pages() -> Dict[str, Dict[str, Any]]:
    pages: Dict[str, Dict[str, Any]] = {}
    for page_type, directory in (("topic", TOPICS_DIR), ("debate", DEBATES_DIR)):
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
            lead = extract_lead(body)
            pages[subtopic_id] = {
                "subtopic_id": subtopic_id,
                "parent_topic_id": str(frontmatter.get("parent_topic_id", "")).strip(),
                "page_type": page_type,
                "title": title,
                "path": path,
                "relative_path": str(path.relative_to(REPO_ROOT).with_suffix("")),
                "lead": lead,
                "anchor_papers": list(frontmatter.get("anchor_papers", []) or []),
                "core_papers": list(frontmatter.get("core_papers", []) or []),
            }
    return pages


def extract_lead(body: str) -> str:
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
    return " ".join(paragraph).strip()


def load_selected_subtopics() -> Dict[str, Dict[str, Any]]:
    subtopics: Dict[str, Dict[str, Any]] = {}
    for catalog_path in sorted(DERIVED_DIR.glob("*subtopic_catalog.yaml")):
        catalog = parse_simple_yaml(catalog_path.read_text())
        for subtopic in catalog.get("selected_subtopics", []):
            if subtopic.get("keep"):
                subtopics[subtopic["subtopic_id"]] = subtopic
    return subtopics


def build_candidates(
    pages: Dict[str, Dict[str, Any]],
    subtopics: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    ids = sorted(set(pages) & set(subtopics))
    candidates: List[Dict[str, Any]] = []
    for index, left_id in enumerate(ids):
        left = pages[left_id]
        left_subtopic = subtopics[left_id]
        left_papers = set(left_subtopic.get("candidate_papers", []) or [])
        for right_id in ids[index + 1 :]:
            right = pages[right_id]
            right_subtopic = subtopics[right_id]
            right_papers = set(right_subtopic.get("candidate_papers", []) or [])
            intersection = left_papers & right_papers
            if not intersection:
                continue
            union = left_papers | right_papers
            jaccard = len(intersection) / len(union)
            same_parent = left["parent_topic_id"] and left["parent_topic_id"] == right["parent_topic_id"]
            if not (same_parent or len(intersection) >= 6 or jaccard >= 0.12):
                continue
            pair_id = f"{left_id}__{right_id}"
            candidates.append(
                {
                    "pair_id": pair_id,
                    "page_a": left,
                    "page_b": right,
                    "subtopic_a": left_subtopic,
                    "subtopic_b": right_subtopic,
                    "overlap_count": len(intersection),
                    "jaccard": round(jaccard, 3),
                    "shared_papers": sorted(intersection),
                    "same_parent_topic": same_parent,
                }
            )
    candidates.sort(
        key=lambda item: (
            int(item["same_parent_topic"]),
            item["jaccard"],
            item["overlap_count"],
            item["page_a"]["title"],
            item["page_b"]["title"],
        ),
        reverse=True,
    )
    return candidates


def build_prompt(candidate: Dict[str, Any]) -> str:
    page_a = candidate["page_a"]
    page_b = candidate["page_b"]
    subtopic_a = candidate["subtopic_a"]
    subtopic_b = candidate["subtopic_b"]
    return "\n".join(
        [
            "You are auditing overlap between two neuroscience wiki pages in a research knowledge base.",
            "Your job is editorial, not generative.",
            "Choose exactly one decision:",
            "- keep_distinct",
            "- keep_distinct_with_crosslink",
            "- consider_merge",
            "- bridge_page_candidate",
            "",
            "Use keep_distinct if the pages are clearly separate and only modestly adjacent.",
            "Use keep_distinct_with_crosslink if the pages should stay separate but readers need an explicit bridge.",
            "Use consider_merge only if the current distinction is too weak to justify both pages as canonical entries.",
            "Use bridge_page_candidate if both pages are valid but a missing bridge/systems page is causing overlap pressure.",
            "",
            "Return strict JSON with keys:",
            'decision, confidence, rationale_short, page_a_focus, page_b_focus, crosslink_angle',
            "",
            f"Page A title: {page_a['title']}",
            f"Page A parent topic: {page_a['parent_topic_id']}",
            f"Page A type: {page_a['page_type']}",
            f"Page A lead: {page_a['lead']}",
            f"Page A judge summary: {subtopic_a.get('judge_summary', '')}",
            f"Page A anchor papers: {', '.join(subtopic_a.get('anchor_papers', [])[:5])}",
            "",
            f"Page B title: {page_b['title']}",
            f"Page B parent topic: {page_b['parent_topic_id']}",
            f"Page B type: {page_b['page_type']}",
            f"Page B lead: {page_b['lead']}",
            f"Page B judge summary: {subtopic_b.get('judge_summary', '')}",
            f"Page B anchor papers: {', '.join(subtopic_b.get('anchor_papers', [])[:5])}",
            "",
            f"Shared paper count: {candidate['overlap_count']}",
            f"Jaccard overlap: {candidate['jaccard']}",
            f"Same parent topic: {str(candidate['same_parent_topic']).lower()}",
            f"Shared papers: {', '.join(candidate['shared_papers'][:12])}",
            "",
            "Be conservative about merge decisions. Conceptual adjacency is not enough to merge.",
        ]
    )


def run_openai_api(prompt: str, model: str) -> Dict[str, Any]:
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
        with urllib.request.urlopen(request, timeout=180) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"openai api error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"openai api request failed: {exc}") from exc
    parsed = json.loads(body)
    text_chunks: List[str] = []
    for item in parsed.get("output", []) or []:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text":
                text_chunks.append(content.get("text", ""))
    response_text = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    if not response_text:
        raise RuntimeError("openai api returned no text content")
    json_match = re.search(r"\{.*\}", response_text, flags=re.DOTALL)
    if not json_match:
        raise RuntimeError(f"no JSON object in response: {response_text[:400]}")
    try:
        return json.loads(json_match.group(0))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON response: {response_text[:400]}") from exc


def load_existing_judgments(path: Path) -> Dict[str, Dict[str, Any]]:
    judgments: Dict[str, Dict[str, Any]] = {}
    if not path.exists():
        return judgments
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        judgments[record["pair_id"]] = record
    return judgments


def append_judgments(path: Path, records: List[Dict[str, Any]]) -> None:
    if not records:
        return
    with path.open("a") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")


def judge_candidate(candidate: Dict[str, Any], model: str) -> Dict[str, Any]:
    result = run_openai_api(build_prompt(candidate), model)
    confidence = result.get("confidence", 0)
    if isinstance(confidence, str):
        match = re.search(r"\d+", confidence)
        confidence_value = int(match.group(0)) if match else 0
    else:
        confidence_value = int(confidence or 0)
    if confidence_value <= 0 and str(result.get("decision", "")).strip():
        confidence_value = 3
    return {
        "pair_id": candidate["pair_id"],
        "decision": str(result.get("decision", "")).strip(),
        "confidence": confidence_value,
        "rationale_short": str(result.get("rationale_short", "")).strip(),
        "page_a_focus": str(result.get("page_a_focus", "")).strip(),
        "page_b_focus": str(result.get("page_b_focus", "")).strip(),
        "crosslink_angle": str(result.get("crosslink_angle", "")).strip(),
        "judge_model": model,
        "prompt_version": PROMPT_VERSION,
        "judged_at": datetime.now(timezone.utc).isoformat(),
    }


def finalize_audit(
    candidates: List[Dict[str, Any]],
    judgments: Dict[str, Dict[str, Any]],
) -> OrderedDict:
    decision_counts: Dict[str, int] = {}
    entries: List[OrderedDict[str, Any]] = []
    for candidate in candidates:
        judgment = judgments.get(candidate["pair_id"])
        if not judgment:
            continue
        decision = judgment["decision"]
        confidence = int(judgment.get("confidence", 0) or 0)
        if confidence <= 0 and decision:
            confidence = 3
        decision_counts[decision] = decision_counts.get(decision, 0) + 1
        entry = OrderedDict(
            [
                ("pair_id", candidate["pair_id"]),
                ("decision", decision),
                ("confidence", confidence),
                ("overlap_count", candidate["overlap_count"]),
                ("jaccard", candidate["jaccard"]),
                ("same_parent_topic", candidate["same_parent_topic"]),
                (
                    "page_a",
                    OrderedDict(
                        [
                            ("subtopic_id", candidate["page_a"]["subtopic_id"]),
                            ("title", candidate["page_a"]["title"]),
                            ("path", candidate["page_a"]["relative_path"]),
                            ("focus", judgment["page_a_focus"]),
                        ]
                    ),
                ),
                (
                    "page_b",
                    OrderedDict(
                        [
                            ("subtopic_id", candidate["page_b"]["subtopic_id"]),
                            ("title", candidate["page_b"]["title"]),
                            ("path", candidate["page_b"]["relative_path"]),
                            ("focus", judgment["page_b_focus"]),
                        ]
                    ),
                ),
                ("crosslink_angle", judgment["crosslink_angle"]),
                ("rationale_short", judgment["rationale_short"]),
                ("shared_papers", candidate["shared_papers"][:15]),
            ]
        )
        entries.append(entry)
    entries.sort(
        key=lambda item: (
            item["decision"],
            -item["confidence"],
            -item["overlap_count"],
            item["page_a"]["title"],
            item["page_b"]["title"],
        )
    )
    payload = OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("prompt_version", PROMPT_VERSION),
            ("candidate_pair_count", len(candidates)),
            ("judged_pair_count", len(entries)),
            ("decision_counts", OrderedDict(sorted(decision_counts.items()))),
            ("entries", entries),
        ]
    )
    return payload


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    pages = load_active_pages()
    subtopics = load_selected_subtopics()
    candidates = build_candidates(pages, subtopics)
    existing = load_existing_judgments(JUDGMENTS_PATH)
    pending = [candidate for candidate in candidates if candidate["pair_id"] not in existing]

    new_records: List[Dict[str, Any]] = []
    failed = 0
    if pending:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
            futures = {
                executor.submit(judge_candidate, candidate, args.model): candidate
                for candidate in pending
            }
            for future in concurrent.futures.as_completed(futures):
                candidate = futures[future]
                try:
                    record = future.result()
                except Exception as exc:
                    failed += 1
                    print(f"{candidate['pair_id']} error={exc}", file=sys.stderr)
                    continue
                new_records.append(record)
                existing[record["pair_id"]] = record
                print(
                    f"{record['pair_id']} decision={record['decision']} "
                    f"confidence={record['confidence']}"
                )
                sys.stdout.flush()

    audit = finalize_audit(candidates, existing)
    if args.write:
        append_judgments(JUDGMENTS_PATH, new_records)
        write_yaml(AUDIT_PATH, audit)
        print(
            f"Wrote {AUDIT_PATH.relative_to(REPO_ROOT)} "
            f"and appended {len(new_records)} judgments to {JUDGMENTS_PATH.relative_to(REPO_ROOT)}"
        )
    else:
        print("\n".join(dump_yaml(audit)))

    if failed:
        print(f"Audit completed with {failed} failures.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
