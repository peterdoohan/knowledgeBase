# Minimal Research Wiki Spec

## Goal

Build a high-quality research wiki from `raw/mds/` and `raw/summaries/` without recreating the current overengineered ontology pipeline.

The wiki should be:
- grounded in the summaries
- easy to maintain incrementally
- useful for synthesis and querying
- small enough that quality stays high

## Design principles

1. `raw/` is immutable.
2. `raw/summaries/` is the atomic knowledge unit.
3. Deterministic extraction comes before LLM judgement.
4. LLM judgement is used only where semantic ambiguity matters.
5. A page should exist only if it earns its place.
6. Fewer dense pages are better than many thin ones.

## Minimal repo shape

```text
raw/
  mds/
  summaries/

derived/
  paper_index.yaml
  citation_edges.yaml
  topic_candidates.yaml
  judge_scores.yaml
  lint_report.yaml

wiki/
  topics/
  debates/
  indices/
```

## Source of truth

### `raw/mds/`

Use as the full-text markdown source.

Purpose:
- fallback when a summary is incomplete
- source for future re-summarisation
- source for image/table/manual extraction if needed

Do not route facts directly from `raw/mds/` into the wiki.

### `raw/summaries/`

Use as the canonical paper notes.

Every wiki claim must trace back to one or more files here.

## Required summary contract

Every summary should keep this section structure:

- `One-line summary`
- `Background & motivation`
- `Methods`
- `Key findings`
- `Computational framework`
- `Prevailing model of the system under study`
- `What this paper contributes`
- `Brain regions & systems`
- `Mechanistic insight`
- `Limitations & open questions`
- `Connections & keywords`
- `Key citations` if available

Required frontmatter fields:

```yaml
paper_id: akam2021_anterior_cingulate_model
title: "The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection"
authors:
  - "Thomas Akam"
  - "Ines Rodrigues-Vaz"
year: 2021
journal: Neuron
paper_type: empirical
contribution_type: empirical
```

Preferred additional frontmatter fields after normalisation:

```yaml
species: [mouse]
tasks: [two_step_task]
methods: [calcium_imaging, optogenetics, logistic_regression]
brain_regions: [anterior_cingulate_cortex, dorsomedial_striatum]
frameworks: [model_based_rl, model_free_rl, reinforcement_learning]
keywords: [state_prediction, state_prediction_error, action_outcome_learning]
```

## Derived artefacts

### 1. `derived/paper_index.yaml`

Purpose:
- one structured registry of the whole corpus
- deterministic lookup layer for downstream tasks
- avoid repeatedly reparsing summaries

Schema:

```yaml
generated_at: 2026-04-12T13:00:00Z
paper_count: 496
papers:
  - paper_id: akam2021_anterior_cingulate_model
    path: raw/summaries/akam2021_anterior_cingulate_model.md
    title: "The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection"
    year: 2021
    authors:
      - "Thomas Akam"
      - "Ines Rodrigues-Vaz"
    journal: Neuron
    paper_type: empirical
    contribution_type: empirical
    species: [mouse]
    tasks: [two_step_task]
    methods: [calcium_imaging, optogenetics]
    brain_regions: [anterior_cingulate_cortex, dorsomedial_striatum]
    frameworks: [model_based_rl, model_free_rl, reinforcement_learning]
    keywords: [state_prediction, goal_directed_behaviour]
    one_line_summary: "ACC encodes action-state predictions and is causally necessary for model-based control."
    key_findings:
      - "ACC encodes predicted second-step states."
      - "ACC inhibition selectively weakens transition-based updating."
    open_questions:
      - "Whether ACC signals state prediction error at transition time or post-outcome remains unresolved."
    key_citations:
      - daw2011_model_based_striatal_prediction
      - alexander2011_action_outcome_predictor
    summary_quality: high
```

Notes:
- this file should be produced mostly by parsing and constrained extraction
- `key_citations` should only include in-corpus IDs when match confidence is high

### 2. `derived/citation_edges.yaml`

Purpose:
- build the paper graph
- support foundational-paper detection
- support backlinking between summaries and topic pages

Minimal schema:

```yaml
generated_at: 2026-04-12T13:05:00Z
edges:
  - source: akam2021_anterior_cingulate_model
    target: daw2011_model_based_striatal_prediction
    type: cites
    confidence: high
    evidence: "Matched from Key citations section"
```

Only required edge type initially:
- `cites`

Optional later:
- `extends`
- `contradicts`
- `same_topic`

Do not start with a rich graph ontology.

### 3. `derived/topic_candidates.yaml`

Purpose:
- define candidate wiki pages before writing them
- stop the model from inventing pages ad hoc

Schema:

```yaml
generated_at: 2026-04-12T13:10:00Z
topics:
  - topic_id: hippocampal_replay
    label: "Hippocampal Replay"
    seed_terms: [hippocampal_replay, reverse_replay, forward_replay, sharp_wave_ripples]
    candidate_papers:
      - ambrose2016_reverse_replay_hippocampal
      - jadhav2016_hippocampal_prefrontal_swr
      - pfeiffer2017_hippocampal_replay_memory
    source_signals:
      keywords: 18
      citation_hits: 7
      summary_hits: 21
```

This file should be produced from:
- keyword frequency
- normalized metadata overlap
- citation centrality

It should not yet decide final inclusion.

### 4. `derived/judge_scores.yaml`

Purpose:
- semantic gating layer
- decide whether a paper belongs in a topic
- decide whether a topic deserves a page

Schema:

