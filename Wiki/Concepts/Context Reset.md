---
title: Context Reset
type: Concept
sources:
  - "[[Harness design for long-running application development]]"
related:
  - "[[Context Anxiety]]"
  - "[[Harness Simplification]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A technique for long-running agentic coding where the context window is cleared entirely and a fresh agent is spawned, with a structured handoff artifact carrying the previous agent's state and next steps. This contrasts with compaction, where earlier conversation parts are summarized in place.

## How it works

When an agent session reaches a natural break point (e.g., completing a feature sprint), the harness:

1. Has the current agent produce a structured artifact summarizing its state — what was built, what remains, key decisions made
2. Terminates that agent's session entirely
3. Spawns a new agent with a clean context window
4. Feeds the handoff artifact as initial context to the new agent

## Why it outperforms compaction

Compaction preserves conversational continuity by summarizing older messages, but the agent still perceives itself as deep into a long session. This means [[Context Anxiety]] — premature wrap-up behavior — can persist. A context reset provides a genuinely clean slate, eliminating the perceived pressure to conclude.

The trade-off is added orchestration complexity, token overhead, and latency for each reset. The handoff artifact must carry enough state for the next agent to pick up work cleanly — too sparse and the new agent loses critical context; too verbose and it defeats the purpose.

## When it's needed

Context resets were essential for Claude Sonnet 4.5, which exhibited strong context anxiety. Opus 4.5 and 4.6 largely removed the behavior, allowing the technique to be dropped in favor of continuous sessions with automatic compaction. This progression illustrates the [[Harness Simplification]] principle — scaffolding built for one model generation may become unnecessary overhead for the next.
