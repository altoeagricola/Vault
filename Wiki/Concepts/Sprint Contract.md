---
title: Sprint Contract
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Generator-Evaluator Pattern]]"
  - "[[Harness Simplification]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A negotiated agreement between a generator and evaluator agent that defines what "done" looks like for a chunk of work before any code is written. The contract bridges the gap between high-level product specs and testable implementation details.

## How it works

Before each sprint:

1. The **generator** proposes what it will build and how success will be verified
2. The **evaluator** reviews the proposal to ensure the generator is building the right thing and that the criteria are testable
3. The two iterate until they agree on the contract
4. The generator builds against the agreed-upon contract
5. The evaluator grades the result against the contract's criteria, with hard pass/fail thresholds

## Why it matters

The planner in a [[Generator-Evaluator Pattern]] intentionally produces high-level specs — detailed enough to scope features but not so granular that incorrect technical assumptions cascade into the implementation. The sprint contract fills the gap: it turns user stories into specific, testable criteria without committing to implementation details too early.

In practice, contracts can be quite granular. In one retro game maker build, Sprint 3 alone had 27 criteria covering the level editor. The evaluator's findings against these criteria were specific enough to act on without extra investigation:

- "Rectangle fill tool only places tiles at drag start/end points instead of filling the region"
- "Delete key handler requires both `selection` and `selectedEntityId` to be set, but clicking an entity only sets `selectedEntityId`"
- "`PUT /frames/reorder` route defined after `/{frame_id}` routes — FastAPI matches 'reorder' as a frame_id integer and returns 422"

## Relationship to harness simplification

Sprint contracts were part of the sprint-based decomposition used with Claude Opus 4.5. When [[Harness Simplification]] led to removing the sprint construct entirely for Opus 4.6 (which could sustain coherent multi-hour builds without chunking), the evaluator moved to a single end-of-run pass with broader criteria rather than per-sprint contracts.
