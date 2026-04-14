---
title: Harness Simplification
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Generator-Evaluator Pattern]]"
  - "[[Context Anxiety]]"
  - "[[Context Reset]]"
  - "[[Sprint Contract]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

The principle that every component in an agent harness encodes an assumption about what the model can't do on its own, and those assumptions must be regularly stress-tested because they go stale as models improve. From Anthropic's "Building Effective Agents": *find the simplest solution possible, and only increase complexity when needed.*

## The core insight

The interesting harness design space doesn't shrink as models improve — it **moves**. Components that were once load-bearing become unnecessary overhead, while new capabilities open space for novel combinations that weren't possible before. The engineer's job is to keep finding the next frontier, not to maintain scaffolding built for previous model generations.

## Methodology

Radical simplification (cutting many components at once) proved counterproductive — it was difficult to tell which pieces were actually load-bearing. A more methodical approach worked better: removing one component at a time and reviewing the impact on final output.

## Case study: Opus 4.5 to Opus 4.6

The transition between model generations illustrated the principle concretely:

| Component | Opus 4.5 | Opus 4.6 | Reason |
|-----------|----------|----------|--------|
| [[Context Reset]] | Essential | Dropped | Model handles long context natively |
| Sprint decomposition | Essential | Dropped | Model sustains coherent multi-hour builds |
| [[Sprint Contract]] per sprint | Essential | Replaced with single end-of-run QA | Less granular coordination needed |
| Evaluator | High value across builds | Value depends on task complexity | Unnecessary for tasks within the model's reliable boundary, still essential at the frontier |

## The evaluator boundary

As a model's raw capability increases, the boundary of what it handles well on its own moves outward. The evaluator adds value only for tasks beyond that boundary. For tasks within it, the evaluator becomes unnecessary overhead. This means the evaluator is not a fixed yes-or-no architectural decision — it should be included or excluded based on where the target task sits relative to the current model's capability frontier.

## Practical guidance

- Re-examine a harness when a new model lands
- Strip away pieces that are no longer load-bearing
- Add new pieces to achieve greater capability that wasn't possible before
- Experiment with the target model on realistic problems and read its traces before deciding what scaffolding it needs
