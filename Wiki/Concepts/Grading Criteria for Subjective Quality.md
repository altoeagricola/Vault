---
title: Grading Criteria for Subjective Quality
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Generator-Evaluator Pattern]]"
  - "[[Agent Self-Evaluation Failure]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A technique for making subjective quality judgments (like "is this design good?") tractable for LLM evaluation by encoding design principles and preferences into concrete, gradable criteria. The key insight: "Is this beautiful?" is hard to answer consistently, but "Does this follow our principles for good design?" gives the model something concrete to score against.

## The four criteria (frontend design)

1. **Design quality** — Does the design feel like a coherent whole rather than a collection of parts? Colors, typography, layout, imagery combine to create a distinct mood and identity.
2. **Originality** — Is there evidence of custom decisions, or is this template layouts and library defaults? Explicitly penalizes "AI slop" patterns like purple gradients over white cards.
3. **Craft** — Technical execution: typography hierarchy, spacing consistency, color harmony, contrast ratios. A competence check rather than a creativity check.
4. **Functionality** — Usability independent of aesthetics. Can users find actions and complete tasks without guessing?

## Weighting matters

Design quality and originality were weighted higher than craft and functionality. Claude already scored well on craft and functionality by default — the technical competence came naturally. The failure mode was bland, generic output, so weighting toward design and originality pushed the model toward more aesthetic risk-taking.

## Criteria wording shapes output

The specific language used in criteria steered the generator in unexpected ways. Including phrases like "the best designs are museum quality" pushed designs toward a particular visual convergence, suggesting that criteria function as a form of prompt engineering — shaping the generator's creative direction through the evaluator's vocabulary.

## Calibration

The evaluator was calibrated using few-shot examples with detailed score breakdowns. This ensured the evaluator's judgment aligned with human preferences and reduced score drift across iterations. Without calibration, the evaluator defaulted to generous scoring that undermined the feedback loop.

## Adaptation for full-stack development

For complete application builds, the criteria were adapted from pure aesthetics to cover four broader dimensions: product depth, functionality, visual design, and code quality. Each criterion had a hard threshold — if any one fell below it, the sprint failed and the generator received detailed feedback on what to fix.
