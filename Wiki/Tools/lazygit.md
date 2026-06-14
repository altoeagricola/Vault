---
title: lazygit
type: Tool
cover: "[[Wiki/Tools/_covers/lazygit.png]]"
sources:
  - InfraKeeper
related:
  - "[[git-delta]]"
  - "[[gh]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

lazygit is a terminal UI for git that makes complex git operations intuitive and fast. It provides interactive staging, visual rebase, branch management, and conflict resolution through a keyboard-driven interface — reducing multi-command git workflows to a few keystrokes.

## Use Cases

- **Interactive staging** — Stage individual lines or hunks without touching `git add -p`
- **Visual interactive rebase** — Reorder, squash, fixup, and edit commits with simple keybindings
- **Branch management** — Create, checkout, merge, rebase, and delete branches visually
- **Conflict resolution** — Navigate and resolve merge conflicts with clear visual diffs
- **Cherry-pick and bisect** — Visual workflows for cherry-picking commits and bisecting regressions

## Examples

### Launch and basic navigation

```bash
# Launch in current repo
lazygit

# Launch in a specific repo
lazygit -p /path/to/repo
```

### Key panels and keybindings

```
Tab / number keys — switch panels (Status, Files, Branches, Commits, Stash)
Space — stage/unstage file
c     — commit
p     — pull
P     — push
b     — create branch
r     — rebase
s     — squash commit
e     — edit commit message
```

### Custom config (~/.config/lazygit/config.yml)

```yaml
gui:
  theme:
    selectedLineBgColor:
      - reverse
  showIcons: true
git:
  paging:
    colorArg: always
    pager: delta --dark --paging=never
```

## Links

- **Repository:** https://github.com/jesseduffield/lazygit
- **Documentation:** https://github.com/jesseduffield/lazygit#keybindings
