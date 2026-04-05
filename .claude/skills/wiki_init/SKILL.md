---
name: wiki_init
description: One-time skill to bootstrap the wiki from all existing summaries in raw/summaries/. Runs fact_finder → router → wiki_writer for each summary, then runs the reviewer. Should only be run once on an empty wiki; use wiki_integrate for ongoing updates.
user-invocable: true
disable-model-invocation: true
argument-hint: []
allowed-tools: Read Glob Grep Write Bash Agent
model: haiku
---

# wiki_init

You are a pipeline orchestrator bootstrapping the wiki from scratch. You process every summary currently in `raw/summaries/` through the full wiki-building pipeline and finish with a reviewer pass.

## Pre-flight checks

1. Glob `raw/summaries/*.md` (excluding `raw/summaries/STATUS.md`). If none found, report and stop.
2. Read `raw/summaries/STATUS.md`. Any summaries already listed under `integrated` will be skipped — do not reprocess them.
3. Check `index.md` — if the search index already has entries, warn the user:
   > **wiki_init: the wiki index is not empty. Running wiki_init again may create duplicate content.**
   > Proceed anyway? (If called programmatically, proceed.)
4. List the summaries you will process (pending minus already integrated) and the count before proceeding.

## Pipeline

Process summaries one at a time. For each `raw/summaries/<filename>.md`:

### Stage 1 — Extract facts (fact_finder)

Use the Agent tool to invoke `fact_finder`, passing the summary path.

- Parse the returned YAML block to get the facts payload.
- If `STATUS: failed` — log the failure to `log.md` and skip to the next summary.

### Stage 2 — Route facts (router)

Pass the facts payload to the Agent tool to invoke `router`.

- Parse the returned routing decisions YAML.
- If `STATUS: failed` — log and skip.

### Stage 3 — Write to wiki (wiki_writer)

For each routing decision with `action: route`, use the Agent tool to invoke `wiki_writer`, passing the individual routing decision.

- wiki_writer handles its own logging to `log.md`.
- Collect the written/skipped counts.

### Stage 4 — Update STATUS.md and log.md

After all facts from a summary have been successfully processed:

1. Read `raw/summaries/STATUS.md` and move the summary from `pending` to `integrated`, adding `integrated_at`:

```yaml
integrated:
  - path: raw/summaries/<filename>.md
    integrated_at: <ISO 8601 UTC>
```

2. Append to `log.md`:

```yaml
- timestamp: <ISO 8601 UTC>
  agent: wiki_init
  event: summary_integrated
  source_summary: raw/summaries/<filename>.md
  facts_extracted: <N>
  facts_routed: <N>
  facts_written: <N>
  facts_skipped: <N>
```

Get timestamp with: `date -u +"%Y-%m-%dT%H:%M:%S"`

## After all summaries

### Stage 5 — Reviewer pass

Use the Agent tool to invoke `reviewer` with the current UTC time minus the duration of this run (so it reviews everything written during this session).

### Stage 6 — Final report

Print a full summary:

```
wiki_init complete.
  Summaries processed: N
  Facts extracted: N total
  Wiki pages created: N
  Wiki pages updated: N
  Facts written: N
  Facts skipped: N (duplicate: N, off-topic: N, low-value: N)
  Inconsistencies flagged: N

Wiki is ready. Run /wiki_integrate after each future /digest run.
```

## Notes

- This skill is designed to be run **once** on a cold wiki. For ongoing updates, use `/wiki_integrate` (which runs the same pipeline on a single new summary).
- Processing may take a long time for large summary collections. The pipeline is intentionally sequential (not parallel) to avoid routing conflicts and wiki write collisions.
- If the run is interrupted, it can be safely resumed — wiki_writer's duplication check will skip already-written facts.
