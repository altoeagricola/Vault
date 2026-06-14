---
title: eza
type: Tool
cover: "[[Wiki/Tools/_covers/eza.png]]"
sources:
  - InfraKeeper
related:
  - "[[bat]]"
  - "[[fd]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

eza is a modern replacement for `ls` that adds file-type icons, color coding, Git status per file, tree view, and extended metadata display. It is a maintained fork of the original exa project, actively developed with community contributions.

## Use Cases

- **List files with icons and colors** — Instantly distinguish file types with Nerd Font icons and color coding
- **Show git status per file** — See staged, modified, and untracked status alongside file listings
- **Tree view** — Visualize directory structure without needing a separate tree command
- **Extended attributes** — Display file sizes, permissions, dates, and owners in a readable format
- **Group-by-type listing** — Separate directories from files for cleaner navigation

## Examples

### Common listing commands

```bash
# List with icons and colors
eza --icons

# Long listing with git status
eza -la --git

# Group directories first
eza --group-directories-first --icons
```

### Tree view

```bash
# Tree with 2 levels of depth
eza --tree --level=2 --icons

# Tree with git status
eza --tree --level=3 --git --icons
```

### Filtering and sorting

```bash
# Sort by modification time (newest first)
eza -la --sort=modified --reverse

# Show only directories
eza -D

# Show file sizes in binary units
eza -la --binary
```

## Links

- **Official site:** https://eza.rocks
- **Repository:** https://github.com/eza-community/eza
- **Documentation:** https://eza.rocks/
