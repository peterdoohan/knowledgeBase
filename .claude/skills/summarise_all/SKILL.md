---
name: summarise_all
description: Scans raw/mds/ for papers without summaries and processes them in parallel batches using make_summary sub-agents. Accepts optional concurrency and model arguments.
user-invocable: true
disable-model-invocation: true
argument-hint: [n_agents] [model=sonnet|opus|haiku] (all optional)
allowed-tools: Read Glob Grep Bash Agent Write
---

# summarise_all

You are an orchestrator agent for a knowledge base pipeline. Your job is to find all papers in `raw/mds/` that do not yet have a summary in `raw/summaries/`, then process them in parallel batches by launching sub-agents that each run the `make_summary` pipeline.

## Step 1 — Parse arguments

The argument string is: `$ARGUMENTS`

Parse the following two optional parameters from `$ARGUMENTS`:

**`n_agents`** — a bare positive integer, e.g. `10`. Controls how many sub-agents run in parallel per batch. Default: `5`.

**`model`** — either a bare model name (`sonnet`, `opus`, `haiku`) or a `model=<value>` key-value pair (`model=sonnet`). Controls which model each sub-agent uses. Default: `sonnet`.

Both parameters are optional and can appear in either order. All of the following are valid:
- `/summarise_all` → n_agents=5, model=sonnet
- `/summarise_all 10` → n_agents=10, model=sonnet
- `/summarise_all opus` → n_agents=5, model=opus
- `/summarise_all 10 sonnet` → n_agents=10, model=sonnet
- `/summarise_all model=opus` → n_agents=5, model=opus
- `/summarise_all 10 model=opus` → n_agents=10, model=opus

If any unrecognised tokens are present (i.e. not a positive integer, not a model name, not a `model=` pair), stop and tell the user:
> **Usage:** `/summarise_all [n_agents] [model]`
> Example: `/summarise_all 10 opus`

## Step 2 — Discover work to do

1. Ensure `raw/summaries/` exists: run `mkdir -p /Users/vyp730/Projects/knowledgeBase/raw/summaries` (use Bash).
2. Glob `raw/mds/*.md` to get the full list of source files (basenames only).
3. Glob `raw/summaries/*.md` to get the full list of existing summaries (basenames only). If the directory is empty this returns nothing — that is fine.
4. A source file is **covered** if a summary exists with the exact same basename. Derive the list of **uncovered** files as the set difference.
5. If there are no uncovered files, report that all papers already have summaries and stop.
6. Report to the user: how many files are covered, how many are uncovered, and list the uncovered filenames. Then proceed.

## Step 3 — Process in parallel batches

Divide the uncovered files into batches of `n_agents`. For each batch, launch all sub-agents in that batch **in a single message** (i.e. in parallel) using the Agent tool. Wait for the batch to complete before starting the next batch.

Set the `model` parameter on every Agent tool call to the value parsed in Step 1.

Each sub-agent prompt must follow this exact structure (keep it short — the sub-agent reads its own instructions):

---
You are executing the make_summary pipeline on a single file.

1. Read the full instructions at `/Users/vyp730/Projects/knowledgeBase/.claude/skills/make_summary/SKILL.md`.
2. The file to process is: `raw/mds/<filename>`
3. Follow the instructions exactly, treating the above path as the file to process (i.e. the input argument).
---

Each sub-agent has access to: Read, Glob, Grep, Write, Bash.

## Step 5 — Report results

Each sub-agent ends its response with a `STATUS:` line. Parse these to build the final report:

- **Processed**: for each `STATUS: success` line, show `input → output` (flag `renamed=yes` cases).
- **Failed**: for each `STATUS: failed` line, show `input` and `reason`. Also flag any sub-agent that returned no STATUS line at all as failed with reason "no status returned".
- **Total**: X succeeded, Y failed out of Z attempted.
