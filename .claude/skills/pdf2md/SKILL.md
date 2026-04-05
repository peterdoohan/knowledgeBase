---
name: pdf2md
description: Converts a single PDF file to LLM-friendly Markdown using pymupdf4llm in the claude_code conda environment. Saves output to raw/mds/. Manual or programmatic invocation.
user-invocable: true
disable-model-invocation: true
argument-hint: [path to .pdf file]
allowed-tools: Read Glob Grep Write Bash
model: haiku
---

# pdf2md

You are an agent in a knowledge base pipeline. Your job is to convert a single PDF file to Markdown and save it to the correct location.

## Input validation

If `$ARGUMENTS` is empty or does not end in `.pdf`, stop immediately and return:

> **pdf2md requires a .pdf file as its argument.**
> Usage: `/pdf2md raw/inbox/filename.pdf` or `/pdf2md raw/pdfs/filename.pdf`

## Conversion

Run the following Python command using the `claude_code` conda environment:

```bash
conda run -n claude_code python -c "
import pymupdf4llm
import pathlib

input_path = pathlib.Path('$ARGUMENTS')
output_stem = input_path.stem
output_path = pathlib.Path('raw/mds') / (output_stem + '.md')

md_text = pymupdf4llm.to_markdown(str(input_path))
output_path.write_text(md_text, encoding='utf-8')
print(f'Written: {output_path}')
"
```

Run this from the repo root (`/Users/vyp730/Projects/knowledgeBase`).

## Output

- Saves the converted Markdown to `raw/mds/<stem>.md`
- Confirms the output path to the caller

## Status line

End your response with exactly this line:

`STATUS: success | input=<input_path> | output=raw/mds/<stem>.md`

If conversion fails for any reason:

`STATUS: failed | input=<input_path> | reason=<brief reason>`
