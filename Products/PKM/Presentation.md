---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a2e
color: #e0e0e0
style: |
  section {
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
  }
  h1, h2, h3 {
    color: #e94560;
  }
  a {
    color: #0f3460;
  }
  table {
    font-size: 0.75em;
  }
  th {
    background-color: #16213e;
    color: #e94560;
  }
  td {
    background-color: #0f3460;
  }
  code {
    background-color: #16213e;
    color: #e94560;
  }
  blockquote {
    border-left: 4px solid #e94560;
    color: #a0a0c0;
  }
  em {
    color: #a0a0c0;
  }
  strong {
    color: #ffffff;
  }
  section.lead h1 {
    font-size: 2.5em;
  }
  section.lead p {
    font-size: 1.2em;
    color: #a0a0c0;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5em;
  }
---

<!-- _class: lead -->

# Personal Knowledge Management

**Knowledge curation leveraged by AI**
**Cognitive augmentation leveraged by mindful consumption**

---

## The Problem

Your mind is for **having** ideas, not for **holding** them.

- Information volume vastly exceeds what any person can hold in their head
- Passive consumption doesn't compound — it evaporates
- Isolated notes are trivia; **connected notes** are insight
- If you can't find it when you need it, you don't have it

> The question shifts from "how much can I remember?" to "how quickly can I find and use what I've already encountered?"

---

## Standing on Giants

This system is a **remix** of proven methodologies, rearranged for a specific mindset.

| Method | Creator | Core Idea |
|--------|---------|-----------|
| **GTD** | David Allen | Externalize every commitment into a trusted system |
| **PARA** | Tiago Forte | Organize by *actionability*, not by topic |
| **LLM Wiki** | Andrej Karpathy | AI agent maintains an interlinked knowledge wiki |

The blend: GTD's **process discipline** + PARA's **organizational structure** + LLM Wiki's **AI-powered maintenance**.

---

## GTD — The Workflow Engine

Five stages that keep the system alive:

1. **Capture** — Collect everything into inboxes. Nothing stays in your head.
2. **Clarify** — Is it actionable? What's the next action?
3. **Organize** — Place items where they belong (project lists, calendar, reference).
4. **Reflect** — Weekly Review: sweep, update, regain perspective.
5. **Engage** — Act with confidence. The system holds everything else.

**The two-minute rule:** if a next action takes < 2 minutes, do it now.

---

## PARA — The Organizational Structure

Everything sorts into four categories by **actionability**:

| Category | What it holds | Actionability |
|----------|--------------|---------------|
| **Projects** | Short-term efforts with a goal and deadline | Highest |
| **Areas** | Ongoing responsibilities to maintain | High |
| **Resources** | Topics of interest or reference | Medium |
| **Archives** | Inactive items from the other three | Low |

The same content **moves between categories** as its purpose changes — Docker might be a Project today, an Area tomorrow, a Resource next month.


___
## The PKM as a System - Expectation Leveling

- Muitas ferramentas / Ferramentas não triviais

- Reflexão: 
	“simplicidade é o grau máximo da sofisticação”.
	“dá muito trabalho fazer algo simples” 
	“simplicidade é um conjunto de conveniências bem selecionadas
	“Simples é o que desiners de produto esperam oferecer, não encontrar”

- Ferramentas críticas:
	Git / Github
	Obsidian
	Plugins do Obsidian (muitos)
	Claude Code / Claude Desktop


___

## The PKM as a System - Expectation Leveling

- Conceitos críticos
	Arquitetura de sistemas
	Controle de versão
	Prototipação
	Ergonomia / UX / UI
	Open Source
	Skills

- Perspectivas (mental attitude required)
	“There is no moat”
	Curated content + Aesthetics are the new moat
	The new normal: always revinventing



---

## The Vault — Architecture Overview

Two distinct zones with clear ownership:

<div class="columns">

**Zone 1: Knowledge Pipeline**
- `Sources/` — Human-owned, immutable raw inputs
- `Wiki/` — Agent-owned, curated and interlinked

**Zone 2: Structural Layers**
- `Areas/` — Life domains (identity)
- `Products/` — Value generation
- `Connections/` — People & companies
- `Journal/` — Periodic logs

</div>

**Cross-zone principle:** Wiki feeds the structural layers, not the reverse.

---

## Sources — The Raw Input

Seven media types, organized by format:

| Type | Content | Count |
|------|---------|-------|
| Articles | Web articles, blog posts | 17 |
| Books | PDFs, highlights | 15 |
| Repos | READMEs, architecture notes | 52 |
| Transcripts | YouTube, podcasts | 1 |
| Papers | Academic research | 1 |
| Tweets | Tweet threads | 1 |
| Data | Datasets, CSVs, JSON | 1 |

Sources are **immutable** — once ingested, they are never modified.

---

## Wiki — The Knowledge Graph

Eight page types, each serving a distinct purpose:

| Type | Purpose | Pages |
|------|---------|-------|
| **Concept** | Topics and ideas across sources | 17 |
| **Tool** | CLI tools, utilities, developer software | 34 |
| **Figure** | Notable individuals | 3 |
| **Summary** | Distillation of a single source | 1 |
| **Analysis** | Deep dives on specific questions | 0 |
| **Comparison** | Side-by-side evaluations | 0 |
| **Insight** | Syntheses born from queries | 0 |
| **Entity** | Organizations, products, technologies | 0 |

