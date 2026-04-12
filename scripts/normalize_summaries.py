#!/usr/bin/env python3
"""Normalize summary frontmatter and build a compact paper index.

This is a first-pass local implementation that uses:
- deterministic parsing for frontmatter and sections
- alias-map phrase matching for canonical fields
- author-year matching for in-corpus citation edges

It is intentionally stdlib-only so it runs in the current repo environment.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
import unicodedata
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
SUMMARIES_DIR = REPO_ROOT / "raw" / "summaries"
DERIVED_DIR = REPO_ROOT / "derived"
ALIAS_MAP_PATH = DERIVED_DIR / "alias_map.yaml"
PAPER_INDEX_PATH = DERIVED_DIR / "paper_index.yaml"

SECTION_HEADERS = [
    "One-line summary",
    "Background & motivation",
    "Methods",
    "Key findings",
    "Computational framework",
    "Prevailing model of the system under study",
    "What this paper contributes",
    "Brain regions & systems",
    "Mechanistic insight",
    "Limitations & open questions",
    "Connections & keywords",
]

FRONTMATTER_ORDER = [
    "source_file",
    "paper_id",
    "title",
    "authors",
    "year",
    "journal",
    "paper_type",
    "contribution_type",
    "species",
    "tasks",
    "methods",
    "brain_regions",
    "frameworks",
    "keywords",
    "key_citations",
]

TITLE_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "using",
    "with",
}

SUBSECTION_LABELS = [
    "Key citations",
    "Named models or frameworks",
    "Brain regions",
    "Keywords",
]


def subsection_header_pattern(label: str) -> str:
    # Support "**Label**", "**Label**:", and "**Label:**" styles.
    escaped = re.escape(label)
    return rf"(?:\*\*{escaped}\*\*:|\*\*{escaped}:\*\*|\*\*{escaped}\*\*)"


def subsection_match(label: str, text: str) -> Optional[re.Match[str]]:
    pattern = rf"(?m)^(?:- )?{subsection_header_pattern(label)}\s*(.*)$"
    return re.search(pattern, text)


def has_structured_subsections(text: str) -> bool:
    pattern = "|".join(subsection_header_pattern(label) for label in SUBSECTION_LABELS)
    return bool(re.search(rf"(?m)^(?:- )?(?:{pattern})\s*", text))


def extract_structured_subsection(text: str, label: str) -> str:
    match = subsection_match(label, text)
    if not match:
        return ""
    block = text[match.start() :]
    header_pattern = rf"(?m)^(?:- )?{subsection_header_pattern(label)}\s*"
    block = re.sub(header_pattern, "", block, count=1)
    stop_labels = [candidate for candidate in SUBSECTION_LABELS if candidate != label]
    stop_pattern = "|".join(subsection_header_pattern(candidate) for candidate in stop_labels)
    stop_match = re.search(rf"(?m)^(?:- )?(?:{stop_pattern})\s*", block)
    if stop_match:
        block = block[: stop_match.start()]
    return block.strip()


@dataclass
class Summary:
    path: Path
    frontmatter: OrderedDict
    body: str
    sections: Dict[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--paper-id",
        action="append",
        default=[],
        help="Restrict processing to one or more paper IDs.",
    )
    parser.add_argument(
        "--write-frontmatter",
        action="store_true",
        help="Write normalized frontmatter back into raw/summaries/*.md.",
    )
    parser.add_argument(
        "--write-index",
        action="store_true",
        help="Write derived/paper_index.yaml.",
    )
    return parser.parse_args()


def read_alias_map(path: Path) -> Dict[str, Dict[str, List[str]]]:
    return parse_simple_yaml(path.read_text())


def split_frontmatter(text: str) -> Tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return "", text
    _, frontmatter, body = parts
    return frontmatter, body


def parse_inline_value(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.startswith("[") or value.startswith("{"):
        try:
            return ast.literal_eval(value)
        except Exception:
            return value
    if value.startswith('"') and value.endswith('"'):
        return ast.literal_eval(value)
    if value.startswith("'") and value.endswith("'"):
        return ast.literal_eval(value)
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.lower() == "null":
        return None
    return value


def parse_frontmatter(frontmatter_block: str) -> OrderedDict:
    data: "OrderedDict[str, Any]" = OrderedDict()
    lines = frontmatter_block.splitlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx].rstrip()
        idx += 1
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        if value.strip():
            data[key] = parse_inline_value(value)
            continue
        items: List[Any] = []
        while idx < len(lines):
            item_line = lines[idx].rstrip()
            if not item_line.strip():
                idx += 1
                continue
            item_match = re.match(r"^\s*-\s+(.*)$", item_line)
            if not item_match:
                break
            items.append(parse_inline_value(item_match.group(1)))
            idx += 1
        data[key] = items if items else ""
    return data


def parse_simple_yaml(text: str) -> Any:
    lines = text.splitlines()

    def nonempty(index: int) -> int:
        while index < len(lines) and not lines[index].strip():
            index += 1
        return index

    def line_indent(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def parse_block(index: int, indent: int) -> Tuple[Any, int]:
        index = nonempty(index)
        if index >= len(lines):
            return OrderedDict(), index
        stripped = lines[index].strip()
        if stripped.startswith("- "):
            items: List[Any] = []
            while index < len(lines):
                index = nonempty(index)
                if index >= len(lines):
                    break
                line = lines[index]
                current_indent = line_indent(line)
                if current_indent != indent or not line.strip().startswith("- "):
                    break
                content = line.strip()[2:].strip()
                index += 1
                if content:
                    items.append(parse_inline_value(content))
                    continue
                nested, index = parse_block(index, indent + 2)
                items.append(nested)
            return items, index

        mapping: "OrderedDict[str, Any]" = OrderedDict()
        while index < len(lines):
            index = nonempty(index)
            if index >= len(lines):
                break
            line = lines[index]
            current_indent = line_indent(line)
            if current_indent != indent or line.strip().startswith("- "):
                break
            match = re.match(r"^\s*([^:]+):\s*(.*)$", line)
            if not match:
                index += 1
                continue
            key, value = match.groups()
            index += 1
            key = key.strip()
            if value.strip():
                mapping[key] = parse_inline_value(value.strip())
                continue
            nested, index = parse_block(index, indent + 2)
            mapping[key] = nested
        return mapping, index

    parsed, _ = parse_block(0, 0)
    return parsed


def parse_sections(body: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    matches = list(re.finditer(r"^### (.+)$", body, re.MULTILINE))
    for idx, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[name] = body[start:end].strip()
    return sections


def load_summaries() -> List[Summary]:
    summaries: List[Summary] = []
    for path in sorted(SUMMARIES_DIR.glob("*.md")):
        if path.name == "STATUS.md":
            continue
        text = path.read_text()
        frontmatter_block, body = split_frontmatter(text)
        frontmatter = parse_frontmatter(frontmatter_block)
        sections = parse_sections(body)
        summaries.append(Summary(path=path, frontmatter=frontmatter, body=body, sections=sections))
    return summaries


def filter_summaries(summaries: List[Summary], paper_ids: List[str]) -> List[Summary]:
    if not paper_ids:
        return summaries
    wanted = set(paper_ids)
    return [summary for summary in summaries if paper_id_from_path(summary.path) in wanted]


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"['’]", "", text)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")


def paper_id_from_path(path: Path) -> str:
    return path.stem


def split_authors(raw_authors: Any) -> List[str]:
    if isinstance(raw_authors, list):
        return [str(item).strip() for item in raw_authors if str(item).strip()]
    text = str(raw_authors).strip()
    if not text:
        return []
    text = text.replace(" and ", ", ")
    text = text.replace(" & ", ", ")
    parts = [part.strip() for part in text.split(",") if part.strip()]
    return parts


def inline_yaml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if value is None:
        return "null"
    if isinstance(value, str):
        if re.fullmatch(r"[A-Za-z0-9_./+-]+", value):
            return value
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return str(value)


def dump_frontmatter(frontmatter: OrderedDict) -> str:
    ordered = OrderedDict()
    for key in FRONTMATTER_ORDER:
        if key in frontmatter and frontmatter[key] not in (None, "", []):
            ordered[key] = frontmatter[key]
    for key, value in frontmatter.items():
        if key not in ordered and value not in (None, "", []):
            ordered[key] = value
    lines = ["---"]
    for key, value in ordered.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {inline_yaml_value(item)}")
        else:
            lines.append(f"{key}: {inline_yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def extract_keyword_block(text: str) -> str:
    block = text.strip()
    if has_structured_subsections(block):
        return extract_structured_subsection(block, "Keywords")
    for stopper in (
        "\n**Key citations**:",
        "\n**Key citations:**",
        "\n**Named models or frameworks**:",
        "\n**Named models or frameworks:**",
        "\n**Brain regions**:",
        "\n**Brain regions:**",
        "\n**Keywords**:",
        "\n**Keywords:**",
        "\n- **Named models or frameworks**:",
        "\n- **Named models or frameworks:**",
        "\n- **Brain regions**:",
        "\n- **Brain regions:**",
        "\n- **Keywords**:",
        "\n- **Keywords:**",
    ):
        if stopper in block:
            block = block.split(stopper, 1)[0]
    return block.strip()


def split_keyword_candidates(text: str) -> List[str]:
    chunks = []
    for part in re.split(r"[,\n;]", text):
        item = part.strip(" -\t")
        if item:
            chunks.append(item)
    return chunks


def compile_alias_patterns(alias_map: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[Tuple[str, re.Pattern]]]:
    compiled: Dict[str, List[Tuple[str, re.Pattern]]] = {}
    for category, mapping in alias_map.items():
        patterns: List[Tuple[str, re.Pattern]] = []
        for canonical, aliases in mapping.items():
            variants = [canonical.replace("_", " ")] + list(aliases)
            seen = set()
            for alias in variants:
                normalized = alias.lower().strip()
                if normalized in seen:
                    continue
                seen.add(normalized)
                regex = re.compile(rf"(?<![a-z0-9]){re.escape(normalized)}(?![a-z0-9])")
                patterns.append((canonical, regex))
        compiled[category] = patterns
    return compiled


def match_aliases(text: str, patterns: Iterable[Tuple[str, re.Pattern]]) -> List[str]:
    matched: List[str] = []
    lowered = text.lower()
    for canonical, pattern in patterns:
        if pattern.search(lowered) and canonical not in matched:
            matched.append(canonical)
    return matched


def extract_citation_block(summary: Summary) -> str:
    section_text = summary.sections.get("Connections & keywords", "")
    if section_text:
        return extract_structured_subsection(section_text, "Key citations")
    return ""


def first_author_surname(authors_value: Any, paper_id: str) -> str:
    authors = split_authors(authors_value)
    if authors:
        surname = authors[0].split()[-1]
        return normalize_text(surname)
    prefix_match = re.match(r"(.+?)(\d{4})", paper_id)
    return normalize_text(prefix_match.group(1) if prefix_match else paper_id)


def build_citation_lookup(summaries: List[Summary]) -> Dict[Tuple[str, int], str]:
    lookup: Dict[Tuple[str, int], str] = {}
    for summary in summaries:
        paper_id = paper_id_from_path(summary.path)
        year = summary.frontmatter.get("year")
        if not isinstance(year, int):
            continue
        surname = first_author_surname(summary.frontmatter.get("authors", ""), paper_id)
        lookup[(surname, year)] = paper_id
        prefix_match = re.match(r"(.+?)(\d{4})", paper_id)
        if prefix_match:
            prefix = normalize_text(prefix_match.group(1))
            lookup.setdefault((prefix, year), paper_id)
    return lookup


def extract_citation_mentions(text: str) -> List[Tuple[str, int]]:
    mentions: List[Tuple[str, int]] = []
    patterns = [
        r"([A-Z][A-Za-z'’\-]+)(?:\s+et al\.)?\s*\((\d{4})\)",
        r"([A-Z][A-Za-z'’\-]+)\s+and\s+[A-Z][A-Za-z'’\-]+\s*\((\d{4})\)",
        r"([A-Z][A-Za-z'’\-]+)\s+et al\.,?\s*(\d{4})",
        r"([A-Z][A-Za-z'’\-]+)\s*&\s+[A-Z][A-Za-z'’\-]+\s*\((\d{4})\)",
    ]
    seen = set()
    for pattern in patterns:
        for author, year in re.findall(pattern, text):
            key = (normalize_text(author), int(year))
            if key not in seen:
                seen.add(key)
                mentions.append(key)
    return mentions


def extract_keywords(summary: Summary) -> List[str]:
    raw_block = summary.sections.get("Connections & keywords", "")
    raw_block = extract_keyword_block(raw_block)
    keywords: List[str] = []
    for item in split_keyword_candidates(raw_block):
        token = normalize_text(item)
        if not token or token in TITLE_STOPWORDS or token == "key_citations":
            continue
        if token not in keywords:
            keywords.append(token)
    return keywords[:20]


def normalized_title_keywords(title: str) -> List[str]:
    parts = [normalize_text(part) for part in re.split(r"[\s:/\-]+", title)]
    keywords: List[str] = []
    for part in parts:
        if len(part) < 3 or part in TITLE_STOPWORDS:
            continue
        if part not in keywords:
            keywords.append(part)
    return keywords[:10]


def extract_semantic_fields(
    summary: Summary,
    patterns: Dict[str, List[Tuple[str, re.Pattern]]],
    citation_lookup: Dict[Tuple[str, int], str],
) -> Dict[str, Any]:
    sections = summary.sections
    title = str(summary.frontmatter.get("title", ""))
    paper_id = paper_id_from_path(summary.path)
    category_text = {
        "species": "\n".join(
            [
                title,
                sections.get("One-line summary", ""),
                sections.get("Methods", ""),
                sections.get("Background & motivation", ""),
            ]
        ),
        "tasks": "\n".join(
            [
                title,
                sections.get("One-line summary", ""),
                sections.get("Methods", ""),
                sections.get("Connections & keywords", ""),
            ]
        ),
        "methods": "\n".join(
            [
                sections.get("Methods", ""),
                sections.get("Connections & keywords", ""),
                sections.get("One-line summary", ""),
            ]
        ),
        "brain_regions": "\n".join(
            [
                title,
                sections.get("Brain regions & systems", ""),
                sections.get("One-line summary", ""),
                sections.get("Methods", ""),
            ]
        ),
        "frameworks": "\n".join(
            [
                sections.get("Computational framework", ""),
                sections.get("Prevailing model of the system under study", ""),
                sections.get("One-line summary", ""),
                sections.get("Connections & keywords", ""),
            ]
        ),
    }

    extracted: Dict[str, Any] = {}
    for category, text in category_text.items():
        extracted[category] = match_aliases(text, patterns[category])
    if any(species in extracted["species"] for species in ("mouse", "rat", "macaque", "monkey")):
        extracted["species"] = [species for species in extracted["species"] if species != "human"]

    keyword_candidates = extract_keywords(summary)
    for item in normalized_title_keywords(title):
        if item not in keyword_candidates:
            keyword_candidates.append(item)
    extracted["keywords"] = keyword_candidates[:20]

    citation_texts = []
    key_citation_block = extract_citation_block(summary)
    if key_citation_block:
        citation_texts.append(key_citation_block)
    for name in (
        "Background & motivation",
        "Computational framework",
        "Prevailing model of the system under study",
    ):
        citation_texts.append(sections.get(name, ""))
    resolved: List[str] = []
    for text in citation_texts:
        for mention in extract_citation_mentions(text):
            cited = citation_lookup.get(mention)
            if cited and cited != paper_id and cited not in resolved:
                resolved.append(cited)
    extracted["key_citations"] = resolved
    return extracted


def count_open_questions(summary: Summary) -> int:
    section = summary.sections.get("Limitations & open questions", "")
    if not section:
        return 0
    bullets = re.findall(r"(?m)^(?:- |\d+\. )", section)
    if bullets:
        return len(bullets)
    return section.count("?")


def summary_quality(summary: Summary, extracted: Dict[str, Any]) -> str:
    present_sections = sum(1 for header in SECTION_HEADERS if summary.sections.get(header))
    structured_hits = sum(1 for key in ("species", "tasks", "methods", "brain_regions", "frameworks") if extracted.get(key))
    if present_sections >= 10 and structured_hits >= 3:
        return "high"
    if present_sections >= 8 and structured_hits >= 2:
        return "medium"
    return "low"


def build_paper_index(summaries: List[Summary], extracted_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    papers: List[Dict[str, Any]] = []
    for summary in summaries:
        paper_id = paper_id_from_path(summary.path)
        frontmatter = summary.frontmatter
        extracted = extracted_by_id[paper_id]
        papers.append(
            OrderedDict(
                [
                    ("paper_id", paper_id),
                    ("path", f"raw/summaries/{summary.path.name}"),
                    ("title", frontmatter.get("title", "")),
                    ("year", frontmatter.get("year")),
                    ("authors", split_authors(frontmatter.get("authors", ""))),
                    ("journal", frontmatter.get("journal", "")),
                    ("paper_type", frontmatter.get("paper_type", "")),
                    ("contribution_type", frontmatter.get("contribution_type", "")),
                    ("species", extracted.get("species", [])),
                    ("tasks", extracted.get("tasks", [])),
                    ("methods", extracted.get("methods", [])),
                    ("brain_regions", extracted.get("brain_regions", [])),
                    ("frameworks", extracted.get("frameworks", [])),
                    ("keywords", extracted.get("keywords", [])),
                    ("one_line_summary", clean_one_line_summary(summary.sections.get("One-line summary", ""))),
                    ("key_citations", extracted.get("key_citations", [])),
                    ("open_question_count", count_open_questions(summary)),
                    ("summary_quality", summary_quality(summary, extracted)),
                ]
            )
        )
    return OrderedDict(
        [
            ("generated_at", "manual_run"),
            ("paper_count", len(papers)),
            ("papers", papers),
        ]
    )


def dump_yaml(value: Any, indent: int = 0) -> List[str]:
    prefix = " " * indent
    if isinstance(value, (dict, OrderedDict)):
        lines: List[str] = []
        for key, item in value.items():
            if isinstance(item, list) and not item:
                lines.append(f"{prefix}{key}: []")
            elif isinstance(item, (dict, OrderedDict, list)):
                lines.append(f"{prefix}{key}:")
                lines.extend(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{prefix}{key}: {inline_yaml_value(item)}")
        return lines
    if isinstance(value, list):
        lines = []
        for item in value:
            if isinstance(item, (dict, OrderedDict)):
                lines.append(f"{prefix}-")
                lines.extend(dump_yaml(item, indent + 2))
            elif isinstance(item, list):
                lines.append(f"{prefix}-")
                lines.extend(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{prefix}- {inline_yaml_value(item)}")
        return lines
    return [f"{prefix}{inline_yaml_value(value)}"]


def write_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(dump_yaml(payload)) + "\n"
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(text)
    tmp_path.replace(path)


def clean_one_line_summary(text: str) -> str:
    lines = []
    for line in text.strip().splitlines():
        if line.strip() == "---":
            continue
        lines.append(line.rstrip())
    return "\n".join(lines).strip()


def write_normalized_frontmatter(summary: Summary, extracted: Dict[str, Any]) -> None:
    updated = OrderedDict(summary.frontmatter)
    updated["source_file"] = summary.path.name
    updated["paper_id"] = paper_id_from_path(summary.path)
    updated["authors"] = split_authors(updated.get("authors", ""))
    for key in ("species", "tasks", "methods", "brain_regions", "frameworks", "keywords", "key_citations"):
        updated[key] = extracted.get(key, [])
    new_text = dump_frontmatter(updated) + summary.body.lstrip("\n")
    if summary.path.read_text() != new_text:
        summary.path.write_text(new_text)


def main() -> int:
    args = parse_args()
    alias_map = read_alias_map(ALIAS_MAP_PATH)
    summaries = filter_summaries(load_summaries(), args.paper_id)
    if not summaries:
        print("No summaries found.", file=sys.stderr)
        return 1

    patterns = compile_alias_patterns(alias_map)
    citation_lookup = build_citation_lookup(summaries)

    extracted_by_id: Dict[str, Dict[str, Any]] = {}
    for summary in summaries:
        paper_id = paper_id_from_path(summary.path)
        extracted_by_id[paper_id] = extract_semantic_fields(summary, patterns, citation_lookup)

    if args.write_frontmatter:
        for summary in summaries:
            write_normalized_frontmatter(summary, extracted_by_id[paper_id_from_path(summary.path)])

    if args.write_index:
        index_payload = build_paper_index(summaries, extracted_by_id)
        write_yaml(PAPER_INDEX_PATH, index_payload)

    print(
        f"Processed {len(summaries)} summaries"
        + (" and updated frontmatter" if args.write_frontmatter else "")
        + (" and wrote paper_index.yaml" if args.write_index else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
