---
title: glow
type: Tool
cover: "[[Wiki/Tools/_covers/glow.png]]"
sources:
related:
  - "[[bat]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

glow is a terminal-based Markdown renderer from Charm that renders Markdown files with glamour styling — headings, code blocks, lists, and links all get proper formatting and color. It can render local files, pipe input, or browse a stash of bookmarked documents.

## Use Cases

- **Render README in terminal** — Read project documentation without leaving the CLI
- **Browse local markdown files** — Navigate and render markdown files interactively
- **Stash and bookmark documents** — Save frequently referenced documents for quick access
- **Pipe markdown** — Render markdown from any source piped through stdin

## Examples

### Basic rendering

```bash
# Render a file
glow README.md

# Render with pager (scrollable)
glow -p README.md

# Pipe markdown content
echo "# Hello\n\nThis is **bold**" | glow

# Use a specific style
glow -s dark README.md
```

### Browse and stash

```bash
# Browse markdown files in current directory
glow

# Stash a document for later
glow stash README.md

# Browse stashed documents
glow stash
```

### Width control

```bash
# Set max render width
glow -w 80 README.md
```

## Links

- **Repository:** https://github.com/charmbracelet/glow
- **Documentation:** https://github.com/charmbracelet/glow#usage
