# CLAUDE.md — Knowledge Base

This is an AI-maintained neuroscience knowledge base. Its purpose is to generate deeply literature-informed summaries when a user queries a topic. Agents continually review papers to build and maintain a structured wiki representing humanity's best current understanding of how the brain works, alongside an up-to-date index of tools and active research avenues.

The repo stores raw papers, structured summaries, and a living wiki — all designed to be navigated, updated, and queried by AI agents autonomously. The repo should also be structured so that it is human-readable when opened in tools like Obsidian — standard markdown, relative links between files, and a navigable folder hierarchy.

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
.pipeline/      # Temp directory for intermediate YAML files during pipeline runs (can be cleaned up)
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

### Ingestion
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

### Wiki init (cold start)
```
/wiki_init  (orchestrator: opus, summaries sorted oldest-first)
    ↓
  Stage 0a: extract metadata  →  .pipeline/summary_index.yaml (compact: one-line summaries, brain regions, keywords)
    ↓
  Stage 0b: /taxonomy_planner  →  .pipeline/taxonomy.yaml + wiki stubs + index.md (reads summary_index.yaml, not raw files)
    ↓  (batches of 20, checkpointed per-summary in STATUS.md)
  Stage 1: /fact_finder (×N, parallel per batch)  →  .pipeline/<stem>_facts.yaml  [YAML validated]
    ↓
  Stage 1.5: dedup manifest  →  .pipeline/batch_<N>_dedup.yaml
    ↓
  Stage 2: /router (batched, ~1 call per batch)  →  .pipeline/<stem>_routing.yaml  [YAML validated]
    ↓
  Stage 3: /wiki_writer (parallel across different pages)  →  wiki pages updated
    ↓
  Stage 5: /synthesiser batch  →  Current understanding narratives written
    ↓
  Stage 6: /reviewer  →  [!INCONSISTENCY] markers + cross-links
```

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
| `/wiki_init` | Manual, once on a cold wiki | Bootstraps wiki from all summaries; runs taxonomy → facts → route → write → synthesise → review |
| `/taxonomy_planner` | Called by `/wiki_init` or manually | Scans all summaries, designs canonical wiki structure, creates stubs, writes `.pipeline/taxonomy.yaml` |
| `/fact_finder` | Called by `/wiki_init` or `/wiki_integrate` | Extracts 3–8 discrete, wiki-ready facts from a single summary; normalises topics against taxonomy |
| `/router` | Called by `/wiki_init` or `/wiki_integrate` | Routes facts to pre-planned wiki pages; creates new stubs only if topic falls outside taxonomy |
| `/wiki_writer` | Called by `/wiki_init` or `/wiki_integrate` | Writes routed facts to wiki pages; checks for duplication and relevance; append-only logging |
| `/synthesiser` | Called by `/wiki_init` or manually | Reads Key evidence on wiki pages and writes Current understanding narratives; batch or single-page mode |
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

1. **Current understanding** — a synthesised narrative of the best current model. Written by synthesis agents, NOT by individual fact additions. Left as a placeholder until enough Key evidence accumulates.
2. **Key evidence** — bullet points with backlinks to supporting summaries. This is where individual paper findings land. Format: `- <Claim> ([Author Year](<relative path to summary>))`
3. **History of ideas** — a chronological narrative of how the field's understanding evolved: early models, key experiments that challenged them, and the intellectual path to the current model. Written by the synthesiser alongside Current understanding, drawing on publication years and `historical_context` annotations from fact_finder. Not a publication timeline — focuses on *why* thinking changed.
4. **Open questions** — unresolved issues flagged by the literature
5. **Related pages** — links to other wiki pages (cross-category links encouraged)

Wiki pages should link back to `raw/summaries/` and `raw/mds/` files so agents can query source material for more detail.

**Relative links**: calculate the correct relative path based on the wiki page's nesting depth. Pages at `wiki/<category>/<page>.md` use `../../raw/summaries/`. Pages at `wiki/<category>/<sub>/<page>.md` use `../../../raw/summaries/`. Cross-wiki links use relative paths between the two pages.

**Inconsistency markers**: the `/reviewer` agent may add `> [!INCONSISTENCY]` callout blocks to flag contradictions between papers. These are working flags — once resolved (through user interaction or new evidence), they are removed and the settled understanding becomes normal wiki content.

---

## Agent guidance

- **Before navigating the wiki**: read `index.md` first — it tells you what pages exist and their keywords. Only glob `wiki/` if `index.md` is insufficient.
- **Before acting**: read `log.md` to check what other agents have recently done and what is queued for wiki integration.
- **Do not hallucinate**: all wiki content must be grounded in summaries in `raw/summaries/`. If a claim cannot be traced to a summary, flag it.
- **When creating a wiki page**: add it to `index.md` immediately.
- **Filename mismatches**: `/make_summary` will auto-correct mismatched filenames and report them — trust its output filename over the input filename.
