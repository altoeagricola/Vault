---
title: Agent Self-Evaluation Failure
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Generator-Evaluator Pattern]]"
  - "[[Grading Criteria for Subjective Quality]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A persistent failure mode in agentic systems where models, when asked to evaluate their own work, respond by confidently praising the output — even when quality issues are obvious to a human observer. The agent identifies legitimate problems but then talks itself into deciding they aren't significant.

## Manifestation

The problem is most pronounced on subjective tasks like frontend design, where there is no binary check equivalent to a verifiable software test. Whether a layout feels polished or generic is a judgment call, and agents reliably skew positive when grading their own work.

However, the failure also appears on tasks with verifiable outcomes. Agents exhibit poor judgment during implementation — missing bugs, stubbing features, or accepting broken functionality — because the same model that wrote the code is poorly positioned to challenge it.

## Why separation works

The [[Generator-Evaluator Pattern]] addresses this by assigning generation and evaluation to separate agents. The separation doesn't eliminate leniency on its own — the evaluator is still an LLM inclined to be generous toward LLM-generated output. But tuning a standalone evaluator to be skeptical is far more tractable than making a generator critical of its own work.

Calibrating the evaluator requires iterative prompt engineering: reading evaluator logs, finding examples where its judgment diverges from human assessment, and updating the prompt to correct those divergences. Several rounds of this loop are typically needed before the evaluator grades in a way that matches human standards.

## Practical observation

Out of the box, Claude is a poor QA agent. In early runs, it would identify issues then approve the work anyway, and test superficially rather than probing edge cases. The evaluator only became useful after explicit tuning to be more skeptical and thorough.