**Total wiki pages: 55** — and growing with every ingestion.

---

## Page Anatomy

Every wiki page follows a strict contract:

```yaml
---
title: Reverse Proxy
type: Concept
sources:
  - "[[InfraKeeper]]"
related:
  - "[[Caddy]]"
  - "[[Split-Horizon DNS]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high       # high | medium | low
---
```

- **Confidence** tracks source quality: single source (low) → corroborated (high)
- **Wiki-links** `[[NoteName]]` connect everything into a navigable graph
- A **validation hook** blocks writes missing required fields

---

## Areas — The Identity Layer

Areas define what is **essential in life** — what all efforts aim toward.

| Area | Purpose |
|------|---------|
| **Self** | Personal growth and learning |
| **Professional** | Career and craft |
| **Health** | Physical and mental well-being |
| **Finance** | Financial stability and goals |
| **Family** | Family relationships |
| **Pets** | Animal companions |

Areas have **no end date** — they are maintained, not completed.

---

## Products — Value from Knowledge

Knowledge consolidated into practical output:

| Product | Domain |
|---------|--------|
| **PKM** | This system itself — self-referential |
| **InfraKeeper** | Homelab infrastructure management |
| **ControlPlane** | Control plane tooling |
| **Hermes** | Messaging system |
| **Fluxy** | Flow management |
| **AI-KB** | AI knowledge base |
| **AsyncAPI** | Async API specs |
| **PM-Metrics / PM-Tools** | Project management |

Each product has a counterpart codebase in `~/Base/Products/`.

---

## The AI Agent — How It Works

The agent (Claude Code) is the **wiki's owner and maintainer**.

Three core workflows:

| Workflow | Trigger | What happens |
|----------|---------|-------------|
| **Ingest** | "ingest [type] [file]" | Read source → discuss → create wiki pages → index → commit |
| **Query** | Ask a question | Search wiki → synthesize answer → optionally file new page |
| **Lint** | "lint" | Find contradictions, orphans, stale claims → fix → commit |

Every workflow ends with a **git commit & push** — the wiki has full version history.

---

## Ingest — The Core Loop

The most-used workflow, always **interactive and one-at-a-time**:

```
User: "ingest article Harness Design..."
    ↓
1. Agent reads the source file
2. Presents first inspection — key observations
3. Discussion to align on emphasis
4. Creates Summary page
5. Creates/updates Concept, Entity, Figure pages
6. Updates Wiki/Index.md
7. Appends to Wiki/Log.md
8. Git commit & push
```

Specialized variants: `ingest-youtube`, `ingest-tweet`, `ingest-pdf`, `ingest-product`, `ingest-call`

---

## Agent Skills — The Toolbox

Reusable workflows registered as slash commands:

| Skill | What it does |
|-------|-------------|
| `/ingest` | Standard wiki ingestion pipeline |
| `/ingest-youtube` | Extracts transcript → ingests |
| `/ingest-tweet` | Captures thread via browser → ingests |
| `/ingest-pdf` | Extracts text from PDF → ingests |
| `/ingest-product` | Reads product codebase → ingests |
| `/ingest-call` | Processes R&D public calls → prospection notes |
| `/conceptualize` | Surveys vault, generates concept page |
| `/lint` | Full wiki health check |

---

## Automation & Guardrails

The system runs on its own where it can:

**Scheduled tasks**
| Task | Schedule | Purpose |
|------|----------|---------|
| `weekly-wiki-lint` | Mondays 9:03 AM | Automated health check |

**Hooks**
| Hook | Trigger | Purpose |
|------|---------|---------|
| `validate-frontmatter.sh` | Before any Wiki write | Blocks pages with missing or invalid frontmatter |

**Git conventions** — every change is committed with structured messages:

---

## The Compounding Effect

What this system produces over time:

- **88 source files** consumed and preserved
- **55 wiki pages** generated, interlinked, and maintained
- **Concepts** that surface across unrelated sources get their own pages — patterns emerge
- **Insights** born from queries create new knowledge that didn't exist in any single source
- Every ingestion **enriches existing pages** — the wiki gets smarter, not just bigger

> The human curates direction. The AI handles throughput.
> Together: knowledge that compounds.

---

<!-- _class: lead -->

# The System Maintains Itself

A weekly lint catches contradictions, orphans, and stale claims.
A frontmatter hook enforces structure at write-time.
Every change is versioned in git.

**The result:** a knowledge base that is always navigable, always consistent, and always growing.

---

## Obsidian — The Interface

The vault lives in Obsidian with purpose-built plugins:

| Plugin | Role |
|--------|------|
| **Templater** | Dynamic note generation |
| **Tasks** | Advanced task queries across the vault |
| **Smart Connections** | Semantic search via embeddings |
| **Auto-Note-Mover** | Automatic file organization |
| **Periodic Notes** | Daily/Weekly/Monthly journaling |

Database views (`.base` files) provide structured browsing of each wiki section.

---

<!-- _class: lead -->

# Knowledge curation leveraged by AI.
# Cognitive augmentation leveraged by mindful consumption.

*A Personal Knowledge Management system — built for compounding.*
