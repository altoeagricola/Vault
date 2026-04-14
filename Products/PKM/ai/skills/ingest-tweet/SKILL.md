---
name: ingest-tweet
description: Ingest tweet threads into the PKM wiki pipeline. Use when the user provides a Twitter/X URL and wants to capture the thread as a source and ingest it into the wiki. Triggers include "ingest this tweet", "capture this thread", or any request to process Twitter/X content into the vault.
---
# Tweet Ingestion Skill
This skill captures tweet threads, saves them as source files in `Sources/Tweets/`, and follows the standard Ingest workflow.

## Workflow

### Step 1: Extract Tweet Content

Use the browser automation tools (Claude in Chrome or Playwright) to:

1. Navigate to the tweet URL
2. Extract the page text content
3. Capture:
   - **Author**: Display name and handle (@username)
   - **Date**: When the tweet was posted
   - **Thread content**: All tweets in the thread, in order
   - **Media descriptions**: Note any images, videos, or links embedded
   - **Engagement context**: Quote tweets or key replies if relevant to the thread's meaning

If browser tools are unavailable, use WebFetch to extract what's possible from the URL.

### Step 2: Create Source File

Create a markdown file in `Sources/Tweets/`:

```markdown
---
title: "[Brief description of thread topic]"
author: "[Display Name (@handle)]"
link: "[Tweet URL]"
date: YYYY-MM-DD
created: YYYY-MM-DD
tags:
  - clippings
  - tweet
---

# Thread by [Display Name] (@handle) — [Date]

[Tweet 1 content]

---

[Tweet 2 content]

---

[Tweet N content]

## Embedded Links
- [link descriptions if any]
```

**Filename:** `[Author handle] - [Brief topic].md` (e.g., `karpathy - LLM knowledge bases.md`)

### Step 3: Standard Ingest

Hand off to the `/ingest` skill, passing the source file path created in Step 2. The standard ingest skill handles: first inspection, discussion, wiki page creation, index/log updates, and git commit & push.

## Notes

- Twitter/X may require authentication. If content can't be extracted, ask the user to paste the thread text directly.
- For single tweets (not threads), still create a source file — even one tweet can contain a significant idea worth tracking.
- Quote tweets referenced in the thread should be attributed to their original author.
