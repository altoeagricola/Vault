---
name: update-mcr
description: Check the BCB portal for a new version of the Manual de Crédito Rural (MCR), compare against the version recorded in the wiki, and ingest changes if there is a newer update. Use when the user says "update mcr", "atualizar mcr", "verificar mcr", or on the scheduled monthly trigger (first Monday of each month at 09:00).
---

# Update MCR

Monitors the Banco Central's Manual de Crédito Rural (MCR) for new "Atualizações" and keeps the wiki's MCR concept page in sync with the current normative version.

## Context

The MCR is updated irregularly (typically monthly or more often) by the BCB. The wiki tracks the current version in:

- **Concept page:** `Wiki/Concepts/MCR.md` — frontmatter field `version` (ex.: `"Atualização MCR nº 754, de 31/03/2026"`)
- **Source page:** `Sources/Papers/BCB - Manual de Crédito Rural (MCR).md` — same field
- **Local PDF:** `/Users/okumaaltoe/Documents/ALTOÈ Agricola/MCR e Regulacoes/ManualCompleto.pdf`

The canonical portal for the MCR is https://manuais.bcb.gov.br/app/manual/mcr/publico.

## Workflow

### Step 1: Fetch the Current Published Version

1. Use WebFetch on the portal page `https://manuais.bcb.gov.br/app/manual/mcr/publico` with a prompt asking for:
   - The current "Atualização MCR nº X, de DD de mês de YYYY" (normally on the cover page or header)
   - The direct download link for the full PDF ("Manual Completo")
   - The "Base Normativa" (list of Resoluções) of the current update
   - The "Comando da Atualização" (list of Capítulos/Seções/Itens alterados)

2. If WebFetch cannot retrieve the PDF URL reliably, ask the user to provide the URL of the current full PDF.

### Step 2: Read the Current Wiki State

1. Read the frontmatter of `Wiki/Concepts/MCR.md` and extract `version`.
2. Normalize both the published version (from Step 1) and the wiki version to the format `Atualização MCR nº NNN, de DD/MM/YYYY` for comparison.

### Step 3: Compare

- **If versions match:** report "No changes — wiki is current at version X". Append an entry to `Wiki/Log.md` with action `update` and note "no-op: MCR version unchanged". Stop here.
- **If the published version is newer:** continue to Step 4.
- **If the published version is older or unparseable:** report the discrepancy and stop — do not overwrite.

### Step 4: Download and Replace the Local PDF

1. Download the new full PDF to `/Users/okumaaltoe/Documents/ALTOÈ Agricola/MCR e Regulacoes/ManualCompleto.pdf`, overwriting the existing file.
2. Verify the download: open with pdfplumber and confirm the cover page shows the expected update number.
3. If download fails, abort the run and report.

### Step 5: Extract the New Update Details

Using pdfplumber on the new PDF, extract:

1. **Cover block** (typically page 2) — the "Atualização MCR nº X, de DD/MM/YYYY" heading, the "Base Normativa da Atualização" table, and the "Comando da Atualização" table.
2. **Page count** (for the source file metadata).
3. A **diff summary**: list the Capítulos/Seções/Itens marked as Incluir / Alterar / Revogar in the Comando da Atualização.

### Step 6: Update Wiki Pages

1. In `Wiki/Concepts/MCR.md`:
   - Update frontmatter fields `version` and `updated` (today's date).
   - Update the section **"Atualizações Alteradas na Versão X"** in the body (or add an equivalent section) with the new update's changes.
   - Do not rewrite the whole page — only reflect what changed. The structural sections (12 capítulos, tipos de operação, programas) rarely change between updates; only update them if a Capítulo or programa was added/removed/renamed.

2. In `Sources/Papers/BCB - Manual de Crédito Rural (MCR).md`:
   - Update frontmatter `version`, `published`, `updated`.
   - Update the "Atualizações Alteradas" table and the "Base Normativa" section.

3. In `Wiki/Index.md`:
   - Update the `Updated` column for the MCR row.

4. In `Wiki/Log.md`:
   - Append a new row: `| YYYY-MM-DD | update | update-mcr (manual or scheduled) | Wiki/Concepts/MCR.md, Sources/Papers/BCB - Manual de Crédito Rural (MCR).md, Index.md | MCR atualizado de vNNN para vNNN+ (DD/MM/YYYY). Alterações: <resumo do Comando da Atualização> |`

### Step 7: Cross-Reference Impact

For each Capítulo/Seção listed in the Comando da Atualização, check if there are concept pages in the wiki that depend on it (ex.: `Wiki/Concepts/Pronaf.md` if Capítulo 10 was touched). If so:

- Flag them in the report as "may need review".
- Do **not** edit them automatically — only flag.

### Step 8: Git Commit

Stage the changed files and commit with the action prefix `update:`:

```
update: MCR atualizado para Atualização nº NNN (DD/MM/YYYY)

- Wiki/Concepts/MCR.md (version bump + changes section)
- Sources/Papers/BCB - Manual de Crédito Rural (MCR).md (version bump)
- Wiki/Index.md (updated)
- Wiki/Log.md (updated)

Base normativa: Resoluções CMN/BCB <lista>
Alterações: <resumo Capítulos/Seções>
Páginas que podem precisar de revisão: <lista, se houver>
```

Do not push unless explicitly asked — the user has git credentials configured separately.

### Step 9: Report

Return a concise summary to the user (or to the scheduled task session):

- Old version → New version
- Date of new update
- Resoluções incorporadas
- Capítulos/Seções afetados
- Lista de páginas do vault que podem precisar revisão (Step 7)
- Confirmação do commit

## Special Cases

- **No newer version available**: this is the common case. Report "MCR is current" in one line and append a no-op row to `Wiki/Log.md` so the monthly check leaves a trail.
- **Portal unavailable / WebFetch fails**: abort, report, suggest the user provide the PDF manually and re-run.
- **Cover page format changed**: if pdfplumber cannot find the expected "Atualização MCR nº X" string on page 2, fall back to page 1 or ask the user to confirm the current version string.
- **Structural changes** (new Capítulo, renamed programa): alert the user explicitly — the base Concept page's "Mapa dos 12 Capítulos" table needs human review before mass edits.

## Invocation

- Manual: user says "update mcr", "atualizar mcr", "verificar mcr", or equivalent.
- Scheduled: first Monday of each month at 09:00 via scheduled task `mcr-monthly-update`. The task prompt invokes this skill's workflow; the skill should detect that it's a scheduled run (no interactive user) and prefer the fully automated path, falling back to flagging instead of asking questions when ambiguity arises.
