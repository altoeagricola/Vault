---
title: fd
type: Tool
cover: "[[Wiki/Tools/_covers/fd.png]]"
sources:
  - InfraKeeper
related:
  - "[[ripgrep]]"
  - "[[fzf]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

fd is a fast and user-friendly alternative to `find` that provides sensible defaults, colorized output, and smart case matching. Like ripgrep, it respects `.gitignore` by default and is significantly faster than the traditional `find` command.

## Use Cases

- **Find files by name pattern** — Regex-based file search with smart case sensitivity
- **Find by extension** — Quickly locate all files of a specific type
- **Find and execute commands** — Run commands on matched files in parallel
- **Find recently modified files** — Filter by modification time for change tracking
- **Integrate with fzf** — Use fd as the file source for fzf's fuzzy finder

## Examples

### Basic file finding

```bash
# Find files matching a pattern
fd "config"

# Find by extension
fd -e py

# Find only directories
fd -t d "src"

# Include hidden and ignored files
fd -H -I "secret"
```

### Execute commands on results

```bash
# Run a command on each match
fd -e jpg -x convert {} {.}.png

# Parallel execution
fd -e rs -x wc -l

# Delete matched files
fd -e tmp -x rm
```

### Time-based filtering

```bash
# Files changed in the last day
fd --changed-within 1d

# Files older than 30 days
fd --changed-before 30d -e log
```

## Links

- **Repository:** https://github.com/sharkdp/fd
- **Documentation:** https://github.com/sharkdp/fd#how-to-use
