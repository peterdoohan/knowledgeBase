# CLAUDE.md — Knowledge Base

This is a personal academic knowledge base for neuroscience research. It stores paper summaries, raw paper conversions, and a structured wiki of current scientific understanding, all designed to be navigated and updated by AI agents.

---

## Repo structure

```
raw/
  inbox/        # Drop PDFs here to be digested
  pdfs/         # Permanent storage for processed PDFs
  mds/          # Markdown conversions of PDFs (output of /pdf2md)
  summaries/    # Structured paper summaries (output of /make_summary)
  summaries/STATUS.md  # Tracks which summaries have been integrated into the wiki

wiki/
  brain_regions/          # Wiki pages organised by brain region (may be nested)
  behaviours/             # Wiki pages organised by behaviour/paradigm
  computational_frameworks/  # Wiki pages organised by computational framework
  methods/                # Wiki pages organised by experimental/analysis method

index.md        # Wiki navigation and primitive search index — read this before globbing wiki/
log.md          # Append-only YAML activity log — read this to check recent agent activity
CLAUDE.md       # This file
```

---

## File naming convention

All files in `raw/mds/` and `raw/summaries/` follow:

```
firstauthorsurname+year_keyword1_keyword2.md
```

Examples: `adams2018_attractor_schizophrenia.md`, `akam2021_dopamine_model_based_rl.md`

- Lowercase, underscores, no spaces
- Year immediately after surname (no separator)
- 2–4 keywords from the title

Wiki pages use descriptive snake_case names reflecting the concept, not a paper: `sequence_working_memory.md`.

---

## Pipeline overview

```
raw/inbox/<paper>.pdf
    ↓ /digest
  /pdf2md  →  raw/mds/<paper>.md  +  raw/pdfs/<paper>.pdf
    ↓
  /make_summary  →  raw/summaries/<paper>.md
    ↓
  log.md  ←  entry added (event: summary_ready)
```

After `/digest`, summaries in `raw/summaries/` are ready for wiki integration.

---

## Skills

### Ingestion pipeline

| Skill | Trigger | What it does |
|---|---|---|
| `/digest` | Manual, when PDFs dropped in `raw/inbox/` | Full ingestion pipeline for all inbox PDFs |
| `/pdf2md` | Called by `/digest` or manually | Converts a single PDF to Markdown using `pymupdf4llm` (conda env: `claude_code`) |
| `/make_summary` | Called by `/digest` or manually | Reads a paper MD and writes a structured summary to `raw/summaries/` |

### Wiki pipeline

| Skill | Trigger | What it does |
|---|---|---|
| `/wiki_init` | Manual, once on a cold wiki | Bootstraps wiki from all summaries in `raw/summaries/`; runs full pipeline then reviewer |
| `/fact_finder` | Called by `/wiki_init` or `/wiki_integrate` | Extracts 3–8 discrete, wiki-ready facts from a single summary as a YAML payload |
| `/router` | Called by `/wiki_init` or `/wiki_integrate` | Routes facts to target wiki pages; creates stub pages and updates `index.md` as needed |
| `/wiki_writer` | Called by `/wiki_init` or `/wiki_integrate` | Writes a single routed fact to a wiki page; checks for duplication and relevance first |
| `/reviewer` | Called at end of `/wiki_init` or manually | Adversarial pass over recent wiki changes; flags inconsistencies with `[!INCONSISTENCY]` markers |

---

## log.md format

`log.md` is an append-only YAML list. Each entry has at minimum:

```yaml
- timestamp: 2026-04-05T14:32:01   # ISO 8601 UTC
  agent: digest                     # skill or agent that wrote the entry
  event: summary_ready              # event type
  summary: raw/summaries/foo.md     # path to the output (for summary_ready events)
```

Always append — never overwrite existing entries.

---

## index.md format

`index.md` has two sections:

1. **Wiki structure** — a YAML tree mirroring the actual `wiki/` directory. Update this when pages are created or deleted.
2. **Search index** — a flat YAML list of all wiki pages with keywords. Use this for primitive search (grep keywords against this list) before reading any wiki files.

Always update `index.md` when creating, renaming, or deleting wiki pages.

---

## Wiki page conventions

Each wiki page represents the **current scientific understanding** of a concept (brain region, behaviour, framework, or method). Pages are living documents — they should be updated as new evidence challenges or refines the prevailing model.

Recommended page structure:

1. **Current understanding** — the best current model of how this thing works, synthesised across all digested papers
2. **Key evidence** — bullet points with links to supporting summaries (`[Adams 2018](../../raw/summaries/adams2018_attractor_schizophrenia.md)`)
3. **History of ideas** — how the understanding evolved over time
4. **Open questions** — unresolved issues flagged by the literature
5. **Related pages** — links to other wiki pages (cross-category links encouraged)

Wiki pages should link back to `raw/summaries/` and `raw/mds/` files for agents that need to query the source material.

---

## Agent guidance

- **Before navigating the wiki**: read `index.md` first — it tells you what pages exist and their keywords. Only glob `wiki/` if `index.md` is insufficient.
- **Before acting**: read `log.md` to check what other agents have recently done and what is queued for wiki integration.
- **Do not hallucinate**: all wiki content must be grounded in summaries in `raw/summaries/`. If a claim cannot be traced to a summary, flag it.
- **When creating a wiki page**: add it to `index.md` immediately.
- **Filename mismatches**: `/make_summary` will auto-correct mismatched filenames and report them — trust its output filename over the input filename.
