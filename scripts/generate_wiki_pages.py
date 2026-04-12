#!/usr/bin/env python3
"""Generate wiki topic and debate pages from the curated subtopic catalog."""

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

from normalize_summaries import (
    REPO_ROOT,
    DERIVED_DIR,
    SUMMARIES_DIR,
    Summary,
    clean_one_line_summary,
    dump_yaml,
    load_summaries,
    parse_simple_yaml,
)


SUBTOPIC_CATALOG_PATH = DERIVED_DIR / "subtopic_catalog.yaml"
DOTENV_PATH = REPO_ROOT / ".env"
WIKI_DIR = REPO_ROOT / "wiki"
TOPICS_DIR = WIKI_DIR / "topics"
DEBATES_DIR = WIKI_DIR / "debates"
INDICES_DIR = WIKI_DIR / "indices"
INDEX_PATH = INDICES_DIR / "index.md"
LOG_PATH = WIKI_DIR / "log.md"
PROMPT_VERSION = "wiki-page-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        choices=("openai_api",),
        default="openai_api",
        help="Generation backend to use.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4",
        help="Model name for page generation.",
    )
    parser.add_argument(
        "--subtopic-id",
        action="append",
        default=[],
        help="Restrict generation to one or more subtopic IDs.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=6,
        help="Number of concurrent generation requests.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write generated pages and update index/log.",
    )
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


def slugify(text: str) -> str:
    normalized = text.lower().replace("–", "-").replace("—", "-")
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized or "untitled"


def load_payloads() -> Tuple[Dict[str, Any], Dict[str, Summary], Dict[str, Dict[str, Any]]]:
    catalog = parse_simple_yaml(SUBTOPIC_CATALOG_PATH.read_text())
    summaries = {summary.frontmatter.get("paper_id", summary.path.stem): summary for summary in load_summaries()}
    paper_index = parse_simple_yaml((DERIVED_DIR / "paper_index.yaml").read_text())
    papers = {paper["paper_id"]: paper for paper in paper_index["papers"]}
    return catalog, summaries, papers


def short_section(text: str, limit: int = 900) -> str:
    cleaned = re.sub(r"\n{2,}", "\n", text.strip())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3].rstrip() + "..."


def author_year_label(paper: Dict[str, Any]) -> str:
    authors = paper.get("authors", []) or []
    if authors:
        surname = str(authors[0]).split()[-1]
        if len(authors) == 1:
            author_part = surname
        elif len(authors) == 2:
            author_part = f"{surname} and {str(authors[1]).split()[-1]}"
        else:
            author_part = f"{surname} et al."
    else:
        author_part = paper["paper_id"]
    year = paper.get("year", "")
    return f"{author_part} {year}".strip()


def obsidian_summary_link(paper_id: str, paper: Dict[str, Any]) -> str:
    return f"[[raw/summaries/{paper_id}|{author_year_label(paper)}]]"


def obsidian_source_link(paper_id: str) -> str:
    candidate = REPO_ROOT / "raw" / "mds" / f"{paper_id}.md"
    if candidate.exists():
        return f"[[raw/mds/{paper_id}|source md]]"
    return ""


def build_paper_block(paper_id: str, summary: Summary, paper: Dict[str, Any]) -> str:
    sections = summary.sections
    lines = [
        f"paper_id: {paper_id}",
        f"title: {paper.get('title', '')}",
        f"year: {paper.get('year', '')}",
        f"paper_type: {paper.get('paper_type', '')}",
        f"contribution_type: {paper.get('contribution_type', '')}",
        f"one_line_summary: {paper.get('one_line_summary', '')}",
        f"methods: {', '.join(paper.get('methods', []) or [])}",
        f"brain_regions: {', '.join(paper.get('brain_regions', []) or [])}",
        f"frameworks: {', '.join(paper.get('frameworks', []) or [])}",
        "key_findings:",
        short_section(sections.get("Key findings", ""), 1100),
        "what_this_paper_contributes:",
        short_section(sections.get("What this paper contributes", ""), 900),
        "limitations_open_questions:",
        short_section(sections.get("Limitations & open questions", ""), 700),
    ]
    return "\n".join(lines)


def build_roster_block(paper_ids: List[str], papers: Dict[str, Dict[str, Any]]) -> str:
    lines = []
    for paper_id in paper_ids:
        paper = papers[paper_id]
        lines.append(
            f"- {paper_id} | {paper.get('title', '')} | {paper.get('year', '')} | {paper.get('one_line_summary', '')}"
        )
    return "\n".join(lines)


