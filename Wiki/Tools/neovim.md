---
title: neovim
type: Tool
cover: "[[Wiki/Tools/_covers/neovim.png]]"
sources:
  - InfraKeeper
related:
  - "[[tmux]]"
  - "[[lazygit]]"
  - "[[ripgrep]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Neovim is a hyperextensible, Vim-based text editor that adds first-class Lua scripting, built-in LSP support, tree-sitter parsing, and an asynchronous plugin architecture. It modernizes Vim while maintaining full backward compatibility, making it the foundation for highly customized, IDE-like terminal editing environments.

## Use Cases

- **Code editing with LSP** — Built-in Language Server Protocol client for completions, diagnostics, go-to-definition, and refactoring
- **Lua-based configuration** — Replace Vimscript with Lua for faster, more maintainable config
- **Plugin ecosystem** — Rich ecosystem managed by lazy.nvim, with plugins for everything from file trees to AI completion
- **Terminal integration** — Built-in terminal emulator for running commands without leaving the editor
- **Remote editing** — Edit files on remote machines via SSH with native client-server architecture

## Examples

### Basic usage

```bash
# Open a file
nvim src/main.py

# Open multiple files in splits
nvim -O file1.py file2.py

# Open at a specific line
nvim +42 config.yaml
```

### init.lua basics

```lua
-- ~/.config/nvim/init.lua

-- Basic settings
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.clipboard = "unnamedplus"

-- Leader key
vim.g.mapleader = " "

-- Keymaps
vim.keymap.set("n", "<leader>w", ":w<CR>")
vim.keymap.set("n", "<leader>q", ":q<CR>")
```

### Plugin manager (lazy.nvim)

```lua
-- Bootstrap lazy.nvim, then:
require("lazy").setup({
  "nvim-telescope/telescope.nvim",
  "nvim-treesitter/nvim-treesitter",
  "neovim/nvim-lspconfig",
  "hrsh7th/nvim-cmp",
  { "catppuccin/nvim", name = "catppuccin" },
})
```

## Links

- **Official site:** https://neovim.io
- **Repository:** https://github.com/neovim/neovim
- **Documentation:** https://neovim.io/doc/
