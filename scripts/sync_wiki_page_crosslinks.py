#!/usr/bin/env python3
"""Sync related-page crosslinks into active wiki pages from the editorial audit."""

from __future__ import annotations

import argparse
from collections import OrderedDict, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import REPO_ROOT, dump_frontmatter, parse_frontmatter, parse_simple_yaml, split_frontmatter


DERIVED_DIR = REPO_ROOT / "derived"
WIKI_DIR = REPO_ROOT / "wiki"
AUDIT_PATH = DERIVED_DIR / "wiki_editorial_audit.yaml"
LOG_PATH = WIKI_DIR / "log.md"
SECTION_NAME = "Related wiki pages"
KEEP_DECISIONS = {"keep_distinct_with_crosslink", "bridge_page_candidate", "consider_merge"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write related-page links into wiki pages.")
    return parser.parse_args()


def active_pages() -> Dict[str, Dict[str, Any]]:
    pages: Dict[str, Dict[str, Any]] = {}
    for directory in (WIKI_DIR / "topics", WIKI_DIR / "debates"):
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
            pages[subtopic_id] = {
                "path": path,
                "relative_path": str(path.relative_to(REPO_ROOT).with_suffix("")),
                "frontmatter": frontmatter,
                "body": body,
            }
    return pages


def load_related_map() -> Dict[str, List[Dict[str, str]]]:
    audit = parse_simple_yaml(AUDIT_PATH.read_text())
    related: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for entry in audit.get("entries", []):
        if entry.get("decision") not in KEEP_DECISIONS:
            continue
        page_a = entry["page_a"]
        page_b = entry["page_b"]
        angle = str(entry.get("crosslink_angle", "")).strip()
        relation_a = {
            "subtopic_id": page_b["subtopic_id"],
            "path": page_b["path"],
            "title": page_b["title"],
            "angle": angle,
            "decision": entry["decision"],
            "confidence": int(entry.get("confidence", 0) or 0),
        }
        relation_b = {
            "subtopic_id": page_a["subtopic_id"],
            "path": page_a["path"],
            "title": page_a["title"],
            "angle": angle,
            "decision": entry["decision"],
            "confidence": int(entry.get("confidence", 0) or 0),
        }
        related[page_a["subtopic_id"]].append(relation_a)
        related[page_b["subtopic_id"]].append(relation_b)
    for subtopic_id, relations in related.items():
        relations.sort(
            key=lambda item: (
                -item["confidence"],
                item["decision"] != "keep_distinct_with_crosslink",
                item["title"],
            )
        )
    return related


def replace_or_append_section(body: str, section_name: str, section_text: str) -> str:
    marker = f"## {section_name}"
    if marker in body:
        start = body.index(marker)
        remainder = body[start:]
        next_header = remainder.find("\n## ", len(marker))
        end = start + next_header + 1 if next_header != -1 else len(body)
        new_body = body[:start].rstrip() + "\n\n" + section_text.strip() + "\n"
        if end < len(body):
            new_body += "\n" + body[end:].lstrip("\n")
        return new_body
    source_marker = "\n## Source papers"
    if source_marker in body:
        insert_at = body.index(source_marker)
        return body[:insert_at].rstrip() + "\n\n" + section_text.strip() + "\n\n" + body[insert_at:].lstrip("\n")
    return body.rstrip() + "\n\n" + section_text.strip() + "\n"


def render_section(relations: List[Dict[str, str]]) -> str:
    lines = [f"## {SECTION_NAME}"]
    for relation in relations[:4]:
        suffix = f": {relation['angle']}" if relation["angle"] else ""
        lines.append(f"- [[{relation['path']}|{relation['title']}]]{suffix}")
    return "\n".join(lines)


def update_page(page: Dict[str, Any], relations: List[Dict[str, str]]) -> str:
    frontmatter = OrderedDict(page["frontmatter"])
    if relations:
        frontmatter["related_wiki_pages"] = [relation["path"] for relation in relations[:4]]
    else:
        frontmatter.pop("related_wiki_pages", None)

    body = page["body"].rstrip() + "\n"
    marker = f"## {SECTION_NAME}"
    if relations:
        body = replace_or_append_section(body, SECTION_NAME, render_section(relations))
    elif marker in body:
        start = body.index(marker)
        remainder = body[start:]
        next_header = remainder.find("\n## ", len(marker))
        end = start + next_header + 1 if next_header != -1 else len(body)
        body = body[:start].rstrip() + ("\n" + body[end:].lstrip("\n") if end < len(body) else "\n")
    return dump_frontmatter(frontmatter) + body.lstrip("\n")


def append_log(updated_paths: List[Path]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"## [{timestamp}] maintain | Sync wiki-to-wiki crosslinks", ""]
    lines.append("- Source audit: `derived/wiki_editorial_audit.yaml`")
    for path in sorted(updated_paths):
        lines.append(f"- updated {path.relative_to(REPO_ROOT)}")
    lines.append("")
    with LOG_PATH.open("a") as handle:
        handle.write("\n".join(lines))


def main() -> int:
    args = parse_args()
    pages = active_pages()
    related_map = load_related_map()
    updated_paths: List[Path] = []
    for subtopic_id, page in pages.items():
        new_text = update_page(page, related_map.get(subtopic_id, []))
        if args.write and page["path"].read_text() != new_text:
            page["path"].write_text(new_text)
            updated_paths.append(page["path"])
    if args.write and updated_paths:
        append_log(updated_paths)
    print(f"Computed related-page links for {len(pages)} active wiki pages; updated {len(updated_paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
