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

## Vault Architecture

The vault has two distinct zones: the **Wiki** (agent-owned) and the **Structural layers** (human-owned, agent-assisted in the future).

### Zone 1: New Knowledge Pipeline (active now)

| Folder | Owner | Purpose |
|--------|-------|---------|
| `Sources/` | Human | Raw, unprocessed information. **Immutable. NEVER modify.** |
| `Wiki/` | Agent | LLM-generated wiki. Organized, interlinked, and maintained by the agent. |


### Zone 2: Structural Layers (agent reads, does not write — future scope)

| Folder | Owner | Purpose |
|--------|-------|---------|
| `Areas/` | Human | Essential identity domains requiring ongoing commitment. |
| `Products/` | Human | Knowledge consolidation as practical means for generating value. |
| `Connections/` | Human | Professional contacts — People and Companies. |
| `Linked Vaults/` | Human | Partner organizations with dedicated subfolders. |
| `Journal/` | Human | Periodic logs. Only `Journal/Daily/` is private (in .claudeignore). |
| `Archive/` | Human | Deprecated or archived content. |

**Cross-zone principle:** The Wiki feeds the structural layers. Insights, analyses, and concepts compiled in the Wiki may later inform Products, Areas, and Network. The reverse does not apply — the agent reads Areas/Products/Network for context during queries but does not write to them unless explicitly asked.


---

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
- `Wiki/Index.md` — Master catalog in table format. Updated on every ingest. Agent queries this with Grep to find relevant pages.
- `Wiki/Log.md` — Append-only activity log in table format. Records every agent action.
- `Wiki/Wiki.md` — Overview file for the Wiki folder.

**Database views:** Each wiki subfolder contains a `.base` file (e.g., `Concepts.base`) that configures Obsidian database views. These are auto-managed by Obsidian — do not modify.

**Creating new folders:** Ask the user before creating new Wiki subfolders, explaining why the existing types don't fit.


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

## Workflows

### Ingest

**Trigger:** User says "ingest [source-type] [filename]" (e.g., "ingest article Karpathy's LLM Wiki...")

**Process:**
1. Read the source file in `Sources/[type]/`
2. Present a first inspection: key questions and observations that help the user capture the gist. Be narrative but straight to the point — not a dry list, but not verbose either.
3. Discuss with the user to align on emphasis and takeaways
4. Create/update a Summary page in `Wiki/Summaries/`
5. Create/update all relevant Concept, Entity, and Figure pages across the wiki
6. Update `Wiki/Index.md` (add/update rows)
7. Append entry to `Wiki/Log.md`
8. **Git commit & push**: Stage all changed files, commit with a meaningful message, and push to remote

**Ingestion is always one source at a time, interactive.**

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


## Agent Skills

Skills are reusable workflows located in `Products/PKM/AI/skills/` and registered as slash commands.

| Skill | Command | Trigger | Purpose |
|-------|---------|---------|---------|
| `ingest` | `/ingest` | User says "ingest" or provides a source file | Standard wiki ingestion: first inspection, discussion, wiki pages, index/log, git commit |
| `ingest-youtube` | `/ingest-youtube` | User provides a YouTube URL | Extracts transcript via Python script, saves to `Sources/Transcripts/`, then delegates to `/ingest` |
| `ingest-tweet` | `/ingest-tweet` | User provides a Twitter/X URL | Extracts thread via browser tools, saves to `Sources/Tweets/`, then delegates to `/ingest` |
| `ingest-pdf` | `/ingest-pdf` | User provides a PDF file path | Extracts text from PDF, saves to `Sources/Papers/`, then delegates to `/ingest` |
| `ingest-product` | `/ingest-product` | User says "ingest product X" or names a product | Reads product docs from `~/Vault/Products/` and `~/Base/Products/`, saves to `Sources/Repos/`, then delegates to `/ingest` |
| `lint` | `/lint` | User says "lint" or "health check" | Full wiki health check: contradictions, orphans, missing pages, stale claims, frontmatter, index sync |
| `conceptualize` | `/conceptualize` | User says "conceptualize" or wants to define/flesh out a concept | Surveys vault-wide usage of a concept, then creates or updates its Wiki/Concepts page with definition and perspectives |
| `ingest-call` | `/ingest-call` | User provides URLs to a public R&D call (edital) | Downloads documents, extracts key metadata, creates structured prospection note in `Prospections/R&D Public Calls/` |

All specialized ingestion skills extract content into a source file, then delegate to `/ingest` for the standard wiki pipeline. The `ingest-call` skill is an exception — it targets `Prospections/`, not the wiki.


## Automation

### Scheduled Tasks

| Task | Schedule | Purpose |
|------|----------|---------|
| `weekly-wiki-lint` | Mondays 9:03 AM | Runs `/lint` automatically and reports findings |

### Hooks

| Hook | Event | Scope | Purpose |
|------|-------|-------|---------|
| `validate-frontmatter.sh` | PreToolUse (Write) | `Wiki/*` | Blocks writes to wiki pages missing required frontmatter fields or with invalid type values |

Hook script location: `Products/PKM/AI/hooks/validate-frontmatter.sh`


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
