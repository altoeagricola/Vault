---
title: Homebrew
type: Tool
cover: "[[Wiki/Tools/_covers/homebrew.png]]"
sources:
  - InfraKeeper
related:
  - "[[Zinit]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Homebrew is the de facto package manager for macOS, providing a consistent way to install, update, and manage CLI tools, libraries, and GUI applications. It handles dependency resolution, version management, and cleanup, making it the foundation of most macOS developer setups.

## Use Cases

- **Install CLI tools** — One-command installation of developer utilities with automatic dependency resolution
- **Manage GUI applications via Casks** — Install and update desktop apps (browsers, editors, terminals) through the CLI
- **Keep everything updated** — Single command to upgrade all installed packages and casks
- **Tap third-party repositories** — Extend available formulae beyond the core with community and private taps
- **Reproducible environments with Brewfile** — Declare all packages in a `Brewfile` for consistent machine setup

## Examples

### Common package operations

```bash
# Install a CLI tool
brew install ripgrep

# Install a GUI application
brew install --cask firefox

# Upgrade all installed packages
brew upgrade

# Search for a package
brew search node
```

### Brewfile for reproducible setup

```ruby
# Brewfile
tap "homebrew/bundle"
brew "git"
brew "fzf"
brew "ripgrep"
brew "bat"
cask "iterm2"
cask "visual-studio-code"
```

```bash
# Install everything from Brewfile
brew bundle install

# Dump current installed packages to Brewfile
brew bundle dump --force
```

### Maintenance

```bash
# Remove old versions and clear cache
brew cleanup

# Check for potential problems
brew doctor
```

## Links

- **Official site:** https://brew.sh
- **Repository:** https://github.com/Homebrew/brew
- **Documentation:** https://docs.brew.sh
