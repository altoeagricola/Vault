---
title: Harness Design for Long-Running Application Development
type: Summary
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Generator-Evaluator Pattern]]"
  - "[[Context Anxiety]]"
  - "[[Context Reset]]"
  - "[[Agent Self-Evaluation Failure]]"
  - "[[Sprint Contract]]"
  - "[[Grading Criteria for Subjective Quality]]"
  - "[[Harness Simplification]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Anthropic engineering blog post by Prithvi Rajasekaran documenting how a GAN-inspired multi-agent architecture — planner, generator, evaluator — produces dramatically better software from simple prompts than single-agent approaches, especially over multi-hour autonomous coding sessions.

## The problem

Naive single-agent implementations hit two persistent failure modes on complex tasks:

1. **[[Context Anxiety]]** — models lose coherence as the context window fills and begin wrapping up work prematurely. Compaction (in-place summarization) doesn't fully solve it because the agent never gets a clean slate. [[Context Reset]] — clearing the window entirely and handing off state via structured artifacts — proved essential for Claude Sonnet 4.5, though Opus 4.6 largely eliminated the need.

2. **[[Agent Self-Evaluation Failure]]** — when asked to evaluate their own work, agents confidently praise mediocre output, even when quality issues are obvious to humans. This is worst on subjective tasks (design) but also present on verifiable ones.

## The architecture

### Frontend design: two-agent loop

The first experiment targeted frontend design, where self-evaluation failure was most visible. A [[Generator-Evaluator Pattern]] inspired by GANs separated creation from judgment:

- **Generator** produced HTML/CSS/JS frontends from prompts
- **Evaluator** used Playwright MCP to navigate the live page, screenshot, and score against four [[Grading Criteria for Subjective Quality]]: design quality, originality, craft, and functionality — with design and originality weighted higher

The evaluator was calibrated with few-shot examples. Over 5–15 iterations per generation, outputs trended toward more distinctive, polished designs. Notably, criteria wording itself shaped output character — phrases like "museum quality" pushed the generator toward specific aesthetics even before evaluator feedback.

In one example (Dutch art museum), the generator scrapped a polished but conventional dark-themed landing page on iteration 10 and reimagined the site as a 3D CSS perspective room with artwork on walls and doorway-based navigation — a creative leap not seen in single-pass generation.

### Full-stack coding: three-agent system

The pattern was then extended to full-stack development:

- **Planner** — takes a 1–4 sentence prompt and expands it into a full product spec. Prompted to be ambitious on scope and focused on product context rather than granular technical implementation, to avoid cascading spec errors. Also prompted to weave AI features into specs.
- **Generator** — works in sprints, implementing one feature at a time (React + Vite + FastAPI + SQLite/PostgreSQL stack). Self-evaluates at each sprint's end before handing off.
- **Evaluator** — uses Playwright MCP to click through the running application as a user would, testing UI, APIs, and database state. Grades each sprint against a [[Sprint Contract]] negotiated before coding began, with hard thresholds per criterion.

The sprint contract was key: generator proposed what it would build and how success would be verified; evaluator reviewed until they agreed. This bridged the gap between high-level specs and testable implementation without over-specifying too early.

### Calibrating the evaluator

Getting the evaluator to perform well required significant iteration. Out of the box, Claude is a poor QA agent — it identifies issues then talks itself into approving the work anyway, and tests superficially rather than probing edge cases. The tuning loop was: read evaluator logs, find judgment divergences from human assessment, update the prompt. Several rounds were needed before grading was reasonable.

## Results

**Retro game maker** (same one-line prompt):
- Solo agent: $9, 20 min — broken core gameplay, wasted layout space, rigid workflow
- Full harness: $200, 6 hr — functional gameplay, full-viewport canvas, AI integration for content generation, 16-feature spec across 10 sprints

**DAW (Digital Audio Workstation)** with simplified harness on Opus 4.6:
- $124, ~4 hr — working arrangement view, mixer, transport, AI agent that could compose simple songs through tool use

## Meta-lessons: harness simplification

The article's second major contribution is the principle of [[Harness Simplification]]: every harness component encodes an assumption about what the model can't do on its own, and those assumptions go stale as models improve. With Opus 4.6:

- **Sprint decomposition was removed** — the model could sustain coherent multi-hour builds without chunking
- **Context resets were dropped** — Opus 4.6 handled long context natively
- **The evaluator moved to a single end-of-run pass** rather than per-sprint grading
- **The evaluator's value became task-dependent** — unnecessary for tasks within the model's reliable capability boundary, still essential at the frontier

The interesting harness design space doesn't shrink as models improve — it *moves*. The engineer's job is to keep finding the next novel combination at the new frontier.
