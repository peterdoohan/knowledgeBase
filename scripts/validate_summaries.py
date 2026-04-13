#!/usr/bin/env python3
"""Validate normalized summaries and produce a deterministic repair queue."""

from __future__ import annotations

import argparse
import re
from collections import OrderedDict, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from normalize_summaries import (
    REPO_ROOT,
    SECTION_HEADERS,
    SUMMARIES_DIR,
    TITLE_STOPWORDS,
    Summary,
    load_summaries,
    parse_simple_yaml,
    read_alias_map,
    write_yaml,
)


DERIVED_DIR = REPO_ROOT / "derived"
VALIDATION_REPORT_PATH = DERIVED_DIR / "summary_validation_report.yaml"
REPAIR_QUEUE_PATH = DERIVED_DIR / "summary_repair_queue.yaml"
RAW_MDS_DIR = REPO_ROOT / "raw" / "mds"

REQUIRED_SECTIONS = [
    "One-line summary",
    "Methods",
    "Key findings",
    "Prevailing model of the system under study",
    "What this paper contributes",
    "Limitations & open questions",
]

COMMON_TITLE_WORDS = {
    "after",
    "all",
    "between",
    "development",
    "effects",
    "emergence",
    "health",
    "impair",
    "mental",
    "mirror",
    "organized",
    "planning",
    "reversals",
    "right",
    "self",
    "systems",
    "visual",
    "way",
}

