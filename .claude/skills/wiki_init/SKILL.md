---
name: wiki_init
description: One-time skill to bootstrap the wiki from all existing summaries in raw/summaries/. Runs taxonomy_planner → batched fact_finder (parallel) → router → wiki_writer → synthesiser → reviewer. Should only be run once on an empty wiki; use wiki_integrate for ongoing updates.
user-invocable: true
disable-model-invocation: true
argument-hint: []
allowed-tools: Read Glob Grep Write Bash Agent
model: opus
---

# wiki_init

You are a pipeline orchestrator bootstrapping the wiki from scratch. You process every summary currently in `raw/summaries/` through the full wiki-building pipeline and finish with synthesis and review passes.

## How to invoke sub-skills

Throughout this pipeline, you invoke other skills by spawning agents. For each sub-skill invocation, use the Agent tool with a prompt structured like this:

```
Read the file .claude/skills/<skill_name>/SKILL.md. Follow every instruction in that file exactly. Use the following value as $ARGUMENTS: <value>
```

The spawned agent will read the skill instructions, execute them, and return its output (including YAML blocks and STATUS lines). You then parse that output to extract the structured data you need.

**Important**: when spawning agents, set the `model` parameter to match the model specified in the sub-skill's frontmatter:
- `taxonomy_planner` → model: `opus`
- `fact_finder` → model: `sonnet`
- `router` → model: `sonnet`
- `wiki_writer` → model: `sonnet`
- `synthesiser` → model: `opus`
- `reviewer` → model: `opus`

## Intermediate file convention

To avoid fragile YAML-as-string passing between agents, structured outputs are written to files in `.pipeline/`:

- taxonomy_planner writes → `.pipeline/taxonomy.yaml`
- fact_finder writes → `.pipeline/<stem>_facts.yaml`
- dedup manifest → `.pipeline/batch_<N>_dedup.yaml` (built by orchestrator after Stage 1)
- router writes → `.pipeline/<stem>_routing.yaml`

Pass file paths (not raw YAML strings) as arguments to downstream skills. The `.pipeline/` directory can be cleaned up after a successful run.

## Pre-flight checks

1. Glob `raw/summaries/*.md` (excluding `raw/summaries/STATUS.md`). If none found, report and stop.
2. Read `raw/summaries/STATUS.md`. Check both `integrated` entries and per-summary `stage` fields (see Checkpoint format below) to determine what work has already been completed.
3. Check `index.md` — if the search index already has entries, warn the user:
   > **wiki_init: the wiki index is not empty. Running wiki_init again may create duplicate content.**
   > Proceed anyway? (If called programmatically, proceed.)
4. Compute the working set: all summaries found in step 1 minus those fully `integrated` from step 2.
5. **Sort the working set by year (oldest first)**. Extract the year from each filename (the digits immediately after the author surname, e.g. `stachenfeld2017_...` → 2017). Foundational papers should be processed first so the wiki backbone forms before niche findings are added. Within the same year, sort alphabetically by author.
6. List the count, year range, and first few filenames before proceeding.

## Stage 0a — Build summary index

Before taxonomy planning, programmatically extract compact metadata from every summary in the working set into a single file. This avoids loading the full text of every summary into the taxonomy planner's context.

For each summary in the working set, read it and extract:
- `filename` — the summary filename (stem)
- `title` — from YAML frontmatter
- `year` — from YAML frontmatter
- `paper_type` — from YAML frontmatter (`empirical`, `computational`, `review`)
- `one_line_summary` — the content under `### One-line summary`
- `brain_regions` — the content under `### Brain regions & systems` (trim to first 2–3 lines if long)
- `computational_framework` — the first 1–2 sentences under `### Computational framework`
- `keywords` — the keywords list from `### Connections & keywords`

Write the collected metadata to `.pipeline/summary_index.yaml`:

```yaml
generated_at: <ISO 8601 UTC>
count: <N>
summaries:
  - filename: adams2018_attractor_schizophrenia
    title: "Computational Psychiatry..."
    year: 2018
    paper_type: computational
    one_line_summary: "Attractor network instability may explain..."
    brain_regions: "prefrontal cortex — proposed locus of attractor instability"
    computational_framework: "Attractor networks with Bayesian inference..."
    keywords: [attractor_networks, schizophrenia, prefrontal_cortex, bayesian_inference]
  - ...
```

**Parallelisation**: you can read multiple summaries in parallel to speed this up. The extraction is purely mechanical — no reasoning needed, just parsing sections from each file.

Validate the YAML output with the validation helper before proceeding.

## Stage 0b — Taxonomy planning

Spawn an agent to invoke `taxonomy_planner` (model: `opus`), passing `.pipeline/summary_index.yaml` as `$ARGUMENTS`.

The taxonomy planner reads this single compact file instead of scanning all summaries individually. Wait for it to complete. Verify that `.pipeline/taxonomy.yaml` was created and that `index.md` now has wiki structure entries. If taxonomy planning fails, stop — the pipeline cannot proceed without a taxonomy.

