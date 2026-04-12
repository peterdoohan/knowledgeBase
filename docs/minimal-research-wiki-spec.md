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
3. Deterministic parsing should wrap and validate LLM extraction, not pretend to replace it.
4. LLM judgement is used for semantic extraction and ambiguity resolution, but its outputs must be normalized and validated.
5. A page should exist only if it earns its place.
6. Fewer dense pages are better than many thin ones.

## Minimal repo shape

```text
raw/
  mds/
  summaries/

derived/
  alias_map.yaml
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

Current guaranteed frontmatter fields in the existing corpus:

```yaml
source_file: akam2021_anterior_cingulate_model.md
title: "The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection"
authors: Thomas Akam, Ines Rodrigues-Vaz, Ivo Marcelo, Xiangyu Zhang, Michael Pereira, Rodrigo Freire Oliveira, Peter Dayan, Rui M. Costa
year: 2021
journal: Neuron
paper_type: empirical
contribution_type: empirical
```

Target normalized frontmatter after Stage 1:

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
- fast lookup layer for downstream tasks
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
    key_citations:
      - daw2011_model_based_striatal_prediction
      - alexander2011_action_outcome_predictor
    open_question_count: 6
    summary_path: raw/summaries/akam2021_anterior_cingulate_model.md
    summary_quality: high
```

Notes:
- this file should stay compact and diffable
- prose findings and open questions remain in the summaries themselves
- `key_citations` should only include in-corpus IDs when match confidence is high

### 2. `derived/alias_map.yaml`

Purpose:
- canonicalize regions, tasks, methods, frameworks, and common abbreviations
- prevent fragmented terms in `paper_index.yaml` and topic generation

Schema:

```yaml
brain_regions:
  PFC: prefrontal_cortex
  prefrontal cortex: prefrontal_cortex
  mPFC: medial_prefrontal_cortex
  ACC: anterior_cingulate_cortex
tasks:
  two-step task: two_step_task
  2-step task: two_step_task
methods:
  calcium imaging: calcium_imaging
  miniscope imaging: calcium_imaging
frameworks:
  model-based reinforcement learning: model_based_rl
  model-free reinforcement learning: model_free_rl
```

Notes:
- this is the replacement for the old `taxonomy.yaml` alias layer
- the alias map should be versioned and expanded incrementally

### 3. `derived/citation_edges.yaml`

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

Citation extraction strategy must handle two formats:

1. structured `Key citations`
- preferred source
- parse explicit `Author (Year)` mentions and map to `paper_id`

2. unstructured mentions in summary body
- fallback source
- scan `Background & motivation`, `Computational framework`, `Prevailing model`, and explicit `Key citations` prose
- only emit edges when author-year match confidence is high

Do not treat flat `Connections & keywords` strings as citations.

### 4. `derived/topic_candidates.yaml`

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

This file should be produced from a defined heuristic:

1. normalize all extracted terms through `alias_map.yaml`
2. compute term frequencies across:
- `brain_regions`
- `tasks`
- `methods`
- `frameworks`
- `keywords`
3. create initial topic seeds from terms appearing in at least 3 papers
4. merge near-synonyms if:
- they share a canonical alias, or
- Jaccard overlap of supporting papers is `>= 0.6`
5. merge topic seeds into a single candidate if:
- at least 50 percent of their supporting papers overlap, and
- they are not clearly parent/child concepts
6. use citation data only to rank and stabilize topics, not to define boundaries
7. keep candidate topics broad enough to support synthesis, not mere indexing

It should not yet decide final inclusion.

### 5. `derived/judge_scores.yaml`

Purpose:
- semantic gating layer
- decide whether a paper belongs in a topic
- decide whether a topic deserves a page

Schema:

```yaml
generated_at: 2026-04-12T13:20:00Z
paper_topic_scores:
  - paper_id: ambrose2016_reverse_replay_hippocampal
    topic_id: hippocampal_replay
    topic_fit: 5
    evidence_strength: 5
    foundationality: 4
    notes: "Core empirical paper establishing reward sensitivity of reverse replay."
paper_pair_disagreements:
  - topic_id: hippocampal_replay
    paper_a: ambrose2016_reverse_replay_hippocampal
    paper_b: gillespie2021_replay_past_experiences
    disagreement: true
    disagreement_type: interpretive
    confidence: 4
    fault_line: "planning vs memory-maintenance function of replay"
    notes: "Both are relevant to replay function but support different interpretations."
```

Score definitions:
- `topic_fit`
  - `0`: irrelevant
  - `1`: weak mention only
  - `2`: peripheral relevance
  - `3`: relevant but not core
  - `4`: clearly belongs
  - `5`: core paper for topic