def build_prompt(
    subtopic: Dict[str, Any],
    summaries: Dict[str, Summary],
    papers: Dict[str, Dict[str, Any]],
) -> str:
    anchor_blocks = []
    for paper_id in subtopic["anchor_papers"][:5]:
        summary = summaries[paper_id]
        paper = papers[paper_id]
        anchor_blocks.append(build_paper_block(paper_id, summary, paper))

    core_roster = build_roster_block(subtopic["core_papers"], papers)
    supporting_roster = build_roster_block(subtopic["supporting_papers"], papers)

    if subtopic["page_type"] == "debate":
        page_instructions = "\n".join(
            [
                "Write a debate page with these exact sections:",
                "## Central question",
                "## Strongest case for the main mechanism or position",
                "## Strongest alternatives or challenges",
                "## What the literature currently supports",
                "## Open questions",
                "## Key papers",
            ]
        )
    else:
        page_instructions = "\n".join(
            [
                "Write a topic page with these exact sections:",
                "## Current view",
                "## Strongest evidence",
                "## Landmark papers",
                "## Boundaries and tensions",
                "## Open questions",
                "## Key papers",
            ]
        )

    return "\n\n".join(
        [
            "You are writing a concise but high-value markdown page for a persistent neuroscience research wiki.",
            "The page should be evidence-dense, skeptical, and synthesis-first. Avoid generic survey prose.",
            "Do not invent claims beyond the provided evidence. If the literature is mixed, say so plainly.",
            "Use short paragraphs and flat bullets only when useful.",
            "Use inline Obsidian-style links for papers in the format [[raw/summaries/paper_id|Author et al. Year]].",
            "Return markdown only. Do not wrap in code fences.",
            page_instructions,
            "Start with a one-paragraph lead directly under the H1 title.",
            "",
            f"Subtopic title: {subtopic['refined_label']}",
            f"Subtopic ID: {subtopic['subtopic_id']}",
            f"Parent topic: {subtopic['parent_label']}",
            f"Page type: {subtopic['page_type']}",
            f"Page worthiness: {subtopic['page_worthiness']}",
            f"Judge summary: {subtopic['judge_summary']}",
            f"Top frameworks: {', '.join(subtopic['top_terms']['frameworks'])}",
            f"Top brain regions: {', '.join(subtopic['top_terms']['brain_regions'])}",
            f"Top tasks: {', '.join(subtopic['top_terms']['tasks'])}",
            f"Top keywords: {', '.join(subtopic['top_terms']['keywords'])}",
            "",
            "Anchor papers (rich evidence):",
            "\n\n".join(anchor_blocks),
            "",
            "Core paper roster:",
            core_roster,
            "",
            "Supporting paper roster:",
            supporting_roster,
        ]
    )