```yaml
generated_at: 2026-04-12T13:20:00Z
judgements:
  - paper_id: ambrose2016_reverse_replay_hippocampal
    topic_id: hippocampal_replay
    topic_fit: 5
    centrality_to_topic: 5
    evidence_strength: 5
    foundationality: 4
    contradiction_flag: false
    notes: "Core empirical paper establishing reward sensitivity of reverse replay."
```

Score definitions:
- `topic_fit`
  - `0`: irrelevant
  - `1`: weak mention only
  - `2`: peripheral relevance
  - `3`: relevant but not central
  - `4`: clearly belongs
  - `5`: core paper for topic
- `centrality_to_topic`
  - how central the paper is to the topic page
- `evidence_strength`
  - strength of evidence for the claims most relevant to the topic
- `foundationality`
  - how much the paper functions as a landmark / canonical reference

Use a single judge by default.

Use a second judge only for:
- contradiction detection
- high-value debate pages
- papers near a hard threshold

## LLM judge policy

Use the LLM judge only where deterministic rules are weak.

Use the judge for:
- paper-to-topic fit
- page creation decisions
- contradiction detection
- foundational-paper ranking

Do not use the judge for:
- author/year parsing
- section extraction
- keyword extraction from explicit lists
- citation parsing from clearly formatted `Key citations`

## Page creation rules

Create a topic page only if one of the following is true:

1. at least 3 papers have:
- `topic_fit >= 4`
- `evidence_strength >= 3`

2. one paper has:
- `topic_fit = 5`
- `foundationality >= 4`

and at least 2 additional papers have:
- `topic_fit >= 3`

If neither rule is met, keep the topic in `topic_candidates.yaml` but do not create a page.

Create a debate page only if:
- at least 2 clusters of papers exist
- the judge marks real interpretive tension, not mere task/species variation

## Wiki page types

Only three page types should exist initially.

### 1. Topic pages

Path:
- `wiki/topics/<topic_id>.md`

Template:

```md
# <Topic Label>

## Current view

Short synthesis of what the field currently supports.

## Strongest evidence

- <claim> ([Paper Year](../../raw/summaries/<paper>.md))

## Landmark papers

- [Paper Year](../../raw/summaries/<paper>.md): one-line reason

## Open questions

- ...

## Related topics

- [Other topic](../topics/<other>.md)
```

### 2. Debate pages

Path:
- `wiki/debates/<debate_id>.md`

Template:

```md
# <Debate Label>

## The disagreement

One paragraph stating the conflict precisely.

## Position A

- <paper-backed claim>

## Position B

- <paper-backed claim>

## Likely sources of disagreement

- task differences
- species differences
- analysis differences

## What would resolve it

- ...
```

### 3. Index pages

Start with:
- `wiki/indices/index.md`
- `wiki/indices/foundational-papers.md`
- `wiki/indices/debates.md`

Do not create many index pages up front.

## Minimal pipeline

### Stage 1. Summary normalisation

Input:
- `raw/summaries/*.md`

Output:
- standardized frontmatter
- consistent section headers
- normalized names for tasks, methods, brain regions, frameworks

Implementation style:
- deterministic parser plus lookup tables

### Stage 2. Paper index build

Input:
- normalized summaries

Output:
- `derived/paper_index.yaml`

Implementation style:
- mostly deterministic extraction
- constrained LLM fallback only for missing structured fields

### Stage 3. Citation edge extraction

Input:
- summaries with `Key citations`
- paper IDs from `paper_index.yaml`

Output:
- `derived/citation_edges.yaml`

Implementation style:
- author-year matching
- explicit alias map for common ambiguous names

### Stage 4. Topic candidate generation

Input:
- `paper_index.yaml`
- `citation_edges.yaml`

Output:
- `derived/topic_candidates.yaml`

Implementation style:
- keyword aggregation
- metadata clustering
- citation-centrality heuristics

### Stage 5. Judge pass

Input:
- topic candidates
- paper summaries or extracted metadata

Output:
- `derived/judge_scores.yaml`

Implementation style:
- one paper-topic judgement unit per record
- single judge by default
- optional second judge for disputed cases

### Stage 6. Page creation

Input:
- topic candidates
- judge scores

Output:
- `wiki/topics/*.md`
- `wiki/debates/*.md`
- `wiki/indices/*.md`

Implementation style:
- only create pages that pass thresholds
- do not create stubs with placeholders

### Stage 7. Lint

Input:
- all derived artefacts and wiki pages

Output:
- `derived/lint_report.yaml`

Checks:
- broken links
- unsupported claims
- duplicate bullets
- orphan pages
- pages with too few core papers
- summaries missing required fields

## Incremental update workflow

When a new paper is added:

1. add to `raw/mds/`
2. produce or update `raw/summaries/<paper>.md`
3. re-run paper index build for that paper
4. re-run citation extraction for that paper
5. update topic candidates
6. judge only impacted topic-paper pairs
7. update only affected wiki pages
8. run lint

Do not rebuild the whole wiki unless the schema changes.

## Non-goals

Do not do these initially:
- full ontology generation
- region/behaviour/framework pages for every concept
- multi-agent pipelines with many intermediate YAML handoffs
- three-judge consensus for all steps
- synthesis pages with placeholder sections

## Practical implementation order

1. build summary parser
2. define normalization dictionaries
3. generate `paper_index.yaml`
4. generate `citation_edges.yaml`
5. generate `topic_candidates.yaml`
6. implement judge pass
7. generate first topic pages
8. implement lint

## Success criteria

The system is working when:
- every topic page is backed by clearly relevant papers
- topic pages are dense and useful, not thin and placeholder-heavy
- foundational papers can be found quickly
- debate pages capture real conflicts
- new papers can be integrated incrementally
- the wiki is small enough that a human can still trust it
