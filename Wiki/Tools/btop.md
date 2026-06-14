---
title: btop
type: Tool
cover: "[[Wiki/Tools/_covers/btop.png]]"
sources:
  - InfraKeeper
related:
  - "[[htop]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

btop (btop++) is a resource monitor that shows CPU, memory, disks, network, and processes in a rich, dashboard-style TUI with mouse support, themes, and GPU monitoring. It provides a more comprehensive system overview than htop, combining multiple monitoring views into a single interface.

## Use Cases

- **Full system monitoring dashboard** — CPU, memory, disk, and network in one view
- **GPU monitoring** — Track GPU usage, temperature, and memory (NVIDIA, AMD, Intel)
- **Per-core CPU usage** — Detailed per-core utilization graphs with temperature readings
- **Network bandwidth** — Real-time upload/download speed with historical graphs
- **Disk I/O monitoring** — Track read/write activity across mounted disks

## Examples

### Launch and navigation

```bash
# Launch btop
btop

# Launch with a specific theme
btop --theme dracula
```

### Keybindings

```
Esc    — Main menu / Back
F2/o   — Options
F1/?   — Help
f      — Filter processes
Tab    — Cycle process sorting
e      — Toggle tree view
m      — Toggle memory display mode
n      — Toggle network display mode
d      — Toggle disk display mode
```

### Configuration

Config is stored at `~/.config/btop/btop.conf`. Themes are stored in `~/.config/btop/themes/`.

```ini
# Key config options
color_theme = "dracula"
shown_boxes = "cpu mem net proc"
update_ms = 1000
proc_sorting = "cpu lazy"
```

## Links

- **Repository:** https://github.com/aristocratos/btop
- **Documentation:** https://github.com/aristocratos/btop#usage