SUSPICIOUS_PATTERNS = [
    re.compile(r"inferred\s+—\s+see note", re.IGNORECASE),
    re.compile(r"conversion failure note", re.IGNORECASE),
    re.compile(r"cannot be read", re.IGNORECASE),
    re.compile(r"cannot be determined reliably", re.IGNORECASE),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write validation report and repair queue YAML.")
    return parser.parse_args()


def normalize_title(title: str) -> str:
    cleaned = re.sub(r"\(.*?\)", "", title.lower())
    cleaned = re.sub(r"[^a-z0-9]+", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def text_for_detection(summary: Summary) -> str:
    return "\n".join(
        [
            str(summary.frontmatter.get("title", "")),
            summary.body,
        ]
    ).lower()


def source_quality(path: Path) -> Tuple[str, int]:
    if not path.exists():
        return "missing", 0
    text = path.read_text(errors="replace")
    omitted = text.count("intentionally omitted")
    if omitted >= 20:
        return "poor", omitted
    if omitted >= 5:
        return "mixed", omitted
    return "good", omitted


def looks_truncated(text: str) -> bool:
    cleaned = text.strip()
    if not cleaned:
        return False
    if "…50 tokens truncated…" in cleaned or "tokens truncated" in cleaned:
        return True
    last_line = cleaned.splitlines()[-1].strip()
    if len(last_line) < 12:
        return False
    if re.search(r"[.!?\]”\"]$", last_line):
        return False
    if last_line.endswith(":"):
        return True
    if re.search(r"\b(and|or|but|that|which|with|while|because|than|to|of|for|in|on|through|vs)\s*$", last_line):
        return True
    return False


def suspicious_keywords(summary: Summary) -> List[str]:
    title = normalize_title(str(summary.frontmatter.get("title", "")))
    title_tokens = {token for token in title.split() if len(token) >= 4 and token not in TITLE_STOPWORDS}
    keywords = [str(item).strip() for item in summary.frontmatter.get("keywords", []) or []]
    bad: List[str] = []
    for keyword in keywords:
        norm = normalize_title(keyword)
        if not norm:
            continue
        if norm in COMMON_TITLE_WORDS:
            bad.append(keyword)
            continue
        parts = norm.split()
        if len(parts) == 1 and parts[0] in title_tokens and parts[0] in COMMON_TITLE_WORDS:
            bad.append(keyword)
    return bad


def alias_presence(alias_map: Dict[str, Dict[str, List[str]]], category: str, canonical: str, text: str) -> bool:
    variants = [canonical.replace("_", " ")] + list(alias_map.get(category, {}).get(canonical, []))
    lowered = text.lower()
    return any(re.search(rf"\b{re.escape(variant.lower())}\b", lowered) for variant in variants)


def analyze_summary(
    summary: Summary,
    alias_map: Dict[str, Dict[str, List[str]]],
    duplicate_titles: Dict[str, List[str]],
    quality_lookup: Dict[str, Dict[str, Any]],
) -> OrderedDict:
    paper_id = str(summary.frontmatter.get("paper_id", summary.path.stem))
    title = str(summary.frontmatter.get("title", ""))
    raw_source = RAW_MDS_DIR / f"{paper_id}.md"
    source_status, omitted_count = source_quality(raw_source)
    body_text = text_for_detection(summary)

    issues: List[str] = []
    severity = 0

    if any(pattern.search(summary.body) or pattern.search(title) for pattern in SUSPICIOUS_PATTERNS):
        issues.append("uncertain_identity_or_conversion_failure")
        severity = max(severity, 5)

    duplicate_group = duplicate_titles.get(normalize_title(title), [])
    if len(duplicate_group) > 1:
        issues.append("duplicate_or_near_duplicate_title")
        severity = max(severity, 4)

    missing_sections = [name for name in REQUIRED_SECTIONS if not summary.sections.get(name, "").strip()]
    if missing_sections:
        issues.append("missing_required_sections")
        severity = max(severity, 4)

    truncated_sections = [
        name
        for name in REQUIRED_SECTIONS + ["Connections & keywords", "Brain regions & systems"]
        if looks_truncated(summary.sections.get(name, ""))
    ]
    if truncated_sections:
        issues.append("truncated_sections")
        severity = max(severity, 4)

    polluted_keywords = suspicious_keywords(summary)
    if polluted_keywords:
        issues.append("polluted_keywords")
        severity = max(severity, 3)

    for category in ("brain_regions", "frameworks"):
        values = [str(item) for item in summary.frontmatter.get(category, []) or []]
        suspicious = [value for value in values if not alias_presence(alias_map, category, value, body_text)]
        if suspicious:
            issues.append(f"suspicious_{category}")
            severity = max(severity, 4 if category == "brain_regions" else 3)

    if not list(summary.frontmatter.get("brain_regions", []) or []):
        issues.append("empty_brain_regions")
        severity = max(severity, 3)
    if not list(summary.frontmatter.get("frameworks", []) or []):
        issues.append("empty_frameworks")
        severity = max(severity, 3)
    if not list(summary.frontmatter.get("wiki_pages", []) or []):
        issues.append("empty_wiki_pages")
        severity = max(severity, 2)

    if source_status in {"missing", "poor"}:
        issues.append(f"source_{source_status}")
        severity = max(severity, 5 if source_status == "missing" else 4)

    quality = quality_lookup.get(paper_id, {})
    if quality.get("action") == "revise":
        issues.append("opus_summary_revise")
        severity = max(severity, 4)
    elif quality.get("action") == "light_edit":
        severity = max(severity, 2)

    return OrderedDict(
        [
            ("paper_id", paper_id),
            ("title", title),
            ("issues", sorted(set(issues))),
            ("severity", severity),
            ("source_path", str(raw_source.relative_to(REPO_ROOT)) if raw_source.exists() else ""),
            ("source_quality", source_status),
            ("omitted_image_marker_count", omitted_count),
            ("missing_sections", missing_sections),
            ("truncated_sections", truncated_sections),
            ("polluted_keywords", polluted_keywords[:10]),
            ("duplicate_group", duplicate_group),
            ("opus_action", quality.get("action", "")),
            ("opus_score", int(quality.get("overall_score", 0) or 0)),
        ]
    )


def load_quality_lookup() -> Dict[str, Dict[str, Any]]:
    path = DERIVED_DIR / "summary_quality_report.yaml"
    if not path.exists():
        return {}
    report = parse_simple_yaml(path.read_text())
    lookup: Dict[str, Dict[str, Any]] = {}
    for entry in report.get("review_queue", []):
        lookup[entry["paper_id"]] = entry
    judgments = DERIVED_DIR / "summary_quality_judgments.jsonl"
    if judgments.exists():
        import json

        for line in judgments.read_text().splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            lookup[record["paper_id"]] = record
    return lookup


def build_report(entries: List[OrderedDict]) -> OrderedDict:
    issue_counts: Dict[str, int] = defaultdict(int)
    flagged = 0
    for entry in entries:
        if entry["issues"]:
            flagged += 1
        for issue in entry["issues"]:
            issue_counts[issue] += 1
    repair_queue = [entry for entry in entries if entry["severity"] >= 4]
    repair_queue.sort(key=lambda item: (-item["severity"], item["opus_score"], item["paper_id"]))
    report_entries = [entry for entry in entries if entry["issues"]]
    report_entries.sort(key=lambda item: (-item["severity"], item["paper_id"]))
    return OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("paper_count", len(entries)),
            ("flagged_paper_count", flagged),
            ("issue_counts", OrderedDict(sorted(issue_counts.items()))),
            ("repair_queue_count", len(repair_queue)),
            ("repair_queue", repair_queue),
            ("flagged_entries", report_entries),
        ]
    )


def main() -> int:
    args = parse_args()
    summaries = load_summaries()
    alias_map = read_alias_map(REPO_ROOT / "derived" / "alias_map.yaml")
    quality_lookup = load_quality_lookup()

    duplicate_titles: Dict[str, List[str]] = defaultdict(list)
    for summary in summaries:
        duplicate_titles[normalize_title(str(summary.frontmatter.get("title", "")))].append(
            str(summary.frontmatter.get("paper_id", summary.path.stem))
        )

    entries = [
        analyze_summary(summary, alias_map, duplicate_titles, quality_lookup)
        for summary in summaries
    ]
    report = build_report(entries)
    if args.write:
        write_yaml(VALIDATION_REPORT_PATH, report)
        write_yaml(REPAIR_QUEUE_PATH, OrderedDict([("generated_at", report["generated_at"]), ("entries", report["repair_queue"])]))
        print(
            f"Wrote {VALIDATION_REPORT_PATH.relative_to(REPO_ROOT)} and {REPAIR_QUEUE_PATH.relative_to(REPO_ROOT)}"
        )
    else:
        print("\n".join(str(line) for line in report.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
