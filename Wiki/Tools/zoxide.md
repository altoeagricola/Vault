---
title: zoxide
type: Tool
cover: "[[Wiki/Tools/_covers/zoxide.png]]"
sources:
  - InfraKeeper
related:
  - "[[fzf]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

zoxide is a smarter `cd` command that learns your most frequently and recently visited directories, letting you jump to them with partial name matches. It uses a ranking algorithm (frecency) to prioritize results, eliminating the need to type full paths.

## Use Cases

- **Jump to frequent directories** — Type a partial name and zoxide resolves it to the most likely directory
- **Replace cd** — Drop-in replacement that works exactly like cd but with smart matching
- **Fuzzy directory matching** — Match against any part of the path, not just the final component
- **Interactive directory selection** — Use `zi` with fzf integration for ambiguous matches

## Examples

### Basic navigation

```bash
# Jump to a directory by partial match
z project
z vault

# Jump with multiple keywords (narrows results)
z home config

# Interactive selection with fzf
zi
```

### Management commands

```bash
# Add a directory manually
zoxide add /path/to/dir

# Query the database
zoxide query project

# Remove a directory from the database
zoxide remove /old/path

# List all entries with scores
zoxide query --list
```

### Shell init (add to .zshrc)

```bash
eval "$(zoxide init zsh)"
```

## Links

- **Repository:** https://github.com/ajeetdsouza/zoxide
- **Documentation:** https://github.com/ajeetdsouza/zoxide#usage
