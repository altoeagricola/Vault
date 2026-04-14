---
title: git-delta
type: Tool
cover: "[[Wiki/Tools/_covers/git-delta.png]]"
sources:
related:
  - "[[lazygit]]"
  - "[[bat]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

delta is a syntax-highlighting pager for git diffs, blame, and grep output. It uses the same syntax themes as bat and adds features like side-by-side view, line numbers, word-level diff highlighting, and merge conflict rendering — making git output dramatically more readable.

## Use Cases

- **Better git diff output** — Syntax-highlighted diffs with word-level change detection
- **Side-by-side diffs** — Compare changes in a two-column layout
- **Syntax-highlighted blame** — Read git blame output with proper code highlighting
- **Navigate diffs** — Use n/N to jump between files in large diffs
- **Merge conflict style** — Render diff3-style merge conflicts with clear visual separation

## Examples

### Git config setup (~/.gitconfig)

```ini
[core]
    pager = delta

[interactive]
    diffFilter = delta --color-only

[delta]
    navigate = true
    line-numbers = true
    syntax-theme = Dracula

[merge]
    conflictstyle = diff3

[diff]
    colorMoved = default
```

### Side-by-side mode

```ini
[delta]
    side-by-side = true
    line-numbers-left-format = "{nm:>4} "
    line-numbers-right-format = "{np:>4} "
```

### Command-line usage

```bash
# Use delta directly
diff file1 file2 | delta

# Side-by-side from CLI
git diff | delta --side-by-side
```

## Links

- **Repository:** https://github.com/dandavison/delta
- **Documentation:** https://dandavison.github.io/delta/
