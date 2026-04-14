---
name: ingest-product
description: Ingest a product's documentation into the PKM wiki pipeline. Use when the user wants to ingest one of the products from ~/Vault/Products and its counterpart codebase in ~/Base/Products. Triggers include "ingest product X", "ingest ControlPlane", or any request to process a product's docs and code into the wiki.
---

# Product Ingestion Skill

This skill reads a product's documentation from both the Obsidian vault (`~/Vault/Products/<Name>/`) and its source codebase (`~/Base/Products/<Name>/`), extracts the **concepts and tools** it introduces or relies on, and feeds them into the wiki. Product-specific explanations (architecture, API, deployment, etc.) belong in the product folders — the wiki only gets reusable knowledge.

## Scope

**Wiki pages created:** Only `Wiki/Concepts/` and `Wiki/Tools/` pages.

No Summary, Entity, Figure, Analysis, or Comparison pages. The product itself is not a wiki page — its documentation lives in `Products/<Name>/`.

**Source file:** Do NOT create a source file in `Sources/` unless the product has no readable documentation in either Vault or Base (i.e., you need to persist extracted content that would otherwise be lost). In the normal case, read directly from the product folders and proceed — the product folders *are* the source.

## Workflow

### Step 1: Identify the Product

1. The user provides a product name (e.g., "ControlPlane", "InfraKeeper", "Fluxy")
2. Verify the product exists:
   - `~/Vault/Products/<Name>/` — Obsidian side (overview MoC, symlinked docs)
   - `~/Base/Products/<Name>/` — Codebase side (source code, original docs)
3. If only one location exists, proceed with what's available
4. If neither exists, list available products from both directories

### Step 2: Read Product Documentation

Read content from both sides in parallel where possible:

**From Vault (`~/Vault/Products/<Name>/`):**
- The overview MoC file: `<Name>.md` — contains frontmatter and the catalog of linked content

**From Base (`~/Base/Products/<Name>/`):**
- `README.md` — primary project description
- `docs/` or `doc/` — key documentation files (overview, architecture, core concepts)
- `package.json`, `Cargo.toml`, `go.mod`, or similar — for tech stack identification
- `AGENTS.md`, `CONTRIBUTING.md` — for workflow and tooling context

**For large docs folders (>20 files):** Focus on overview, architecture, and core concepts. Ask the user which areas to deep-dive.

### Step 3: First Inspection

Present a narrative first inspection focused on:
- What **concepts** the product introduces or heavily relies on (design patterns, paradigms, protocols, techniques)
- What **tools** it uses, integrates with, or provides (CLI tools, libraries, frameworks, services)
- Potential connections to existing wiki content (search `Wiki/Index.md`)

Be straight to the point. The goal is to agree on which concepts and tools deserve wiki pages.

### Step 4: Discussion

Wait for the user's input. Align on:
- Which concepts deserve their own wiki pages vs. are too product-specific
- Which tools are general-purpose enough for the wiki vs. product-internal
- Connections to existing wiki pages

**Do not proceed until the user confirms.**

### Step 5: Create/Update Wiki Pages

Based on the discussion, create or update only:

1. **Concept pages** in `Wiki/Concepts/` — for ideas, patterns, paradigms, techniques that are reusable beyond this product
2. **Tool pages** in `Wiki/Tools/` — for CLI tools, libraries, frameworks, services that exist independently of this product

For each page:
- Check if it already exists (search `Wiki/Index.md` and use Glob)
- If it exists, update with new information — add a source reference to the product, merge content, update `updated:` date
- If new, create with full frontmatter per page conventions
- In `sources:`, reference the product overview: `"[[Products/<Name>/<Name>]]"`
- Use `[[wiki-links]]` for all internal references
- Set appropriate `confidence` level

### Step 6: Update Index & Log

- Update `Wiki/Index.md` — add/update rows for all pages created or modified
- Append entry to `Wiki/Log.md`

### Step 7: Git Commit & Push

Stage all changed files, commit with a meaningful message, push to remote.

## Notes

- The product's own documentation is the authoritative source — don't duplicate product-specific content into wiki pages. Wiki concepts should be written so they make sense independently of the product.
- A concept page may mention the product as an example or implementation, but should not be *about* the product.
- A tool page should describe the tool generally, noting that the product uses/provides it as context.
