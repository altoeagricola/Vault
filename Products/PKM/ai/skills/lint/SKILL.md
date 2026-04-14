---
name: lint
description: Health-check the PKM wiki. Finds contradictions, orphan pages, missing concept pages, stale claims, and suggests next questions. Use when the user says "lint", "health check", "check the wiki", or wants to audit wiki quality.
---
# Wiki Lint
Performs a comprehensive health check of the wiki and produces an actionable report.

## Workflow

### Step 1: Gather State

1. Read `Wiki/Index.md` to get the full page inventory
2. Use Glob to find all `.md` files under `Wiki/`
3. For each wiki page, read its frontmatter and scan for `[[wiki-links]]`

### Step 2: Run Checks

Perform these checks in parallel where possible (using sub-agents):

#### 2a. Orphan Pages
- Pages in `Wiki/` that have **no inbound links** from other wiki pages
- Exclude `Index.md` and `Log.md` from this check

#### 2b. Missing Pages
- `[[wiki-links]]` that point to pages that **don't exist** yet
- Group by frequency: concepts mentioned 3+ times across pages are high priority

#### 2c. Contradictions
- Read all wiki pages and identify claims that conflict with each other
- Flag with the specific pages and the conflicting statements

#### 2d. Stale Claims
- Check `confidence: low` or `confidence: medium` pages that haven't been updated in 30+ days
- Flag pages whose `sources` reference has been superseded by newer sources

#### 2e. Frontmatter Completeness
- Pages missing required frontmatter fields (title, type, sources, related, created, updated, confidence)
- Pages with empty `related` arrays (should link to at least one other page)

#### 2f. Index Sync
- Pages that exist in `Wiki/` but are not listed in `Index.md`
- Entries in `Index.md` whose files no longer exist

### Step 3: Generate Report

Present findings organized by severity:

```
## Wiki Health Report — [Date]

### Critical (fix now)
- Contradictions
- Index out of sync

### Warnings (review soon)
- Orphan pages
- Missing pages (high frequency)
- Stale claims

### Suggestions (when you have time)
- Missing pages (low frequency)
- Incomplete frontmatter
- Questions to investigate next
```

### Step 4: Offer Fixes

For each finding, offer to fix it:
- Orphan pages → suggest links to add from related pages
- Missing pages → offer to create stub pages
- Index sync → update Index.md
- Frontmatter → fill in missing fields

Always ask before making changes.

### Step 5: Log

Append a lint entry to `Wiki/Log.md` with the date and summary of findings.
