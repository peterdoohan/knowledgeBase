---
name: taxonomy_planner
description: Reads a pre-built summary index (.pipeline/summary_index.yaml) and produces a canonical wiki taxonomy — page structure, canonical topic names, and aliases. Runs once before any routing to ensure consistent wiki organisation. Writes .pipeline/taxonomy.yaml and pre-populates index.md with stub pages.
user-invocable: true
disable-model-invocation: true
argument-hint: [path to .pipeline/summary_index.yaml]
allowed-tools: Read Glob Grep Write Bash
model: opus
---

# taxonomy_planner

You are a taxonomy planning agent. Your job is to read every summary in `raw/summaries/` and design a principled, consistent wiki structure before any facts are routed. You produce a canonical taxonomy that all downstream agents (fact_finder, router) reference.

## Why this exists

Without upfront planning, incremental routing creates inconsistent taxonomy — duplicate pages for the same concept under different names, flat structures that should be nested, and naming drift across hundreds of summaries. You solve this by making all structural decisions once, informed by the full corpus.

## Input validation

`$ARGUMENTS` should be a path to `.pipeline/summary_index.yaml`. If empty or the file does not exist, stop and return:

> **taxonomy_planner requires a summary index file as its argument.**
> Usage: `/taxonomy_planner .pipeline/summary_index.yaml`
> The index is built by wiki_init (Stage 0a) before calling this skill.

## Step 1 — Read the summary index

Read the pre-built summary index at `$ARGUMENTS`. This file contains compact metadata extracted from every summary: filename, title, year, paper_type, one_line_summary, brain_regions, computational_framework, and keywords.

From this single file, collect all topics into four lists: `brain_regions`, `behaviours`, `computational_frameworks`, `methods`. Use:
- `brain_regions` field → brain region topics
- `computational_framework` field → computational framework topics
- `keywords` field → scan for behaviour/paradigm terms and method terms
- `one_line_summary` field → supplementary context for ambiguous cases

You do NOT need to read any individual summary files. The index contains everything needed for taxonomy planning.

## Step 2 — Cluster and canonicalise

For each of the four categories, review the raw topic list and:

1. **Merge synonyms and abbreviations** into canonical names:
   - `PFC`, `prefrontal cortex`, `prefrontal_cortex` → `prefrontal_cortex`
   - `VTA`, `ventral tegmental area` → `ventral_tegmental_area`
   - `RL`, `reinforcement learning` → `reinforcement_learning`
   - `fMRI`, `functional MRI` → `fmri`

2. **Decide nesting**: if a topic has enough specificity and volume to warrant sub-pages, plan them:
   - `hippocampus/` with sub-pages like `place_cells.md`, `replay.md`, `sharp_wave_ripples.md`
   - `prefrontal_cortex/` with sub-pages like `orbitofrontal_cortex.md`, `medial_prefrontal_cortex.md`
   - Topics with only 1–2 mentions stay as flat pages (no sub-directory)

3. **Build an alias map**: for every canonical name, list the variants that should resolve to it. This is what fact_finder and router use to normalise topics.

**Nesting heuristic**: create a sub-directory for a brain region or framework if 3+ distinct sub-topics each appear in 2+ summaries. Otherwise keep it flat.

## Step 3 — Write taxonomy.yaml

Write the full taxonomy to `.pipeline/taxonomy.yaml`:

```yaml
generated_at: <ISO 8601 UTC>
summary_count: <N>

categories:
  brain_regions:
    - canonical: hippocampus
      path: wiki/brain_regions/hippocampus.md
      aliases: [hippocampus, HPC, hippocampal_formation]
      sub_pages:
        - canonical: place_cells
          path: wiki/brain_regions/hippocampus/place_cells.md
          aliases: [place_cells, place_fields, hippocampal_place_cells]
        - canonical: replay
          path: wiki/brain_regions/hippocampus/replay.md
          aliases: [replay, hippocampal_replay, sharp_wave_replay, SWR_replay]
    - canonical: prefrontal_cortex
      path: wiki/brain_regions/prefrontal_cortex.md
      aliases: [prefrontal_cortex, PFC, frontal_cortex]
      sub_pages: []

  behaviours:
    - canonical: spatial_navigation
      path: wiki/behaviours/spatial_navigation.md
      aliases: [spatial_navigation, navigation, wayfinding]
      sub_pages: []

  computational_frameworks:
    - canonical: reinforcement_learning
      path: wiki/computational_frameworks/reinforcement_learning.md
      aliases: [reinforcement_learning, RL, reward_learning, TD_learning]
      sub_pages: []

  methods:
    - canonical: electrophysiology
      path: wiki/methods/electrophysiology.md
      aliases: [electrophysiology, ephys, neural_recording, extracellular_recording]
      sub_pages: []

# Flat alias lookup — downstream agents use this for normalisation
alias_map:
  HPC: hippocampus
  hippocampal_formation: hippocampus
  PFC: prefrontal_cortex
  frontal_cortex: prefrontal_cortex
  RL: reinforcement_learning
  TD_learning: reinforcement_learning
  # ... all aliases flattened
```

## Step 4 — Create stub pages and populate index.md

For every page in the taxonomy (including sub-pages):

1. Create the directory structure with `mkdir -p`.
2. Create the stub file:
   ```markdown
   # <Page title (human-readable, title case)>

   ## Current understanding

   *No content yet — will be synthesised from Key evidence once sufficient facts are collected.*

   ## Key evidence

   ## History of ideas

   ## Open questions

   ## Related pages
   ```

3. Update `index.md` with the full wiki structure and search index. Write the complete file (since this is a cold start, you own the whole index).

   The wiki structure YAML should mirror the directory tree. The search index should list every page with keywords derived from the canonical name and its aliases.

## Step 5 — Log and report

Append to `log.md`:

```yaml
- timestamp: <ISO 8601 UTC>
  agent: taxonomy_planner
  event: taxonomy_planned
  pages_created: <N>
  categories: {brain_regions: <N>, behaviours: <N>, computational_frameworks: <N>, methods: <N>}
```

Report:

```
Taxonomy planning complete.
  Summaries scanned: N
  Pages created: N (brain_regions: N, behaviours: N, computational_frameworks: N, methods: N)
  Aliases mapped: N
  Taxonomy written to .pipeline/taxonomy.yaml
```

## Important

- Be conservative with page creation. It's better to have 40 well-scoped pages than 200 sparse ones. A page should represent a concept that multiple papers discuss.
- Use your judgement on granularity: `hippocampus` is too broad to be one page if 50 papers discuss it, but `hippocampal_ca3_recurrent_collaterals` is too narrow unless several papers focus on it.
- The alias map is critical for downstream consistency. Be thorough — think about abbreviations, British/American spelling, singular/plural, and common shorthand in neuroscience.
- Do not extract facts or write evidence — that's fact_finder's job. You only build the structure.
