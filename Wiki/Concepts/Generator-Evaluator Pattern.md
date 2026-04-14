---
title: Generator-Evaluator Pattern
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Agent Self-Evaluation Failure]]"
  - "[[Grading Criteria for Subjective Quality]]"
  - "[[Sprint Contract]]"
  - "[[Harness Simplification]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A multi-agent architecture inspired by Generative Adversarial Networks (GANs) where one agent generates output and a separate agent evaluates it, creating an iterative feedback loop that drives quality upward. Designed to overcome [[Agent Self-Evaluation Failure]].

## Structure

**Generator** — produces the artifact (frontend code, full-stack application, etc.) based on a prompt or spec. Iterates on its output in response to evaluator feedback.

**Evaluator** — inspects the generator's output against defined criteria, scores it, and writes a detailed critique. The critique feeds back to the generator as input for the next iteration.

In the full-stack variant, a **Planner** is added as a third agent to expand a brief user prompt into a detailed product spec before the generator begins work.

## The feedback loop

The GAN analogy is structural, not mathematical — there's no adversarial training. The generator and evaluator improve the artifact through iterative cycles:

1. Generator produces or refines the artifact
2. Evaluator inspects the live artifact (e.g., via Playwright MCP to navigate a running app)
3. Evaluator scores against [[Grading Criteria for Subjective Quality]] or a [[Sprint Contract]], writes a detailed critique
4. Generator receives the critique and either refines the current approach or pivots to a new direction
5. Repeat until criteria thresholds are met

In frontend design experiments, 5–15 iterations per generation were typical, with runs stretching up to four hours. Outputs generally trended upward but not always linearly — middle iterations sometimes outperformed later ones, and implementation complexity tended to increase across rounds.

## Key design decisions

- **The evaluator must interact with the live artifact**, not just review static code or screenshots. Using Playwright MCP to navigate pages and click through applications produces much more grounded feedback.
- **The evaluator needs calibration** — few-shot examples with detailed score breakdowns aligned the evaluator's judgment with human preferences and reduced score drift.
- **The generator should have strategic freedom** — instructed to decide after each evaluation whether to refine incrementally or pivot to an entirely different approach if the current direction isn't working.

## In full-stack development

The pattern extends to a three-agent system for complete application builds:

| Agent | Role | Key behavior |
|-------|------|-------------|
| Planner | Expands brief prompt into full product spec | Ambitious on scope, high-level on implementation, weaves in AI features |
| Generator | Implements features from the spec | Works in sprints (or continuously on capable models), self-evaluates before handing off |
| Evaluator | QA via live interaction with the running app | Grades against sprint contracts, files specific bugs with code-level detail |

Communication between agents happens via files — one agent writes, another reads and responds. This keeps state explicit and inspectable.