def run_openai_api(prompt: str, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    payload = {
        "model": model,
        "input": prompt,
        "text": {"verbosity": "medium"},
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
    output = parsed.get("output", []) or []
    text_chunks = []
    for item in output:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text":
                text_chunks.append(content.get("text", ""))
    text = "\n".join(chunk for chunk in text_chunks if chunk).strip()
    if not text:
        raise RuntimeError("openai api returned no text content")
    return text


def output_path_for_subtopic(
    subtopic: Dict[str, Any],
    used_paths: set[str],
) -> Path:
    stem = slugify(subtopic["refined_label"])
    if stem in used_paths:
        stem = f"{stem}__{subtopic['subtopic_id']}"
    used_paths.add(stem)
    directory = DEBATES_DIR if subtopic["page_type"] == "debate" else TOPICS_DIR
    return directory / f"{stem}.md"


def render_frontmatter(subtopic: Dict[str, Any], relative_path: str) -> str:
    payload = OrderedDict(
        [
            ("title", subtopic["refined_label"]),
            ("subtopic_id", subtopic["subtopic_id"]),
            ("parent_topic_id", subtopic["parent_topic_id"]),
            ("page_type", subtopic["page_type"]),
            ("page_worthiness", subtopic["page_worthiness"]),
            ("status", "draft_llm"),
            ("generated_at", datetime.now(timezone.utc).isoformat()),
            ("generated_by", "generate_wiki_pages.py"),
            ("prompt_version", PROMPT_VERSION),
            ("source_catalog", relative_path),
            ("anchor_papers", subtopic["anchor_papers"]),
            ("core_papers", subtopic["core_papers"]),
        ]
    )
    return "---\n" + "\n".join(dump_yaml(payload)) + "\n---\n\n"


def source_papers_section(subtopic: Dict[str, Any], papers: Dict[str, Dict[str, Any]]) -> str:
    lines = ["## Source papers"]
    for paper_id in subtopic["anchor_papers"] + [pid for pid in subtopic["core_papers"] if pid not in subtopic["anchor_papers"]]:
        paper = papers[paper_id]
        summary_link = obsidian_summary_link(paper_id, paper)
        source_link = obsidian_source_link(paper_id)
        extra = f" | {source_link}" if source_link else ""
        lines.append(f"- {summary_link}{extra}: {paper.get('title', '')}")
    return "\n".join(lines) + "\n"


def ensure_title(markdown: str, title: str) -> str:
    stripped = markdown.lstrip()
    if stripped.startswith("# "):
        return stripped if markdown == stripped else stripped
    return f"# {title}\n\n{stripped}"


def generate_page_markdown(
    subtopic: Dict[str, Any],
    summaries: Dict[str, Summary],
    papers: Dict[str, Dict[str, Any]],
    model: str,
    relative_catalog_path: str,
) -> str:
    body = run_openai_api(build_prompt(subtopic, summaries, papers), model)
    body = ensure_title(body, subtopic["refined_label"]).rstrip() + "\n\n"
    return render_frontmatter(subtopic, relative_catalog_path) + body + source_papers_section(subtopic, papers)


def build_index(entries: List[Tuple[Dict[str, Any], Path]]) -> str:
    existing_entries = [(subtopic, path) for subtopic, path in entries if path.exists()]
    topic_entries = [(subtopic, path) for subtopic, path in existing_entries if subtopic["page_type"] == "topic"]
    debate_entries = [(subtopic, path) for subtopic, path in existing_entries if subtopic["page_type"] == "debate"]

    lines = [
        "# Research Wiki Index",
        "",
        "This index covers the current judged subtopic pages generated from the refactored corpus pipeline.",
        "",
        f"- Topic pages: {len(topic_entries)}",
        f"- Debate pages: {len(debate_entries)}",
        "",
        "## Topics",
    ]
    for subtopic, path in sorted(topic_entries, key=lambda item: (-item[0]["page_worthiness"], item[0]["refined_label"])):
        rel = path.relative_to(WIKI_DIR)
        lines.append(
            f"- [[{rel.with_suffix('')}|{subtopic['refined_label']}]]: {subtopic['judge_summary']}"
        )
    lines.extend(["", "## Debates"])
    for subtopic, path in sorted(debate_entries, key=lambda item: item[0]["refined_label"]):
        rel = path.relative_to(WIKI_DIR)
        lines.append(
            f"- [[{rel.with_suffix('')}|{subtopic['refined_label']}]]: {subtopic['judge_summary']}"
        )
    lines.append("")
    return "\n".join(lines)


def append_log(generated: List[Tuple[Dict[str, Any], Path]]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"## [{timestamp}] generate | First wiki topic pages from judged subtopics", ""]
    for subtopic, path in sorted(generated, key=lambda item: item[0]["subtopic_id"]):
        rel = path.relative_to(REPO_ROOT)
        lines.append(
            f"- {subtopic['subtopic_id']} -> {rel} ({subtopic['page_type']}, worthiness {subtopic['page_worthiness']})"
        )
    lines.append("")
    with LOG_PATH.open("a") as handle:
        handle.write("\n".join(lines))


def main() -> int:
    args = parse_args()
    load_dotenv(DOTENV_PATH)
    catalog, summaries, papers = load_payloads()
    wanted = set(args.subtopic_id)

    all_selected = [
        subtopic
        for subtopic in catalog["selected_subtopics"]
        if subtopic.get("keep")
    ]
    if not all_selected:
        print("No selected subtopics to generate.")
        return 0

    used_paths: set[str] = set()
    relative_catalog_path = "derived/subtopic_catalog.yaml"
    all_tasks = []
    for subtopic in all_selected:
        output_path = output_path_for_subtopic(subtopic, used_paths)
        all_tasks.append((subtopic, output_path))

    tasks = [
        (subtopic, output_path)
        for subtopic, output_path in all_tasks
        if not wanted or subtopic["subtopic_id"] in wanted
    ]
    if not tasks:
        print("No selected subtopics matched the requested IDs.")
        return 0

    generated: List[Tuple[Dict[str, Any], Path, str]] = []
    failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
        futures = {
            executor.submit(
                generate_page_markdown,
                subtopic,
                summaries,
                papers,
                args.model,
                relative_catalog_path,
            ): (subtopic, output_path)
            for subtopic, output_path in tasks
        }
        for future in concurrent.futures.as_completed(futures):
            subtopic, output_path = futures[future]
            try:
                markdown = future.result()
            except Exception as exc:
                failed += 1
                print(f"{subtopic['subtopic_id']} error={exc}", file=sys.stderr)
                continue
            generated.append((subtopic, output_path, markdown))
            print(
                f"{subtopic['subtopic_id']} -> {output_path.relative_to(REPO_ROOT)} "
                f"({subtopic['page_type']}, worthiness {subtopic['page_worthiness']})"
            )
            sys.stdout.flush()

    if failed:
        print(f"Generation completed with {failed} failures.", file=sys.stderr)
    if not args.write:
        return 0 if generated else 1

    for _, directory in (("topics", TOPICS_DIR), ("debates", DEBATES_DIR), ("indices", INDICES_DIR)):
        directory.mkdir(parents=True, exist_ok=True)
    for subtopic, output_path, markdown in generated:
        output_path.write_text(markdown)

    generated_pairs = [(subtopic, output_path) for subtopic, output_path, _ in generated]
    INDEX_PATH.write_text(build_index(all_tasks))
    append_log(generated_pairs)
    print(f"Wrote {len(generated)} pages, updated {INDEX_PATH.relative_to(REPO_ROOT)} and {LOG_PATH.relative_to(REPO_ROOT)}")
    return 0 if generated else 1


if __name__ == "__main__":
    raise SystemExit(main())