This stage creates all wiki stub pages and populates `index.md`, so the router has a pre-planned structure to route into.

## Checkpoint format (STATUS.md)

`raw/summaries/STATUS.md` tracks per-summary progress so crashed runs can resume without redoing work. The enhanced format is:

```yaml
integrated:
  - path: raw/summaries/<filename>.md
    integrated_at: <ISO 8601 UTC>

in_progress:
  - path: raw/summaries/<filename>.md
    stage: facts_done       # or: routed, written
    updated_at: <ISO 8601 UTC>
```

**Stage values**: `facts_done` → fact_finder completed, `routed` → router completed, `written` → wiki_writer completed. After `written`, move the entry from `in_progress` to `integrated`.

When resuming a crashed run:
- Summaries in `integrated` → skip entirely.
- Summaries with `stage: facts_done` → skip fact_finder, resume from routing. Verify `.pipeline/<stem>_facts.yaml` exists.
- Summaries with `stage: routed` → skip fact_finder and routing, resume from wiki_writer. Verify `.pipeline/<stem>_routing.yaml` exists.
- Summaries with `stage: written` → just needs the final move to `integrated`.
- If a checkpoint references a `.pipeline/` file that doesn't exist, reset that summary to the previous stage.

## YAML validation helper

After every `.pipeline/` file is written by a sub-skill, validate it before proceeding:

```bash
python3 -c "import yaml, sys; yaml.safe_load(open(sys.argv[1])); print('VALID')" .pipeline/<file>.yaml
```

If validation fails, log the error and **retry the sub-skill once**. If it fails again, log as a permanent failure and skip that summary.

## Pipeline — batch processing

Process summaries in **batches of 20**, sorted by year (oldest first, as determined in pre-flight). After each batch, checkpoint progress via STATUS.md so the run can be resumed if interrupted.

For each batch:

### Stage 1 — Extract facts in parallel (fact_finder)

Check each summary's checkpoint status. Skip any that already have `stage: facts_done` or later.

Spawn **all fact_finder agents for the batch in parallel** — one agent per summary. These are independent: each reads a different summary and writes to a different `.pipeline/<stem>_facts.yaml` file with no shared state.

For each summary, spawn an agent to invoke `fact_finder`, passing the summary path as `$ARGUMENTS`. Tell the agent to write its YAML output to `.pipeline/<stem>_facts.yaml`.

After all agents in the batch return, collect the results:
- **Validate** each `.pipeline/<stem>_facts.yaml` using the YAML validation helper. If invalid, retry the fact_finder once.
- Parse each STATUS line.
- If `STATUS: failed` — log the failure to `log.md` and remove from the batch.
- If `STATUS: success` — update STATUS.md: add entry to `in_progress` with `stage: facts_done`.

### Stage 1.5 — Dedup manifest

After all fact_finder calls in the batch complete, build a lightweight dedup manifest to flag near-duplicate claims before routing:

1. Read all successful `.pipeline/<stem>_facts.yaml` files from the batch.
2. Collect every `claim` string along with its `source_summary`.
3. Write `.pipeline/batch_<N>_dedup.yaml` with the following format:

```yaml
batch: <N>
claims:
  - claim: "<claim text>"
    source: "<stem>"
    topics: [<flattened list of all topic values>]
  - ...
```

4. Scan the list for **near-duplicate claims** — claims from different summaries that describe the same finding. Use your judgement: two claims are near-duplicates if they make the same mechanistic point, even if worded differently. Mark duplicates by adding a `duplicate_of: <stem of the earlier/stronger claim>` field.

5. Write the annotated manifest back. The router will read this manifest to skip routing claims already flagged as duplicates, saving wiki_writer from redundant work.

**Note**: this is a best-effort pass. wiki_writer still has its own duplication check as a safety net. The purpose here is to reduce wasted compute on obviously redundant claims.

### Stage 2 — Route facts (router) — batched

The router now accepts **multiple facts files in a single invocation**. Instead of spawning one router agent per summary, batch them.

Collect all successful `.pipeline/<stem>_facts.yaml` paths from this batch. Spawn **one router agent** per batch, passing all paths as space-separated `$ARGUMENTS`. Also tell the agent: "Read `.pipeline/batch_<N>_dedup.yaml` — for any claim marked `duplicate_of`, set `action: skip` with `skip_reason: duplicate_flagged_by_dedup`."

The router reads `index.md` and `taxonomy.yaml` once, then processes all facts files in sequence, writing a separate `.pipeline/<stem>_routing.yaml` for each.

**If the batch is large (>15 files)**, split into 2 router calls to avoid context overflow. Each sub-batch should still process multiple files.

After the router returns:
- **Validate** each `.pipeline/<stem>_routing.yaml` using the YAML validation helper.
- Parse each STATUS line.
- If any individual file failed, log and skip it.
- For successes, update STATUS.md: set `stage: routed`.

