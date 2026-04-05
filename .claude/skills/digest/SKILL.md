---
name: digest
description: Pipeline skill that processes all new PDFs in raw/inbox. For each PDF: converts to markdown, moves files to their permanent locations, generates a structured summary, and logs the result to log.md. Invoked manually when new PDFs have been dropped into raw/inbox.
user-invocable: true
disable-model-invocation: true
argument-hint: []
allowed-tools: Read Glob Grep Write Bash Agent
model: haiku
---

# digest

You are a pipeline orchestrator. Your job is to process every PDF currently sitting in `raw/inbox/`, running each through the full ingestion pipeline and logging the results.

## Step 1 — Discover new PDFs

Glob `raw/inbox/*.pdf`. If no files are found, report "No PDFs found in raw/inbox." and stop.

List the files you found to the user before proceeding.

## Step 2 — For each PDF, run the pipeline

Process files one at a time. For each `raw/inbox/<filename>.pdf`:

### 2a. Convert PDF to Markdown

Use the Agent tool to invoke the `pdf2md` skill, passing the full path to the PDF. Wait for it to return a STATUS line.

- If `STATUS: failed` — log the failure (see Step 3) and skip to the next PDF.
- If `STATUS: success` — note the output path (e.g. `raw/mds/<stem>.md`) and continue.

### 2b. Move files to permanent locations

Once conversion succeeds:

1. Move the PDF out of inbox:
   ```bash
   mv /Users/vyp730/Projects/knowledgeBase/raw/inbox/<filename>.pdf /Users/vyp730/Projects/knowledgeBase/raw/pdfs/<filename>.pdf
   ```
2. Confirm `raw/mds/<stem>.md` exists (it was written by pdf2md).

### 2c. Generate summary

Use the Agent tool to invoke the `make_summary` skill, passing the path to the new `.md` file (e.g. `raw/mds/<stem>.md`). Wait for it to return a STATUS line.

- Note the output summary path from the STATUS line (may differ from input stem if a filename mismatch was detected and corrected).
- If `STATUS: failed` — log the failure and continue to the next PDF.

## Step 3 — Update STATUS.md and log.md

After a successful summary, read `raw/summaries/STATUS.md` and add the new summary to the `pending` list:

```yaml
pending:
  - path: raw/summaries/<summary_filename>.md
    added_at: <ISO 8601 UTC>
```

Then append a YAML entry to `log.md`.

Read the current contents of `log.md` first, then write the full updated file. The file is a YAML list — append new entries at the bottom.

### Entry format for success:

```yaml
- timestamp: <ISO 8601 datetime, e.g. 2026-04-05T14:32:01>
  agent: digest
  event: summary_ready
  pdf: raw/pdfs/<filename>.pdf
  md: raw/mds/<stem>.md
  summary: raw/summaries/<summary_filename>.md
  renamed: <yes/no>
```

### Entry format for failure:

```yaml
- timestamp: <ISO 8601 datetime>
  agent: digest
  event: failed
  pdf: raw/inbox/<filename>.pdf
  stage: <pdf2md | make_summary>
  reason: <brief reason from STATUS line>
```

Get the current timestamp by running: `date -u +"%Y-%m-%dT%H:%M:%S"`

## Step 4 — Report to user

After all PDFs are processed, print a summary:

```
Digest complete.
  Processed: N
  Succeeded: N
  Failed: N

Ready for wiki integration:
  - raw/summaries/foo.md
  - raw/summaries/bar.md
```

List any failures separately with their stage and reason.
