---
title: tmux
type: Tool
cover: "[[Wiki/Tools/_covers/tmux.png]]"
sources:
  - InfraKeeper
related:
  - "[[neovim]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

tmux is a terminal multiplexer that lets you create persistent sessions with multiple windows and split panes, all within a single terminal connection. Sessions survive disconnections, making it essential for remote server work and complex multi-terminal workflows.

## Use Cases

- **Persistent remote sessions** — SSH sessions survive disconnections; reattach from anywhere
- **Split panes** — Divide the terminal into horizontal and vertical panes for parallel work
- **Window management** — Organize work across named windows within a session
- **Session sharing** — Multiple users can attach to the same session for pair programming
- **Scripted layouts** — Automate terminal layouts for repeatable development environments

## Examples

### Session management

```bash
# Create a named session
tmux new -s dev

# Detach from session
# Ctrl+b d

# List sessions
tmux list-sessions

# Reattach to a session
tmux attach -t dev

# Kill a session
tmux kill-session -t dev
```

### Pane and window keybindings (prefix: Ctrl+b)

```
%     — Split vertically
"     — Split horizontally
o     — Cycle through panes
x     — Close current pane
c     — Create new window
n/p   — Next/previous window
,     — Rename current window
z     — Toggle pane zoom (fullscreen)
```

### .tmux.conf basics

```bash
# Set prefix to Ctrl+a
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# Enable mouse support
set -g mouse on

# Start windows and panes at 1, not 0
set -g base-index 1
setw -g pane-base-index 1

# Better split keybindings
bind | split-window -h
bind - split-window -v
```

## Links

- **Official site:** https://github.com/tmux/tmux/wiki
- **Repository:** https://github.com/tmux/tmux
- **Documentation:** https://man7.org/linux/man-pages/man1/tmux.1.html
