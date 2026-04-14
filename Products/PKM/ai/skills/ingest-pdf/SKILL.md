---
name: ingest-pdf
description: Ingest PDF documents (papers, reports, whitepapers) into the PKM wiki pipeline. Use when the user provides a PDF file path and wants to extract its content and ingest it into the wiki. Triggers include "ingest this paper", "ingest this PDF", "process this PDF", or any request to ingest PDF content.
---

# PDF Ingestion Skill
This skill extracts text from PDF documents, saves them as source files in `Sources/Papers/`, and follows the standard Ingest workflow.

## Workflow

### Step 1: Extract PDF Content

Use the Read tool to read the PDF file. For large PDFs (>10 pages), read in chunks using the `pages` parameter.

1. Read the PDF to extract text content
2. Identify:
   - **Title**: From the document header or first page
   - **Authors**: From the paper's author section
   - **Abstract/Summary**: If present
   - **Key sections**: Section headings and their content
   - **References**: Notable citations

### Step 2: Create Source File

Create a markdown file in `Sources/Papers/`:

```markdown
---
title: "[Paper/Document Title]"
author:
  - "[Author 1]"
  - "[Author 2]"
source: "[Journal/Publisher/Organization]"
link: "[URL if available]"
published: YYYY-MM-DD
created: YYYY-MM-DD
tags:
  - clippings
  - paper
---

## Abstract

[Abstract or executive summary]

## Content

[Extracted text organized by sections]

## References

[Key references cited in the document]
```

**Filename:** Use the paper title, cleaned of special characters, under 60 characters.

**Subfolder note:** The user specifies the source type at ingest time. Default is `Sources/Papers/` for academic content. For reports or whitepapers that are more article-like, the user may direct to `Sources/Articles/` instead.

### Step 3: Standard Ingest

Hand off to the `/ingest` skill, passing the source file path created in Step 2. The standard ingest skill handles: first inspection, discussion, wiki page creation, index/log updates, and git commit & push.

## Notes

- PDFs with scanned images (no text layer) cannot be processed. Inform the user.
- For very long documents (50+ pages), focus the first inspection on the abstract, introduction, and conclusion. Ask the user which sections to deep-dive.
- Tables and figures are described textually. Note their existence and key data points.
