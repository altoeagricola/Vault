---
title: bat
type: Tool
cover: "[[Wiki/Tools/_covers/bat.png]]"
sources:
  - InfraKeeper
related:
  - "[[fzf]]"
  - "[[git-delta]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

bat is a `cat` replacement with syntax highlighting for over 200 languages, automatic paging, line numbers, and Git integration that shows modifications inline. It brings the readability of a code editor to the terminal while remaining fully compatible with cat's piping behavior.

## Use Cases

- **View files with syntax highlighting** — Automatic language detection with rich color themes
- **Show git changes inline** — Highlight added, modified, and removed lines directly in file output
- **cat replacement** — Drop-in replacement that falls back to plain output when piped
- **fzf preview pane** — Provide syntax-highlighted file previews in fzf workflows
- **Concatenate with style** — View multiple files with headers and decorations

## Examples

### Basic usage

```bash
# View a file with syntax highlighting
bat src/main.py

# Force a specific language
bat -l json data.txt

# Plain output (no decorations, useful for piping)
bat --style=plain config.yaml

# Show only line numbers and content
bat --style=numbers Makefile
```

### Git integration

```bash
# Show modified lines alongside content
bat --diff README.md

# Show all modified files with changes
git diff --name-only | xargs bat --diff
```

### Integration with fzf

```bash
# fzf with bat preview
fzf --preview 'bat --color=always --style=numbers --line-range :500 {}'
```

## Links

- **Repository:** https://github.com/sharkdp/bat
- **Documentation:** https://github.com/sharkdp/bat#how-to-use
