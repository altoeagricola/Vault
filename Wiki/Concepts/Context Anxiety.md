---
title: Context Anxiety
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Context Reset]]"
  - "[[Harness Simplification]]"
created: 2026-04-13
updated: 2026-05-18
confidence: medium
---

A behavioral pattern in language models where the agent begins wrapping up work prematurely as it approaches what it believes is its context limit. The model shifts from executing the task to concluding it, even when significant work remains.

## Mechanism

As the context window fills during long-running agentic tasks, models lose coherence and start exhibiting completion-seeking behavior. This isn't a hard technical failure — the model doesn't crash — but rather a soft degradation where the agent starts cutting corners, simplifying outputs, or declaring tasks finished earlier than they should be.

## Compaction is insufficient

Compaction — summarizing earlier parts of the conversation in place so the agent can keep going on a shortened history — preserves continuity but doesn't give the agent a clean slate. Context anxiety can persist because the model still perceives itself as deep into a long session. [[Context Reset]] (clearing the window entirely with a structured handoff artifact) proved more effective because it provides a genuinely fresh start.

## Model variation

The severity varies across model generations. Claude Sonnet 4.5 exhibited context anxiety strongly enough that compaction alone wasn't sufficient, making context resets essential to harness design. Opus 4.5 largely removed the behavior on its own. Opus 4.6 improved further, handling long-context tasks natively without requiring either resets or decomposition into sprints.

## Implications for harness design

Context anxiety is a key reason multi-session architectures with structured handoffs outperform single long sessions for complex tasks — at least on models that exhibit the behavior. As models improve and the behavior diminishes, the scaffolding built to address it becomes unnecessary overhead, illustrating the [[Harness Simplification]] principle.

## Lint Review

Reviewed during the 2026-05-18 wiki lint. Confidence remains medium because the page describes a behavior observed in agent workflows rather than a stable external standard.
