---
name: make_summary
description: Summarizes an academic paper that has been converted to a .md file. Produces a structured summary for downstream knowledge base agents to consume. Manual invocation only.
user-invocable: true
disable-model-invocation: true
argument-hint: [filename or path to .md paper]
allowed-tools: Read Glob Grep Write Bash
---

# make_summary

You are an agent operating inside a knowledge base pipeline. Your role is to read a single academic paper (already converted from PDF to Markdown) and produce a structured summary. This summary will NOT be read by humans first — it will be consumed directly by downstream agents building a structured knowledge base. Your output must be precise, consistent, and machine-friendly, while remaining semantically rich enough for agents to reason over.

## Input validation

If `$ARGUMENTS` is empty, or does not end in `.md`, stop immediately and return the following message to the user without doing anything else:

> **make_summary requires a .md file as its argument.**
> Usage: `/make_summary raw/mds/filename.md` or `/make_summary filename.md`

## Repo context

- Raw paper Markdown files live in: `raw/mds/`
- Summaries you produce should be saved to: `raw/summaries/`
- Filename convention: source filename is preserved, e.g. `adams2018_attractor_schizophrenia.md` → `raw/summaries/adams2018_attractor_schizophrenia.md`
- If a bare filename is given (no path), assume it lives in `raw/mds/`

## Filename mismatch check

After reading the paper, check whether the source filename plausibly matches the actual paper content (author surname, year, and a keyword from the title). Mismatches are common in this repo due to PDF conversion errors.

- **If the filename matches**: proceed normally, saving to `raw/summaries/<source_filename>`.
- **If the filename does not match**: do not stop or ask the user. Instead, derive a corrected filename from the actual paper content using the same naming convention — `firstauthorsurname+year_keyword1_keyword2.md` (lowercase, underscores, no spaces). Then:
  1. Rename the source file using an absolute path: `mv /Users/vyp730/Projects/knowledgeBase/raw/mds/<original_filename> /Users/vyp730/Projects/knowledgeBase/raw/mds/<corrected_filename>` (use Bash).
  2. Save the summary to `raw/summaries/<corrected_filename>`.
  3. Set `source_file` in the YAML frontmatter to the **corrected** filename (since the source file has now been renamed).
  4. After writing, note the mismatch to the user: state the original filename, the corrected filename, and the actual paper title.

## Reading large files

Papers in this repo are often long. Use the following strategy:

- Attempt to read the full file with no `limit` parameter first.
- If the Read tool returns a token-limit error, read the file in chunks using `offset` and `limit` (use `limit: 150` lines per chunk). Work through the entire file from offset 0 until you reach the end (when a chunk returns fewer lines than the limit, or an empty result).
- Do not begin writing until you have read all chunks.

## Before writing

Read the full paper before writing anything. Note whether the paper is:
- **Empirical primary study** — original data collection and analysis
- **Computational/modelling study** — model development and/or simulation, may include empirical validation
- **Review or meta-analysis** — synthesis of existing literature

This classification affects how you fill in several sections below.

---

## Output format

Write the summary as a Markdown file. Use the exact section headings below. Replace all `<...>` placeholder text with your content. Do not include the `<...>` markers in the output.

---

Frontmatter (YAML, at the top of the file):

```yaml
---
source_file: <original filename>
title: <full paper title>
authors: <comma-separated author list>
year: <publication year>
journal: <journal or venue name>
paper_type: <empirical | computational | review>
contribution_type: <methodological | empirical | theoretical | review>
---
```

`contribution_type` definitions (do not include these lines in the output YAML):
- `methodological` — primary contribution is a new task, analysis technique, or critique of existing methods
- `empirical` — primary contribution is new experimental data or findings about a system
- `theoretical` — primary contribution is a new model, framework, or conceptual account
- `review` — primary contribution is synthesis of existing literature

---

### One-line summary

A single sentence capturing the core claim or finding.

---

### Background & motivation

2–4 sentences on the problem being addressed and why it matters. What gap does this paper fill?

---

### Methods

Concise description of the approach. Use bullet points.