**Important**: the router's output does not include `source_summary`, `source_title`, or `source_year`. Before passing routing decisions to wiki_writer, you must inject these fields from the fact_finder output. Read `.pipeline/<stem>_facts.yaml` to get `source_summary`, `source_title`, and `source_year`, then include them when constructing the wiki_writer input.

### Stage 3 — Write to wiki (wiki_writer)

For each routing decision with `action: route`, spawn an agent to invoke `wiki_writer`.

Construct the input for wiki_writer by combining:
- The routing decision entry (from router output)
- `source_summary`, `source_title`, `source_year` (from fact_finder output)

Write this combined payload to `.pipeline/<stem>_write_<fact_index>.yaml` and pass the file path as `$ARGUMENTS`.

**Validate** each write payload YAML before passing to wiki_writer.

**Parallelisation rule**: wiki_writer agents targeting **different wiki pages** may run in parallel. Group the routing decisions by target page path. Within each group (same target page), run sequentially to avoid write collisions. Across groups, run in parallel.

wiki_writer handles its own logging to `log.md` (append-only). Collect the written/skipped counts from each STATUS line.

After all writes for a summary complete, update STATUS.md: set `stage: written`.

### Stage 4 — Mark summary as integrated

After all facts from a summary have been written (stage: written):

1. Read `raw/summaries/STATUS.md`. Move the summary from `in_progress` to `integrated`:

```yaml
integrated:
  - path: raw/summaries/<filename>.md
    integrated_at: <ISO 8601 UTC>
```

2. Append to `log.md` (use bash append, not read-then-rewrite):

```bash
echo '- timestamp: '"$(date -u +"%Y-%m-%dT%H:%M:%S")"'
  agent: wiki_init
  event: summary_integrated
  source_summary: raw/summaries/<filename>.md
  facts_extracted: <N>
  facts_routed: <N>
  facts_written: <N>
  facts_skipped: <N>' >> log.md
```

### End of batch

After each batch of 20 summaries, report progress:
```
Batch N complete. Processed M/total summaries (year range: YYYY–YYYY). Continuing...
```

## After all summaries

### Stage 5 — Synthesis pass

Spawn an agent to invoke `synthesiser` (model: `opus`), passing `batch` as `$ARGUMENTS`.

The synthesiser will find all wiki pages that have accumulated enough Key evidence (3+ bullets) and write Current understanding narratives for them. This is the critical step that transforms the wiki from an evidence dump into an actual knowledge base.

**Note**: the synthesiser processes pages in groups of 10 internally. For a large wiki, this will take time. Let it run to completion.

### Stage 6 — Reviewer pass

Spawn an agent to invoke `reviewer` (model: `opus`). Pass a timestamp from the start of this run as `$ARGUMENTS` so it reviews everything written during this session.

**Note**: the reviewer may need to work in batches too if many pages were modified. Tell the spawned agent to process wiki pages in groups of 20–30 if the total exceeds 30.

### Stage 7 — Cleanup and report

1. Optionally clean up `.pipeline/` temp files (or leave them for debugging).
2. Print a full summary:

```
wiki_init complete.
  Summaries processed: N
  Facts extracted: N total
  Wiki pages created: N (by taxonomy planner)
  Wiki pages updated: N (by wiki_writer)
  Facts written: N
  Facts skipped: N (duplicate: N, off-topic: N, low-value: N)
  Pages synthesised: N (Current understanding narratives written)
  Inconsistencies flagged: N

Wiki is ready. Run /wiki_integrate after each future /digest run.
```

## Notes

- This skill is designed to be run **once** on a cold wiki. For ongoing updates, use `/wiki_integrate` (which runs the same pipeline on a single new summary).
- **Parallelisation**: fact_finder calls are fully parallel within each batch. Router calls are batched (one call per batch of ~15–20 summaries). wiki_writer calls are parallel across different target pages, sequential within the same page.
- **Resumability**: STATUS.md tracks per-summary stage (`facts_done` → `routed` → `written` → `integrated`). If the run is interrupted, it resumes from each summary's last completed stage. The taxonomy planning and stub creation only need to run once (check if `.pipeline/taxonomy.yaml` exists to skip re-running).
- **Priority ordering**: summaries are processed oldest-first by publication year, so foundational papers form the wiki backbone before niche findings are added.
- **YAML validation**: every `.pipeline/` file is validated via `yaml.safe_load` before being passed to the next stage. Invalid files trigger one retry; persistent failures are logged and skipped.
- **Dedup manifest**: after fact extraction, a per-batch dedup pass flags near-duplicate claims from different papers. The router skips these, and wiki_writer's own duplication check provides a safety net.
- The synthesis pass runs on the opus model because writing coherent scientific narratives from multiple evidence sources requires strong reasoning and integration ability.
