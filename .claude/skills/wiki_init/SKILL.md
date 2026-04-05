---
name: wiki_init
description: One-time skill to bootstrap the wiki from all existing summaries in raw/summaries/. Runs taxonomy_planner → batched fact_finder (parallel) → router → wiki_writer → synthesiser → reviewer. Should only be run once on an empty wiki; use wiki_integrate for ongoing updates.
user-invocable: true
disable-model-invocation: true
argument-hint: []
allowed-tools: Read Glob Grep Write Bash Agent
model: sonnet
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
- router writes → `.pipeline/<stem>_routing.yaml`

Pass file paths (not raw YAML strings) as arguments to downstream skills. The `.pipeline/` directory can be cleaned up after a successful run.

## Pre-flight checks

1. Glob `raw/summaries/*.md` (excluding `raw/summaries/STATUS.md`). If none found, report and stop.
2. Read `raw/summaries/STATUS.md`. Any summaries listed under `integrated` will be skipped — do not reprocess them.
3. Check `index.md` — if the search index already has entries, warn the user:
   > **wiki_init: the wiki index is not empty. Running wiki_init again may create duplicate content.**
   > Proceed anyway? (If called programmatically, proceed.)
4. Compute the working set: all summaries found in step 1 minus those in `integrated` from step 2.
5. List the count and first few filenames before proceeding.

## Stage 0 — Taxonomy planning

Spawn an agent to invoke `taxonomy_planner` (model: `opus`). No arguments needed — it scans all summaries itself.

Wait for it to complete. Verify that `.pipeline/taxonomy.yaml` was created and that `index.md` now has wiki structure entries. If taxonomy planning fails, stop — the pipeline cannot proceed without a taxonomy.

This stage creates all wiki stub pages and populates `index.md`, so the router has a pre-planned structure to route into.

## Pipeline — batch processing

Process summaries in **batches of 20**. After each batch, checkpoint progress via STATUS.md so the run can be resumed if interrupted.

For each batch:

### Stage 1 — Extract facts in parallel (fact_finder)

Spawn **all fact_finder agents for the batch in parallel** — one agent per summary. These are independent: each reads a different summary and writes to a different `.pipeline/<stem>_facts.yaml` file with no shared state.

For each summary, spawn an agent to invoke `fact_finder`, passing the summary path as `$ARGUMENTS`. Tell the agent to write its YAML output to `.pipeline/<stem>_facts.yaml`.

After all agents in the batch return, collect the results:
- Parse each STATUS line.
- If `STATUS: failed` — log the failure to `log.md` and remove from the batch.
- If `STATUS: success` — continue to Stage 2.

### Stage 2 — Route facts (router) — sequential

Process routers **sequentially** within the batch. The router reads and may update `index.md`, so concurrent access must be avoided.

For each successful fact extraction, spawn an agent to invoke `router`, passing `.pipeline/<stem>_facts.yaml` as `$ARGUMENTS`.

Tell the agent to write its routing decisions to `.pipeline/<stem>_routing.yaml`.

**Important**: the router's output does not include `source_summary`, `source_title`, or `source_year`. Before passing routing decisions to wiki_writer, you must inject these fields from the fact_finder output. Read `.pipeline/<stem>_facts.yaml` to get `source_summary`, `source_title`, and `source_year`, then include them when constructing the wiki_writer input.

- Parse the returned STATUS line.
- If `STATUS: failed` — log and skip.

### Stage 3 — Write to wiki (wiki_writer)

For each routing decision with `action: route`, spawn an agent to invoke `wiki_writer`.

Construct the input for wiki_writer by combining:
- The routing decision entry (from router output)
- `source_summary`, `source_title`, `source_year` (from fact_finder output)

Write this combined payload to `.pipeline/<stem>_write_<fact_index>.yaml` and pass the file path as `$ARGUMENTS`.

**Parallelisation rule**: wiki_writer agents targeting **different wiki pages** may run in parallel. Group the routing decisions by target page path. Within each group (same target page), run sequentially to avoid write collisions. Across groups, run in parallel.

wiki_writer handles its own logging to `log.md` (append-only). Collect the written/skipped counts from each STATUS line.

### Stage 4 — Mark summary as integrated

After all facts from a summary have been processed:

1. Read `raw/summaries/STATUS.md` and add the summary to `integrated`:

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
Batch N complete. Processed M/total summaries. Continuing...
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
- fact_finder calls are parallelised within each batch (they are independent). Router and wiki_writer calls have sequential constraints due to shared state.
- If the run is interrupted, it can be safely resumed — STATUS.md tracks which summaries are already integrated, and wiki_writer's duplication check will skip already-written facts. The taxonomy planning and stub creation only need to run once (check if `.pipeline/taxonomy.yaml` exists to skip re-running).
- The synthesis pass runs on the opus model because writing coherent scientific narratives from multiple evidence sources requires strong reasoning and integration ability.
