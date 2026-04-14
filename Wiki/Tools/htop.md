---
title: htop
type: Tool
cover: "[[Wiki/Tools/_covers/htop.png]]"
related:
  - "[[btop]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

htop is an interactive process viewer for Unix systems that provides a real-time, color-coded overview of CPU, memory, and swap usage alongside a sortable, filterable process list. It is the standard upgrade from the venerable `top` command, available on virtually every Linux and macOS system.

## Use Cases

- **Monitor system resources** — Real-time CPU, memory, and swap usage with per-core breakdown
- **Kill processes** — Select and send signals to processes interactively
- **Sort by resource usage** — Quickly find processes consuming the most CPU or memory
- **Filter processes** — Search and filter the process list by name, user, or PID
- **Tree view** — Visualize parent-child process relationships

## Examples

### Launch and basic usage

```bash
# Launch htop
htop

# Monitor a specific process
htop -p 1234

# Show only processes for a user
htop -u edgar
```

### Keybindings

```
F5 — Tree view (toggle)
F6 — Sort by column
F9 — Kill process (select signal)
F4 — Filter by name
F3 — Search
/  — Incremental search
M  — Sort by memory
P  — Sort by CPU
t  — Toggle tree view
```

### Configuration

htop stores its config in `~/.config/htop/htoprc`. Settings changed via the Setup screen (F2) persist automatically.

## Links

- **Official site:** https://htop.dev
- **Repository:** https://github.com/htop-dev/htop
- **Documentation:** https://htop.dev/
