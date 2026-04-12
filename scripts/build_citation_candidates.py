#!/usr/bin/env python3
"""Build deterministic in-corpus citation candidates from summaries."""

from __future__ import annotations

import argparse
import hashlib
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from normalize_summaries import (
    DERIVED_DIR,
    Summary,
    extract_citation_block,
    filter_summaries,
    first_author_surname,
    load_summaries,
    normalize_text,
    paper_id_from_path,
    split_authors,
    write_yaml,
)


CITATION_CANDIDATES_PATH = DERIVED_DIR / "citation_candidates.yaml"
BODY_CITATION_SECTIONS = (
    "Background & motivation",
    "Computational framework",
    "Prevailing model of the system under study",
    "What this paper contributes",
)

CITATION_PATTERNS = [
    r"([A-Z][A-Za-z'’\-]+)(?:\s+et al\.)?\s*\((\d{4})\)",
    r"([A-Z][A-Za-z'’\-]+)\s+and\s+[A-Z][A-Za-z'’\-]+\s*\((\d{4})\)",
    r"([A-Z][A-Za-z'’\-]+)\s+et al\.,?\s*(\d{4})",
    r"([A-Z][A-Za-z'’\-]+)\s*&\s+[A-Z][A-Za-z'’\-]+\s*\((\d{4})\)",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--paper-id",
        action="append",
        default=[],
        help="Restrict candidate generation to one or more source paper IDs.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write derived/citation_candidates.yaml.",
    )
    return parser.parse_args()


def build_citation_lookup_lists(summaries: List[Summary]) -> Dict[Tuple[str, int], List[str]]:
    lookup: Dict[Tuple[str, int], List[str]] = {}
    for summary in summaries:
        paper_id = paper_id_from_path(summary.path)
        year = summary.frontmatter.get("year")
        if not isinstance(year, int):
            continue
        surnames = {first_author_surname(summary.frontmatter.get("authors", ""), paper_id)}
        parts = paper_id.split("_")
        if parts:
            surnames.add(normalize_text(parts[0]))
        for surname in sorted(surnames):
            if not surname:
                continue
            lookup.setdefault((surname, year), [])
            if paper_id not in lookup[(surname, year)]:
                lookup[(surname, year)].append(paper_id)
    return lookup


def extract_citation_records(text: str) -> List[Tuple[str, str, int]]:
    seen = set()
    records: List[Tuple[str, str, int]] = []
    for pattern in CITATION_PATTERNS:
        for match in re.finditer(pattern, text):
            raw_mention = match.group(0).strip()
            surname = normalize_text(match.group(1))
            year = int(match.group(2))
            key = (raw_mention, surname, year)
            if key in seen:
                continue
            seen.add(key)
            records.append(key)
    return records


def mention_excerpt(text: str, mention_text: str) -> str:
    idx = text.find(mention_text)
    if idx == -1:
        return text.strip()
    start = idx
    while start > 0 and text[start - 1] not in ".!?\n":
        start -= 1
    end = idx + len(mention_text)
    while end < len(text) and text[end] not in ".!?\n":
        end += 1
    excerpt = text[start:end].strip(" -\n\t")
    return excerpt if excerpt else text.strip()


def candidate_id_for(
    source: str,
    section: str,
    mention_text: str,
    evidence_excerpt: str,
    candidate_targets: Iterable[str],
) -> str:
    payload = "|".join(
        [
            source,
            section,
            normalize_text(mention_text),
            normalize_text(evidence_excerpt),
            ",".join(sorted(candidate_targets)),
        ]
    )
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:12]
    return f"{source}__{digest}"


def deterministic_confidence(extraction_method: str, target_count: int) -> str:
    if extraction_method == "structured_key_citations" and target_count == 1:
        return "high"
    if target_count == 1:
        return "medium"
    return "low"


