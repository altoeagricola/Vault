---
name: ingest
description: Ingest a source file into the PKM wiki. Use when the user says "ingest", provides a source file path, or wants to process any content already in Sources/ into the wiki. This is the standard ingestion workflow that all specialized ingest skills (YouTube, tweet, PDF) delegate to after creating their source files.
---
# Standard Ingest Skill
Ingests a single source file from `Sources/` into the wiki. This is the core pipeline that all specialized ingest skills delegate to after extracting and saving their source content.

**Trigger:** User says "ingest [source-type] [filename]", provides a source file path, or a specialized ingest skill completes its extraction step.

## Input

A source file that already exists in one of the `Sources/` subfolders:
- `Sources/Articles/` — Web articles, blog posts
- `Sources/Papers/` — Academic papers, research documents
- `Sources/Repos/` — Repository READMEs, architecture notes
- `Sources/Data/` — Datasets, CSVs, JSON files
- `Sources/Transcripts/` — YouTube/podcast transcripts
- `Sources/Tweets/` — Tweet threads

If the user provides a URL to a web article (not YouTube, not Twitter/X, not a PDF), use WebFetch to extract the content, save it as a source file in `Sources/Articles/`, then continue with the workflow below.

## Workflow

### Step 1: Read the Source

Read the source file from `Sources/[type]/`.

### Step 2: First Inspection

Present a narrative first inspection:
- What the source is about — the core thesis or topic
- Key questions it raises or answers
- Notable claims, frameworks, or ideas worth tracking
- Potential connections to existing wiki content (search `Wiki/Index.md` first)

Be narrative but straight to the point — not a dry list, but not verbose either. The goal is to help the user capture the gist and decide what to emphasize.

### Step 3: Discussion

Wait for the user's input. Discuss to align on:
- Which takeaways matter most
- What emphasis or framing to use
- Whether certain concepts deserve their own pages
- Connections to existing wiki content

**Do not proceed until the user confirms direction.**

### Step 4: Create/Update Wiki Pages

Based on the discussion:

1. **Summary page** in `Wiki/Summaries/` — distillation of the source
2. **Concept pages** in `Wiki/Concepts/` — for significant ideas, frameworks, techniques
3. **Entity pages** in `Wiki/Entities/` — for organizations, products, tools, technologies
4. **Figure pages** in `Wiki/Figures/` — for notable individuals mentioned

For each page:
- Check if the page already exists (search `Wiki/Index.md` and use Glob)
- If it exists, **update** it with new information from this source — add the source to `sources:`, merge content, update `updated:` date
- If new, create it with full frontmatter per the page conventions in Instructions.md
- Use `[[wiki-links]]` for all internal references
- Set appropriate `confidence` level

### Step 5: Update Index

Update `Wiki/Index.md` — add new rows or update existing ones for all pages created/modified.

### Step 6: Update Log

Append an entry to `Wiki/Log.md` recording this ingestion with the date and list of pages affected.

### Step 7: Git Commit & Push

Stage all changed files, commit with a meaningful message following the vault's git conventions, and push to remote.

## Quality Guidelines

- Only create wiki-links for significant concepts, not every noun
- Check existing wiki pages for consistent naming before creating new ones
- Proper nouns maintain capitalization
- Technologies use official casing (e.g., `[[JavaScript]]`, `[[VS Code]]`)
- Set `confidence` based on source quality and corroboration
