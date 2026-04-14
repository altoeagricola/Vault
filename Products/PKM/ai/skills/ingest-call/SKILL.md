---
name: ingest-call
description: Ingest R&D public calls (editais) into the Prospections folder. Use when the user provides one or more URLs to a public call for proposals (edital, chamada pública) and wants to create a structured summary. Triggers include "ingest call", "ingest edital", or any request to process a public R&D call.
---
# Public Call Ingestion Skill
This skill downloads and processes R&D public call documents (editais, chamadas públicas), extracts key metadata, and creates a structured prospection note in `Prospections/R&D Public Calls/`.

This skill does **not** delegate to `/ingest` — public calls are prospection assets, not wiki sources.

## Input

One or more URLs pointing to the public call documents. Typically includes:
- **Main edital PDF** — the call itself with objectives, budget, timeline, requirements
- **Annexes** — submission forms, declarations, templates (PDF, DOCX, etc.)

## Workflow

### Step 1: Download Documents

Download all provided URLs to a subfolder inside `Prospections/R&D Public Calls/`:

```
Prospections/R&D Public Calls/[Call Name]/
├── [Call Name].md          ← structured summary note (created in Step 4)
├── _attachments/
│   ├── edital.pdf
│   ├── anexo-i-formulario.pdf
│   └── ...
```

Use `curl` or `WebFetch` to download files. Preserve original filenames where readable; otherwise use descriptive names. For DOCX files that can't be read directly, still save them as attachments — the user will open them in their editor.

### Step 2: Extract Content from Main Edital

Read the main edital PDF using `pdftotext` (via Bash) or the Read tool. Extract:

1. **Call number and name** (e.g., "EDITAL FAPES N° 06/2026 — Apoio aos Clusters de Inovação Capixaba")
2. **Issuing organization** (e.g., FAPES, FINEP, CNPq)
3. **Purpose** — what the call funds (1-2 sentences)
4. **Target sectors/areas** — which economic clusters, research areas, or themes
5. **Budget** — total funding available and per-project range (min/max)
6. **Counterpart requirements** — financial counterpart percentage from the company
7. **Timeline/Cronograma** — key dates (publication, submission deadline, results, contracting)
8. **Execution period** — project duration and possible extensions
9. **Eligibility** — who can apply (company type, location, partnerships required)
10. **Key requirements** — mandatory partnerships (ICT/IES), NIT involvement, certifications
11. **Submission platform** — where to submit (e.g., SigFapes)
12. **Contact** — email or phone for inquiries

For long editais (50+ pages), focus on the first ~20 pages which typically contain all metadata. Evaluation criteria and detailed rules can be summarized briefly.

### Step 3: First Inspection

Present a narrative overview of the call to the user:
- What it funds and why it matters
- Budget attractiveness (total and per-project)
- Key dates, especially submission deadline
- Eligibility fit — based on what's known about the user's context (company location, partnerships)
- Notable requirements or constraints
- Which annexes were downloaded and their purpose

Be straight to the point. The goal is to help the user quickly assess whether this call is worth pursuing.

**Wait for the user to confirm before creating the note.** The user may want to adjust emphasis, add notes, or flag specific requirements.

### Step 4: Create Prospection Note

Create a markdown file at `Prospections/R&D Public Calls/[Call Name]/[Call Name].md`:

```markdown
---
title: "[Call Number] — [Short Name]"
issuer: "[[Organization Name]]"
status: analyzing
budget_total: "R$ X.XXX.XXX,XX"
budget_per_project: "R$ XXX.XXX,XX – R$ XXX.XXX,XX"
counterpart: "X%"
deadline: YYYY-MM-DD
execution_months: NN
sectors:
  - "[Sector 1]"
  - "[Sector 2]"
link: "[Main URL]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - Prospection
  - public-call
---

## Overview

[1-2 paragraph summary of the call's purpose, what it funds, and strategic alignment]

## Key Dates

| Stage | Date |
|-------|------|
| Publication | YYYY-MM-DD |
| Submission deadline | YYYY-MM-DD |
| Preliminary results | YYYY-MM-DD |
| Final results | YYYY-MM-DD |
| Contracting starts | YYYY-MM-DD |

## Budget

- **Total**: R$ X.XXX.XXX,XX
- **Per project**: R$ XXX.XXX,XX – R$ XXX.XXX,XX
- **Counterpart**: X% financial counterpart from the company
- **Source**: [Fund name, e.g., FUNCITEC]

## Eligibility

[Bullet list of key eligibility requirements: company type, location, partnerships, etc.]

## Requirements

[Key mandatory requirements: ICT/IES partnership, NIT involvement, specific certifications, etc.]

## Sectors & Themes

[Description of target sectors, themes, or research areas]

## Evaluation Criteria

[Brief summary of how proposals are evaluated, if available]

## Documents

| Document | Purpose |
|----------|---------|
| [[edital.pdf]] | Main call text |
| [[anexo-i-formulario.pdf]] | Submission form |
| ... | ... |

## Notes

[User's notes, strategic observations, next steps — populated during discussion]
```

**Filename:** Use the call's short name, cleaned of special characters (e.g., `FAPES 06-2026 Clusters de Inovacao`).

**Frontmatter `status` values:**
- `analyzing` — initial state, still evaluating fit
- `preparing` — decided to apply, working on proposal
- `submitted` — proposal submitted
- `approved` / `rejected` — final outcome
- `archived` — no longer relevant

### Step 5: Git Commit & Push

Stage all new files (note + attachments), commit with message:
```
ingest-call: [Call Name] — [brief description]

- Prospections/R&D Public Calls/[Call Name]/[Call Name].md (created)
- Prospections/R&D Public Calls/[Call Name]/_attachments/... (downloaded)
```

Push to remote.

## Notes

- All monetary values should use Brazilian format (R$ X.XXX.XXX,XX)
- Dates in frontmatter use ISO format (YYYY-MM-DD); dates in the body can use DD/MM/YYYY for readability when quoting the original document
- If the main edital can't be read (encrypted PDF, scanned image), inform the user and ask them to provide the text
- DOCX files cannot be reliably extracted — save as attachments and note their purpose based on filename
- Some calls have multiple versions (original + amendments). Note which version was processed and flag any amendments
- The skill can process calls from any Brazilian funding agency (FAPES, FINEP, CNPq, FAPESP, etc.) — the structure is broadly similar