def build_candidate(
    source: str,
    section: str,
    mention_text: str,
    evidence_excerpt: str,
    extraction_method: str,
    candidate_targets: List[str],
) -> OrderedDict[str, Any]:
    targets = sorted(candidate_targets)
    return OrderedDict(
        [
            ("candidate_id", candidate_id_for(source, section, mention_text, evidence_excerpt, targets)),
            ("source", source),
            ("section", section),
            ("mention_text", mention_text),
            ("evidence_excerpt", evidence_excerpt),
            ("extraction_method", extraction_method),
            ("candidate_targets", targets),
            ("deterministic_confidence", deterministic_confidence(extraction_method, len(targets))),
        ]
    )


def collect_structured_candidates(
    summary: Summary,
    citation_lookup: Dict[Tuple[str, int], List[str]],
) -> List[OrderedDict[str, Any]]:
    paper_id = paper_id_from_path(summary.path)
    block = extract_citation_block(summary)
    if not block:
        return []
    candidates: List[OrderedDict[str, Any]] = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        records = extract_citation_records(line)
        if not records:
            continue
        for raw_mention, surname, year in records:
            targets = [target for target in citation_lookup.get((surname, year), []) if target != paper_id]
            if not targets:
                continue
            candidates.append(
                build_candidate(
                    source=paper_id,
                    section="Connections & keywords",
                    mention_text=raw_mention,
                    evidence_excerpt=line,
                    extraction_method="structured_key_citations",
                    candidate_targets=targets,
                )
            )
    return candidates


def collect_body_candidates(
    summary: Summary,
    citation_lookup: Dict[Tuple[str, int], List[str]],
) -> List[OrderedDict[str, Any]]:
    paper_id = paper_id_from_path(summary.path)
    candidates: List[OrderedDict[str, Any]] = []
    for section in BODY_CITATION_SECTIONS:
        text = summary.sections.get(section, "")
        if not text:
            continue
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            records = extract_citation_records(line)
            if not records:
                continue
            for raw_mention, surname, year in records:
                targets = [target for target in citation_lookup.get((surname, year), []) if target != paper_id]
                if not targets:
                    continue
                candidates.append(
                    build_candidate(
                        source=paper_id,
                        section=section,
                        mention_text=raw_mention,
                        evidence_excerpt=mention_excerpt(line, raw_mention),
                        extraction_method="body_author_year",
                        candidate_targets=targets,
                    )
                )
    return candidates


def dedupe_candidates(candidates: List[OrderedDict[str, Any]]) -> List[OrderedDict[str, Any]]:
    deduped: Dict[str, OrderedDict[str, Any]] = OrderedDict()
    for candidate in candidates:
        deduped.setdefault(candidate["candidate_id"], candidate)
    return list(deduped.values())


def build_payload(summaries: List[Summary]) -> OrderedDict[str, Any]:
    citation_lookup = build_citation_lookup_lists(load_summaries())
    candidates: List[OrderedDict[str, Any]] = []
    for summary in summaries:
        candidates.extend(collect_structured_candidates(summary, citation_lookup))
        candidates.extend(collect_body_candidates(summary, citation_lookup))
    candidates = dedupe_candidates(candidates)
    auto_accept_count = sum(
        1
        for candidate in candidates
        if candidate["deterministic_confidence"] == "high" and len(candidate["candidate_targets"]) == 1
    )
    payload = OrderedDict(
        [
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("candidate_count", len(candidates)),
            ("auto_accept_count", auto_accept_count),
            ("judge_queue_count", len(candidates) - auto_accept_count),
            ("candidates", candidates),
        ]
    )
    return payload


def main() -> int:
    args = parse_args()
    all_summaries = load_summaries()
    summaries = filter_summaries(all_summaries, args.paper_id)
    if not summaries:
        raise SystemExit("No summaries found.")

    payload = build_payload(summaries)
    if args.write:
        write_yaml(CITATION_CANDIDATES_PATH, payload)

    print(
        f"Built {payload['candidate_count']} citation candidates "
        f"({payload['auto_accept_count']} auto-accept, {payload['judge_queue_count']} judge queue)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
