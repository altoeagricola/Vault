---
title: Starship
type: Tool
cover: "[[Wiki/Tools/_covers/starship.png]]"
sources:
  - InfraKeeper
related:
  - "[[Zinit]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Starship is a minimal, blazing-fast, cross-shell prompt written in Rust. It dynamically shows contextual information — git branch and status, active language versions, Docker context, Kubernetes cluster, command duration — without slowing down your shell. Configuration is a single TOML file.

## Use Cases

- **Show git branch and status** — Current branch, ahead/behind count, staged/unstaged changes at a glance
- **Display active language versions** — Automatically detect and show Python, Node, Rust, Go, etc. versions per directory
- **Docker and Kubernetes context** — Show active Docker context and Kubernetes cluster/namespace
- **Command duration** — Display how long the last command took when it exceeds a threshold
- **Custom modules** — Add custom segments for any environment information you need

## Examples

### Shell init (add to .zshrc)

```bash
eval "$(starship init zsh)"
```

### starship.toml configuration

```toml
# ~/.config/starship.toml

[character]
success_symbol = "[>](bold green)"
error_symbol = "[>](bold red)"

[directory]
truncation_length = 3
truncation_symbol = ".../"

[git_branch]
symbol = " "
format = "[$symbol$branch]($style) "

[git_status]
format = '([$all_status$ahead_behind]($style) )'

[python]
symbol = " "
format = '[$symbol$version(\($virtualenv\))]($style) '

[nodejs]
symbol = " "
format = "[$symbol$version]($style) "

[command_duration]
min_time = 2000
format = "took [$duration]($style) "
```

### Disable unused modules

```toml
[aws]
disabled = true

[gcloud]
disabled = true
```

## Links

- **Official site:** https://starship.rs
- **Repository:** https://github.com/starship/starship
- **Documentation:** https://starship.rs/config/
