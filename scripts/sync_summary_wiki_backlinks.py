#!/usr/bin/env python3
"""Sync backlinks from active wiki pages into raw summary notes."""

from __future__ import annotations

import argparse
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Any, Dict, List

from normalize_summaries import (
    REPO_ROOT,
    Summary,
    dump_frontmatter,
    load_summaries,
    parse_frontmatter,
    parse_simple_yaml,
    split_frontmatter,
)


DERIVED_DIR = REPO_ROOT / "derived"
WIKI_DIR = REPO_ROOT / "wiki"
CATALOG_GLOB = "*subtopic_catalog.yaml"
SECTION_NAME = "Related wiki pages"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write wiki backlinks into raw summaries.")
    return parser.parse_args()


def active_pages() -> Dict[str, Dict[str, str]]:
    pages: Dict[str, Dict[str, str]] = {}
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
            title = str(frontmatter.get("title", "")).strip()
            if not title:
                for line in body.splitlines():
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
            pages[subtopic_id] = {
                "path": str(path.relative_to(REPO_ROOT).with_suffix("")),
                "title": title or path.stem,
            }
    return pages


def page_membership() -> Dict[str, List[Dict[str, str]]]:
    active = active_pages()
    memberships: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for catalog_path in sorted(DERIVED_DIR.glob(CATALOG_GLOB)):
        catalog = parse_simple_yaml(catalog_path.read_text())
        for subtopic in catalog.get("selected_subtopics", []):
            subtopic_id = subtopic.get("subtopic_id")
            if subtopic_id not in active:
                continue
            page = active[subtopic_id]
            for paper_id in subtopic.get("candidate_papers", []) or []:
                memberships[paper_id].append(page)
    for paper_id, pages in memberships.items():
        pages.sort(key=lambda page: (page["title"], page["path"]))
    return memberships


def replace_or_append_section(body: str, section_name: str, section_text: str) -> str:
    marker = f"### {section_name}"
    if marker in body:
        start = body.index(marker)
        remainder = body[start:]
        next_header = remainder.find("\n### ", len(marker))
        end = start + next_header + 1 if next_header != -1 else len(body)
        new_body = body[:start].rstrip() + "\n\n" + section_text.strip() + "\n"
        if end < len(body):
            new_body += "\n" + body[end:].lstrip("\n")
        return new_body
    return body.rstrip() + "\n\n" + section_text.strip() + "\n"


def render_section(pages: List[Dict[str, str]]) -> str:
    lines = [f"### {SECTION_NAME}"]
    for page in pages:
        lines.append(f"- [[{page['path']}|{page['title']}]]")
    return "\n".join(lines)


def update_summary(summary: Summary, pages: List[Dict[str, str]]) -> str:
    frontmatter = OrderedDict(summary.frontmatter)
    if pages:
        frontmatter["wiki_pages"] = [page["path"] for page in pages]
    else:
        frontmatter.pop("wiki_pages", None)

    body = summary.body.rstrip() + "\n"
    marker = f"### {SECTION_NAME}"
    if pages:
        body = replace_or_append_section(body, SECTION_NAME, render_section(pages))
    elif marker in body:
        start = body.index(marker)
        remainder = body[start:]
        next_header = remainder.find("\n### ", len(marker))
        end = start + next_header + 1 if next_header != -1 else len(body)
        body = body[:start].rstrip() + ("\n" + body[end:].lstrip("\n") if end < len(body) else "\n")
    return dump_frontmatter(frontmatter) + body.lstrip("\n")


def main() -> int:
    args = parse_args()
    memberships = page_membership()
    summaries = load_summaries()
    updated = 0
    for summary in summaries:
        paper_id = str(summary.frontmatter.get("paper_id", summary.path.stem))
        new_text = update_summary(summary, memberships.get(paper_id, []))
        if args.write and summary.path.read_text() != new_text:
            summary.path.write_text(new_text)
            updated += 1
    print(f"Computed wiki backlinks for {len(summaries)} summaries; updated {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
