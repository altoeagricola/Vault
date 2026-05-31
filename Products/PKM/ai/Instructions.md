---
title: Agent Instructions
---
This file provides guidance to AI agents (Claude Code, GitHub Copilot, OpenAI Codex, etc.) when working with this repository.

> **CRITICAL: Symlink Configuration**
>
> The files `CLAUDE.md`, `AGENTS.md` and `OPENCODE.MD` in the repository root are **symlinks** pointing to this file (`./Products/PKM/ai/Instructions.md`). This ensures a single source of truth for all AI agents.
>
> **AI Agents MUST:**
> - **NEVER** replace these symlinks with regular files
> - If symlinks are broken, restore them.


## What This Is

This is an **Obsidian vault** implementing a Personal Knowledge Management (PKM) system. It is not a traditional software codebase — there is no build system, package manager, or tests to run.

The system is a remix of GTD (Getting Things Done), PARA method, and other personalizations, with an LLM-maintained wiki at its core (inspired by Karpathy's LLM Wiki pattern).


## Objective

Knowledge curation leveraged by AI and cognitive augmentation leveraged by mindful consumption.


---

## Company Context

This vault serves **ALTOE Agricola**, a rural credit and agro-financing consultancy based in Marilândia, ES. For task-specific context, read these files on demand — **do not load all proactively**.

| File | Purpose | Read When |
|------|---------|----------|
| `Areas/ALTOE Agricola/Estrutura de Agentes IA.md` | Agent roster, skills, responsibilities, and models | Task involves agents or multi-agent coordination |
| `Areas/ALTOE Agricola/Regras de Organizacao do Vault.md` | Vault organization rules, content placement by type | Placing new content or organizing files |
| `Areas/ALTOE Agricola/ALTOE Agricola.md` | Strategic vision, company objectives, PKM+AI roadmap | Strategic or architectural decisions |
| `Areas/ALTOE Agricola/Design — Matriz de Handoff entre Agentes.md` | Inter-agent workflows and handoff patterns | Multi-agent task coordination |
| `Areas/ALTOE Agricola/Equipe.md` | Human team — Rodrigo (founder, CRQ) and Gaby (credit ops) | Tasks involving human responsibilities or scope limits |
| `Areas/ALTOE Agricola/Cadencia - Revisao de Agentes e Vault.md` | Recurring review rituals | Periodic review or structural change tasks |
| `Areas/ALTOE Agricola/Onboard - Sintese e Feedback dos Agentes.md` | Agent onboarding synthesis and open actions | Onboarding a new agent or reviewing past feedback |



## Sources Structure

Sources are organized by media type. The user specifies the type when requesting ingestion.

| Subfolder | Content |
|-----------|---------|
| `Sources/Articles/` | Web articles, blog posts, clippings |
| `Sources/Papers/` | Academic papers, research documents |
| `Sources/Books/` | PDFs or highlights from books |
| `Sources/Repos/` | Repository READMEs, architecture notes |
| `Sources/Data/` | Datasets, CSVs, JSON files |
| `Sources/Transcripts/` | YouTube video and podcast transcripts |
| `Sources/Tweets/` | Tweet threads and posts |


## Wiki Structure

Each subfolder maps to a page type. The folder name is the plural of the type.

| Subfolder           | Type       | Purpose                                        |
| ------------------- | ---------- | ---------------------------------------------- |
| `Wiki/Summaries/`   | Summary    | Distillation of a single source                |
| `Wiki/Concepts/`    | Concept    | Topic or idea referenced across sources        |
| `Wiki/Entities/`    | Entity     | Organizations, products, technologies          |
| `Wiki/Tools/`       | Tool       | CLI tools, GUI tools, developer utilities      |
| `Wiki/Figures/`     | Figure     | Notable individuals                            |
| `Wiki/Analyses/`    | Analysis   | Deep dives on specific questions               |
| `Wiki/Comparisons/` | Comparison | Side-by-side evaluations of concepts/entities  |
| `Wiki/Insights/`    | Insight    | Pages born from queries — the compounding loop |

**Special files:**
- `Wiki/Index.md` — Master catalog in table format. Updated on every ingest. Agent queries this with Grep to find relevant pages. *(Reference implementation of the vault-wide index convention — see below.)*
- `Wiki/Log.md` — Append-only activity log in table format. Records every agent action. *(Reference implementation of the vault-wide log convention — see below.)*
- `Wiki/Wiki.md` — Overview file for the Wiki folder.

**Database views:** Each wiki subfolder contains a `.base` file (e.g., `Concepts.base`) that configures Obsidian database views. These are auto-managed by Obsidian — do not modify.

**Creating new folders:** Ask the user before creating new Wiki subfolders, explaining why the existing types don't fit.


---

## Folder Index and Log Convention

**MANDATORY — All agents must maintain `index.md` and `log.md` in every major vault folder they touch. This is not optional.**

Every major vault folder (top-level and its direct subfolders, e.g., `Wiki/`, `Wiki/Concepts/`, `Sources/`, `Sources/Articles/`, `Areas/`, `Products/`) must contain two special files:

| File | Format | Purpose |
|------|--------|---------|
| `<Folder>/index.md` | Markdown table (update on add, change, or delete) | Catalog of all content in that folder. Agents MUST query this file first (via Grep) before scanning the full folder tree. |
| `<Folder>/log.md` | Markdown table — **append-only, never delete rows** | Activity log recording every agent action that touches the folder. One row per workflow run. |

### Update Triggers

- **index.md**: Update whenever a file is **created, updated, renamed, moved, or deleted** in the folder.
- **log.md**: Append one row after every agent workflow that touches the folder (`ingest`, `query` with filed result, `lint`, `update`, `scaffold`, `conceptualize`).

### When the Files Don't Exist Yet

If you are working in a folder that is missing `index.md` or `log.md`, **create both files before finishing your task**. Do not leave a folder without them.

### Index Column Formats

Adapt the index columns to the folder's content type:

| Folder type | Suggested columns |
|-------------|------------------|
| Wiki pages | `Path \| Type \| Title \| Topics \| Sources \| Confidence \| Updated` |
| Sources | `Path \| Type \| Title \| Source URL \| Added \| Ingested` |
| Areas / Products | `Path \| Type \| Title \| Description \| Updated` |
| Journal | `Path \| Date \| Summary` |

See `Wiki/Index.md` and `Wiki/Log.md` for reference implementations.

### Lint Check

The `lint` skill checks for missing or visibly stale `index.md` and `log.md` files and reports them as errors.

---

## Page Conventions

Every wiki page MUST have YAML frontmatter:
```yaml
---
title: Page Title
type: Concept | Entity | Figure | Tool | Summary | Analysis | Comparison | Insight
sources:
  - "[[source file 1]]"
related:
  - "[[wiki page 1]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
---
```

**Confidence rules:**
- `low` — Single source, unverified, or speculative
- `medium` — Single authoritative source, or multiple weak sources
- `high` — Corroborated by multiple sources, or well-established fact

**Linking:** Use Obsidian wiki-links `[[NoteName]]` for all internal references. Wiki pages may link to Areas and Products for context.


---
### Query

**Trigger:** User asks a question.

**Process:**
1. Search `Wiki/Index.md` to find relevant pages
2. Read those pages, plus any relevant pages in `Areas/` and `Products/` for context
3. Synthesize an answer with `[[wiki-link]]` citations
4. If the answer produces a valuable synthesis, offer to file it as a new wiki page — suggest the appropriate type (often Insight or Analysis) and folder
5. If new pages were created: **Git commit & push** with a meaningful message

**Scope:** All folders are searchable for queries **except** `Sources/` (used only during ingestion) and `Journal/Daily/` (private).

### Lint

**Trigger:** User says "lint".

**Process:**
1. Check for contradictions between pages
2. Find orphan pages with no inbound links
3. List concepts mentioned in pages but lacking their own page
4. Check for stale claims superseded by newer sources
5. Suggest questions to investigate next
6. If fixes were applied: **Git commit & push** with a meaningful message


---

## Templates Location

All note templates are in `Products/PKM/Templates/` (prefixed with `T-` for structural/content templates):
- `Daily Note.md` — Daily journal with routine tasks and due items
- `Weekly Note.md`, `Monthly Note.md` — Periodic reviews
- `T-Project.md`, `T-Area.md` — Structural notes
- `T-Article.md`, `T-Book.md`, `T-Video.md` — Source content types
- `T-Person.md` — Person entries (for Network/People)


## Key Conventions

- **Frontmatter**: Notes use YAML frontmatter with `tags` property for categorization
- **Links**: Use Obsidian wiki-links `[[NoteName]]` for internal references
- **Tasks**: Created with `- [ ]` syntax, often in Journal entries, queried via Tasks plugin
- **Attachments**: Stored in `_attachments/` folders (ignored in searches)
- **Covers**: Stored in `_covers/` folders (ignored in searches)
- **Overview files**: Each folder has an eponymous `.md` file (e.g., `Areas/Areas.md`, `Wiki/Wiki.md`)
- **Index files**: Each major folder has an `index.md` catalog — agents query these first; see [Folder Index and Log Convention](#folder-index-and-log-convention)
- **Log files**: Each major folder has a `log.md` activity log (append-only) — agents append a row after every workflow; see [Folder Index and Log Convention](#folder-index-and-log-convention)
- **`.base` files**: Database view configurations for Obsidian — agent should not modify these

### Structural Note Frontmatter

Non-wiki notes use different frontmatter patterns than wiki pages:

- **Root-level folders** (Areas, Products, Network, Partners, Archive): `tags: Root`
- **Child notes** link to parents via `root:` (array of wiki-links):
  ```yaml
  root:
    - "[[Areas]]"
  ```
- **Products** add `primary area:` and optionally `secondary area:`, `company:`
- **Network/People** use `aliases:`, `company:`, `role:` (array of wiki-links)
- **Network/Companies** use `context: "[[Network]]"`
- **Pets** use `context:`, `breed:`, `birth:`


## Obsidian Plugins in Use

Key plugins affecting vault behavior:
- **Templater**: Dynamic note generation with `{{date}}` variables
- **Tasks**: Advanced task queries in code blocks with `tasks` language
- **Smart Connections**: Semantic search using TaylorAI/bge-micro-v2 embeddings
- **Auto-Note-Mover**: Automatic file organization
- **Periodic-Notes**: Daily/Weekly/Monthly note generation
- **MG Grafeno Query**: Local desktop plugin for read-only `mg-grafeno-sql` code blocks that render live SELECT/WITH queries from the Docker database `mg-grafeno`.


## Structured Data Source of Truth

The Docker database `mg-grafeno` is the source of truth for structured MGgrafeno/MGg3 data already covered by its schema. Markdown files may preserve historical extracts for audit, but those tables must be treated as deprecated comparison material once an equivalent database query exists.

### MG Grafeno Application

There is also a dedicated application at `~/Base/Products/MG-Grafeno` that gives visibility and controlled manipulation surfaces for the `mg-grafeno` database. Agents working on MGg3 data must know this app exists before proposing new Markdown-only workflows.

Current structure:

- Stack: Next.js 16 App Router, React 19, TypeScript, Tailwind CSS v4, Shadcn/Radix UI, NextAuth/GitHub, `pg`, Recharts, OpenTelemetry.
- Local service: `mggrafeno-app`, normally exposed at `http://localhost:3200`; database service: `mggrafeno-postgres`.
- Generic data manipulation: `src/app/app/r/[resource]/` renders CRUD screens for resources registered in `src/lib/crud/registry.ts` and `src/lib/crud/resources/*`.
- Charts and database visibility: `src/app/app/reports/*` renders chart-driven reports, with SQL/query code in `src/lib/reports/queries.ts` and report metadata in `src/lib/reports/registry.ts`.
- Database model and migrations: `db/schema.sql` and `db/migrations/`; migrations must preserve the database as the canonical structured-data layer.
- App-specific agent guidance lives in `~/Base/Products/MG-Grafeno/ai/instructions.md` through the repo-root `AGENTS.md`/`CLAUDE.md` symlinks.

Boundary:

- Use the app for structured data entry, corrections, CRUD review, dashboards, charts, and operational visibility over the database.
- Keep discursive analysis, interpretation, synthesis, decision memos, historical narrative, and argumentation in Obsidian notes.
- When a new MGg3 need appears, decide explicitly: data/table/chart/workflow belongs in the app; narrative/analysis belongs in Obsidian; schema gaps should be proposed before either surface invents parallel data.

**Mandatory for all agents working with new files or MGg3/MGgrafeno notes:**

- Before adding or trusting tabular/factual operational data in Markdown, check whether the data belongs in one of the existing schemas: `documental`, `tecnologia`, `operacao`, `custo`, `suprimentos`, `aplicacao`, or `ssma`.
- If the model already covers the data, present suggested new database records or updates instead of duplicating the data as canonical Markdown.
- If the model is insufficient, present a concrete schema expansion proposal: table/schema, key columns, relationships, and why the existing tables are not enough.
- When preserving old Markdown tables for validation, mark them as deprecated/legacy and place the nearest possible `mg-grafeno-sql` query beside or immediately above/below them.
- Use only read-only queries in Obsidian blocks: `SELECT` or `WITH`. Mutating SQL belongs in a separate reviewed database task, not in notes.



## Git Conventions

Every workflow that modifies files ends with a git commit & push. Commit messages must be meaningful and follow this format:

```
<action>: <description>

- <list of pages created/updated>
```

**Examples:**
```
ingest: Karpathy's LLM Wiki — idea files, wiki-vs-RAG, three-layer architecture

- Wiki/Summaries/Karpathy LLM Wiki.md (created)
- Wiki/Concepts/LLM Wiki.md (created)
- Wiki/Concepts/RAG.md (created)
- Wiki/Figures/Andrej Karpathy.md (created)
- Wiki/Index.md (updated)
- Wiki/Log.md (updated)
```

```
query: filed comparison of MoE routing strategies

- Wiki/Comparisons/MoE Routing Strategies.md (created)
- Wiki/Index.md (updated)
```

```
lint: fixed 3 orphan pages, updated 2 stale claims

- Wiki/Concepts/Tokenization.md (added inbound links)
- Wiki/Entities/OpenAI.md (updated param count from newer source)
```

**Actions:** `ingest`, `query`, `lint`, `update`, `scaffold`

Stage only the files changed by the workflow. Push to remote after commit.


## Working with This Vault

1. Respect the hierarchy when suggesting where to place new content
2. Use appropriate templates when creating new notes; suggest improvements if you see opportunities
3. Maintain wiki-link references to connect related content
4. Keep `Journal/Daily/` private per the permissions
5. When in doubt about folder placement or new page types, ask the user

---

## File System — Absolute Paths and Placement Rules

**CRITICAL: Never create files outside the Vault root.** All work must be saved directly inside the Vault — never in a temporary `workdir/`, a workspace directory, or any path outside the Vault root.

This applies even when the agent is launched from a Multica workspace such as `/Users/okumaaltoe/multica_workspaces/.../workdir/`. Treat that directory as execution context only; it is not part of the Obsidian Vault, and files created there will not appear in Obsidian.
