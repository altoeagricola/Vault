---
title: Atuin
type: Tool
cover: "[[Wiki/Tools/_covers/atuin.png]]"
sources:
  - InfraKeeper
related:
  - "[[fzf]]"
  - "[[Zinit]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Atuin replaces your existing shell history with a SQLite database, providing full-text search across your entire command history with optional encrypted sync between machines. It transforms Ctrl+R from a basic reverse search into a powerful, context-aware history explorer with fuzzy matching, session filtering, and exit-code awareness.

## Use Cases

- **Full-text history search** — Fuzzy-match against your entire shell history, not just prefix matching
- **Cross-machine sync** — Encrypted history sync across all your workstations via Atuin's server or self-hosted instance
- **Replace Ctrl+R** — Interactive TUI replaces the default reverse search with richer filtering (by directory, session, exit code)
- **Audit command usage** — Query history statistics to understand usage patterns and find forgotten commands
- **Import existing history** — Pull in history from bash, zsh, or fish to avoid starting from scratch

## Examples

### Search history interactively

```bash
# Launch interactive search (replaces Ctrl+R)
atuin search -i

# Search for a specific pattern
atuin search "docker compose"

# Filter by directory
atuin search --cwd /home/user/project "make"
```

### Sync setup

```bash
# Register and login to sync server
atuin register -u username -e email@example.com -p password
atuin login -u username -p password

# Sync history
atuin sync
```

### Statistics and history info

```bash
# Show history stats
atuin stats

# Show recent history
atuin history list --cmd-only
```

## Links

- **Official site:** https://atuin.sh
- **Repository:** https://github.com/atuinsh/atuin
- **Documentation:** https://docs.atuin.sh
