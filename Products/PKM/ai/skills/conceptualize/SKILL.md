---
name: conceptualize
description: Analyze how a concept is used across the vault and generate or update its Wiki/Concepts page with a well-rounded definition and perspectives. Use when the user says "conceptualize", names a concept to define, or wants to flesh out a concept page from vault-wide usage.
---
# Conceptualize Skill
Builds or enriches a concept page by surveying how the concept appears across the entire vault — wiki pages, areas, products, and journal — then synthesizing a comprehensive definition with multiple perspectives.

**Trigger:** User says "conceptualize [concept name]", or asks to define/flesh out a concept from vault usage.

## Input

A concept name (e.g., "Reverse Proxy", "Infrastructure as Code", "Context Anxiety").

## Workflow

### Step 1: Search the Vault

Search broadly for the concept across the vault:

1. **Wiki/Index.md** — Check if a concept page already exists
2. **Grep the vault** — Find every mention of the concept (and reasonable aliases/variations) across:
   - `Wiki/` — all page types (summaries, entities, tools, analyses, comparisons, insights)
   - `Areas/` — areas of responsibility
   - `Products/` — product documentation
   - `Journal/Weekly/` and `Journal/Monthly/` — periodic reflections (skip `Journal/Daily/`)
3. **Read the matches** — Read the relevant sections of each file where the concept appears to understand context and usage

### Step 2: Present Findings

Present a concise synthesis to the user:
- How many times and where the concept appears
- The different contexts and angles from which it's referenced (practical, theoretical, tooling, etc.)
- Whether a concept page already exists and what it currently covers
- Gaps: perspectives or angles present in the vault but missing from the concept page (or that would be missing from a new one)

### Step 3: Discussion

Wait for the user's input. Discuss to align on:
- Which perspectives and angles to emphasize
- What definition framing works best (practical vs. theoretical, broad vs. narrow)
- Whether related concepts should also be created or updated
- Any additional context the user wants to inject that isn't in the vault

**Do not proceed until the user confirms direction.**

### Step 4: Create or Update the Concept Page

Write `Wiki/Concepts/[Concept Name].md` with:

**Frontmatter:**
```yaml
---
title: Concept Name
type: Concept
sources:
  - "[[source or page where it appears]]"
related:
  - "[[related wiki page]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
---
```

**Tone and scope:** Concept pages serve an educational purpose — this vault is shared with partners who may not be familiar with the subject. Pages should expose the gist and instigate further exploration, not be exhaustive references. Write for someone encountering the concept for the first time: clear, concise, and curiosity-provoking. End with threads the reader can pull on, not with closure.

**Body structure:**
1. **Opening paragraph** — Clear, concise definition. What it is and why it matters. Accessible to newcomers.
2. **Core mechanics** — The essential how-it-works, kept brief. Use tables or short lists when they aid clarity.
3. **Perspectives** — Sections drawn from how the vault uses the concept. Each perspective is a lens (e.g., "In infrastructure", "In knowledge management", "In software design"). Only include perspectives that are grounded in vault content or the user's input.
4. **Relationships** — How this concept connects to other wiki concepts, with `[[wiki-links]]`. Frame these as invitations to explore further.
5. **Open Questions** (optional) — Unresolved tensions or areas where the vault's understanding is incomplete.

**What to avoid:** Don't write encyclopedic coverage. Don't include exhaustive history or every edge case. The goal is a landing page that orients the reader and gives them enough to decide where to go deeper.

**Confidence rules:**
- `high` — Concept appears in 3+ vault pages with consistent usage
- `medium` — Concept appears in 1-2 pages or usage varies
- `low` — Concept is mentioned but never deeply explored in the vault

If the page already exists, merge new perspectives and sources rather than overwriting. Update the `updated:` date and adjust `confidence` if warranted.

### Step 5: Update Related Pages

For wiki pages that reference the concept but don't link to its concept page:
- Offer to add `[[Concept Name]]` wiki-links where appropriate
- Update `related:` arrays on closely connected pages

### Step 6: Update Index & Log

1. Update `Wiki/Index.md` — add or update the row for the concept page
2. Append an entry to `Wiki/Log.md` recording this action

### Step 7: Git Commit & Push

Stage all changed files, commit with a meaningful message, and push to remote.

```
conceptualize: [Concept Name] — [brief description of what was done]

- Wiki/Concepts/[Concept Name].md (created|updated)
- [other pages updated]
- Wiki/Index.md (updated)
- Wiki/Log.md (updated)
```
