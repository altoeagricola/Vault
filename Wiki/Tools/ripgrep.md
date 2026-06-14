---
title: ripgrep
type: Tool
cover: "[[Wiki/Tools/_covers/ripgrep.png]]"
sources:
  - InfraKeeper
related:
  - "[[fd]]"
  - "[[fzf]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

ripgrep (rg) is a line-oriented search tool that recursively searches directories for regex patterns at extremely high speed. It automatically respects `.gitignore` rules, skips binary files, and supports Unicode — making it the go-to replacement for grep in modern development workflows.

## Use Cases

- **Search codebases fast** — Orders of magnitude faster than grep on large repositories
- **Respect .gitignore** — Automatically skips ignored files, hidden directories, and binaries
- **Search specific file types** — Built-in type filters for dozens of languages and formats
- **JSON output for scripting** — Machine-readable output for integration with other tools
- **Context-aware results** — Show surrounding lines for better understanding of matches

## Examples

### Basic search

```bash
# Search for a pattern recursively
rg "TODO"

# Search with context (3 lines before and after)
rg -C3 "error handling"

# List only files containing matches
rg -l "import pandas"
```

### Filtered search

```bash
# Search only Python files
rg -t py "def main"

# Search with glob pattern
rg --glob '*.yaml' "replicas"

# Ignore a directory
rg --glob '!node_modules' "useState"
```

### Advanced usage

```bash
# JSON output for scripting
rg --json "pattern" | jq '.data.lines.text'

# Multiline search
rg -U "fn main.*\{[^}]*unwrap"

# Replace text (preview)
rg "old_name" --replace "new_name"
```

## Links

- **Repository:** https://github.com/BurntSushi/ripgrep
- **Documentation:** https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md