- For **empirical** papers: task design, subject population, key measurements, analysis approach.
- For **computational** papers: model architecture, key variables, datasets used for validation.
- For **reviews**: scope of literature covered, inclusion criteria, synthesis method (narrative, meta-analytic, etc.).

---

### Key findings

The main results. Use bullet points. Be specific — include numbers, effect sizes, or model comparisons where relevant.

For **reviews**: summarise the major conclusions drawn across the literature, noting areas of consensus and disagreement.

---

### Computational framework

What computational lens or framework does the paper use? Examples: Bayesian inference, reinforcement learning, dynamical systems, predictive coding, drift-diffusion modelling, attractor networks, etc.

Describe the core formalism briefly: what is being modelled, what are the key variables or quantities, and what assumptions does the framework make about the underlying process.

If the paper is purely empirical with no explicit computational framework, write "Not applicable" and note what kind of framework the results might constrain.

---

### Prevailing model of the system under study

Describe the baseline understanding of the system, process, or brain region this paper is investigating — i.e. what the field assumed about how things work before this paper's contribution.

**Ground this in the paper's own introduction.** Authors use the introduction to lay out the current theoretical landscape as they understand it. Use this to infer what working model they are assuming or pushing against. Do not import background knowledge that is not signalled by the paper itself. If the introduction is thin on theoretical framing, note that explicitly.

---

### What this paper contributes

How do the results update, refine, challenge, or extend the prevailing model described above? Be concrete — what can we now say that we could not say (or could only speculate) before?

For **reviews**: what is the state of knowledge this review establishes, and what does it identify as the key unresolved questions?

---

### Brain regions & systems

List the brain regions, circuits, or neural systems this paper focuses on. For each, note its role in the paper's argument — e.g. "prefrontal cortex — proposed locus of attractor instability".

If the paper is purely computational or behavioural with no anatomical focus, write "Not applicable" and briefly describe the level of analysis instead.

---

### Mechanistic insight

This section has a high bar. To populate it, the paper must meet **both** of the following criteria:

1. It presents or formalises an **algorithm** — a process or computation that could in principle explain the phenomenon.
2. It provides **neural data** (recordings, imaging, lesion, pharmacology, etc.) that specifically support *that* algorithm over alternatives.

**Bonus**: if the paper also addresses the physical neural implementation (specific cell types, connectivity, neuromodulators, biophysical mechanisms), note this explicitly.

If the paper meets the bar, describe the phenomenon and then map the evidence onto Marr's three levels:
- **Computational**: what problem is the brain solving, and why?
- **Algorithmic**: what representations and processes implement the solution?
- **Implementational**: how is this realised in neural hardware?

If the paper does not meet the bar, write 2–3 sentences explaining why — e.g. "The paper proposes an RL algorithm and fits it to behaviour, but does not provide neural data linking the model's specific variables (e.g. RPE signals) to measured neural activity."

---

### Limitations & open questions

Acknowledged weaknesses, assumptions, or questions the paper raises but does not answer.

---

### Connections & keywords

List the following in one unified section:

- **Key citations**: papers explicitly named as foundational or directly compared against.
- **Named models or frameworks**: any named computational model, task paradigm, or theoretical framework central to the paper.
- **Brain regions**: any regions identified in the Brain regions section above.
- **Keywords**: 8–12 specific technical keyphrases summarising the paper's content. Favour precise terms over generic ones.

---

## Instructions

1. Read the full paper at `$ARGUMENTS`.
2. Classify the paper type (empirical / computational / review) — this governs how you fill in Methods, Key findings, and What this paper contributes.
3. Work through each section carefully. Do not hallucinate results — if something is unclear in the source, say so briefly rather than inventing detail.
4. Write the summary to `raw/summaries/<output_filename>`, where `<output_filename>` is the source filename unless a mismatch was detected (see **Filename mismatch check** above).
5. Confirm to the user which file was written, and flag any filename mismatch as described above.
6. End your response with exactly this line (fill in the values, keep the format exactly):
   `STATUS: success | input=<input_filename> | output=<output_filename> | renamed=<yes/no>`
   If you failed to write a summary for any reason, use `STATUS: failed | input=<input_filename> | reason=<brief reason>`
