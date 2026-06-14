---
title: fzf
type: Tool
cover: "[[Wiki/Tools/_covers/fzf.png]]"
sources:
  - InfraKeeper
related:
  - "[[fd]]"
  - "[[bat]]"
  - "[[ripgrep]]"
  - "[[Zinit]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

fzf is a general-purpose command-line fuzzy finder that can be used to interactively filter any list — files, command history, processes, git branches, or anything piped to stdin. Its speed (written in Go) and composability make it a cornerstone of productive terminal workflows.

## Use Cases

- **Fuzzy file search (Ctrl+T)** — Quickly find and insert file paths into the current command
- **Interactive history search (Ctrl+R)** — Replace the default reverse search with fuzzy matching across full command history
- **Directory navigation (Alt+C)** — Jump to any subdirectory with fuzzy matching
- **Pipe any list through fzf** — Interactively filter process lists, git branches, Kubernetes pods, or any text stream
- **Preview integration** — Combine with bat for syntax-highlighted file previews while browsing

## Examples

### Basic usage and shell keybindings

```bash
# Fuzzy find files in current directory
fzf

# Ctrl+R — fuzzy search shell history
# Ctrl+T — fuzzy find file and paste path
# Alt+C  — fuzzy cd into subdirectory
```

### Piping and filtering

```bash
# Filter processes
ps aux | fzf

# Switch git branch interactively
git branch | fzf | xargs git checkout

# Kill a process interactively
kill -9 $(ps aux | fzf | awk '{print $2}')
```

### Preview with bat

```bash
# Browse files with syntax-highlighted preview
fzf --preview 'bat --color=always --style=numbers {}'

# Use fd as the source for better file listing
fd --type f | fzf --preview 'bat --color=always {}'
```

## Links

- **Official site:** https://junegunn.github.io/fzf/
- **Repository:** https://github.com/junegunn/fzf
- **Documentation:** https://junegunn.github.io/fzf/
