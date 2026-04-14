---
title: Zinit
type: Tool
cover: "[[Wiki/Tools/_covers/zinit.png]]"
sources:
related:
  - "[[Starship]]"
  - "[[fzf]]"
  - "[[Atuin]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Zinit is a flexible and fast zsh plugin manager with turbo mode for deferred loading, annexes for extended functionality, and the ability to install not just zsh plugins but also binaries directly from GitHub releases. Its lazy-loading capabilities keep shell startup times under 100ms even with dozens of plugins.

## Use Cases

- **Manage zsh plugins** — Install and update plugins from GitHub, Oh My Zsh, or Prezto
- **Lazy-load for fast startup** — Turbo mode defers plugin loading until after the prompt appears
- **Install completions** — Automatically manage and compile zsh completion files
- **Install binaries from GitHub releases** — Download and install CLI tools directly from release assets
- **Snippet loading** — Load individual files from repos or URLs without cloning entire repositories

## Examples

### Basic plugin loading

```zsh
# Light loading (no tracking)
zinit light zsh-users/zsh-autosuggestions

# Regular loading with reporting
zinit load zsh-users/zsh-syntax-highlighting
```

### Turbo mode (deferred loading)

```zsh
# Load after prompt with wait ice
zinit ice wait lucid
zinit light zsh-users/zsh-autosuggestions

zinit ice wait lucid atload"_zsh_autosuggest_start"
zinit light zsh-users/zsh-completions
```

### Install binaries from GitHub releases

```zsh
# Install a binary from GitHub release assets
zinit ice from"gh-r" as"program"
zinit light junegunn/fzf

zinit ice from"gh-r" as"program" mv"fd* -> fd" pick"fd/fd"
zinit light sharkdp/fd

zinit ice from"gh-r" as"program" mv"bat* -> bat" pick"bat/bat"
zinit light sharkdp/bat
```

### Snippet loading

```zsh
# Load a single file from Oh My Zsh
zinit snippet OMZP::git
zinit snippet OMZP::docker-compose
```

## Links

- **Repository:** https://github.com/zdharma-continuum/zinit
- **Documentation:** https://github.com/zdharma-continuum/zinit#introduction