- `evidence_strength`
  - strength of evidence for the claims most relevant to the topic
  - for review papers this means strength of synthesis and field coverage, not new empirical evidence
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
- field extraction in Stage 1 normalization
- paper-to-topic fit
- page creation decisions
- contradiction detection
- foundational-paper ranking

Do not use the judge for:
- author/year parsing
- section extraction
- validation of already-extracted canonical IDs

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
- `paper_pair_disagreements` identifies at least 2 high-confidence disagreements within the topic
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
- structured `Key citations` block when recoverable
- `paper_id` added explicitly to frontmatter

Implementation style:
- LLM extraction is the primary path
- deterministic parser validates structure and rejects malformed outputs
- normalization dictionaries from `alias_map.yaml` canonicalize extracted values

Stage 1 should be honest about what is semantic:
- species extraction
- task extraction
- method extraction
- brain-region extraction
- framework extraction
- distinction between keyword vs citation

These are not deterministic today. The right design is:
1. parse existing frontmatter and section boundaries deterministically
2. run an LLM extraction pass over targeted sections
3. normalize outputs through `alias_map.yaml`
4. validate against allowed schemas and write back only valid fields

### Stage 2. Paper index build

Input:
- normalized summaries

Output:
- `derived/paper_index.yaml`

Implementation style:
- deterministic assembly from normalized summaries
- no new semantic extraction here
- compact metadata only; keep prose in source summaries

### Stage 3. Citation edge extraction

Input:
- summaries with `Key citations`
- paper IDs from `paper_index.yaml`

Output:
- `derived/citation_edges.yaml`

Implementation style:
- prefer structured `Key citations`
- fallback to author-year matching in body text
- explicit alias map for common ambiguous names
- never infer citations from keyword lists alone

### Stage 4. Topic candidate generation

Input:
- `paper_index.yaml`
- `citation_edges.yaml`

Output:
- `derived/topic_candidates.yaml`

Implementation style:
- canonical term aggregation
- thresholded seed creation
- explicit merge heuristics
- citation-centrality ranking only as a secondary signal

### Stage 5. Judge pass

Input:
- topic candidates
- paper summaries or extracted metadata

Output:
- `derived/judge_scores.yaml`

Implementation style:
- one paper-topic judgement unit per record
- one paper-pair disagreement unit for shortlisted papers within a topic
- single judge by default
- optional second judge for disputed cases

### Stage 5.5. Debate discovery

Input:
- top papers per topic from `judge_scores.yaml`

Output:
- debate candidates embedded in `judge_scores.yaml` or emitted to a separate report

Implementation style:
- for each topic, compare only shortlisted papers with `topic_fit >= 4`
- run pairwise disagreement queries on the top 5 to 10 papers, not the full cross product
- cluster disagreements by shared fault line
- only promote to a debate page when the disagreement is substantive

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

## Existing wiki migration

The current repo already has a large legacy wiki. Do not mix the old and new structures.

Migration rule:
- move the existing tree to `wiki/_legacy/`
- keep it readable but out of the active generation path
- do not delete it initially
- do not mine it automatically for synthesis content

The active wiki for the new pipeline should live only in:
- `wiki/topics/`
- `wiki/debates/`
- `wiki/indices/`

Legacy content can be consulted manually when useful, but it is not a source of truth.

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

## Checkpointing and recovery

All stages should be idempotent and restartable.

Minimum requirement:
- each derived file should be safely regenerable
- partial runs should write to a temporary file and then atomically replace the target

Recommended checkpoint file:

```yaml
generated_at: 2026-04-12T13:30:00Z
papers:
  akam2021_anterior_cingulate_model:
    normalized: true
    indexed: true
    citations_done: true
    topics_done: true
    judged: true
```

Rules:
- Stage 1 and Stage 2 should support per-paper regeneration
- Stage 3 should support per-paper citation recomputation
- Stage 5 should support scoring only impacted paper-topic pairs
- re-running a completed stage should be safe

## Non-goals

Do not do these initially:
- full ontology generation
- region/behaviour/framework pages for every concept
- multi-agent pipelines with many intermediate YAML handoffs
- three-judge consensus for all steps
- synthesis pages with placeholder sections

## Practical implementation order

1. build summary parser
2. define `alias_map.yaml`
3. implement LLM-led normalization with deterministic validation
4. generate `paper_index.yaml`
5. generate `citation_edges.yaml`
6. generate `topic_candidates.yaml`
7. implement judge pass
8. generate first topic pages
9. implement lint

## Success criteria

The system is working when:
- every topic page is backed by clearly relevant papers
- topic pages are dense and useful, not thin and placeholder-heavy
- foundational papers can be found quickly
- debate pages capture real conflicts
- new papers can be integrated incrementally
- the wiki is small enough that a human can still trust it
