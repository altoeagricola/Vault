Mirrors all markdown files from `~/Base` into `~/Vault` as symlinks, making codebases and product documentation visible in Obsidian without duplication.

## Why

The `~/Base` directory contains product codebases with markdown documentation (READMEs, ADRs, guides). Obsidian can only index files inside its vault directory. Symlinks bridge this gap: the source of truth stays in `~/Base` (version-controlled per repo), while Obsidian sees and indexes the content in `~/Vault`.

## How it works

1. `fd` finds all `.md` files under `~/Base`, respecting `.gitignore` and excluding `Archive/`
2. For each file, the script:
   - Strips leading dots from folder names (`.github/` becomes `github/`) so hidden dirs appear in Obsidian
   - Renames `README.md` to the parent folder name (Obsidian folder note convention)
   - Creates destination directories as needed
   - Creates a symlink if one doesn't already exist, or relinks if the target changed
   - Skips regular files to avoid overwriting manual content

## Command

| Command palette entry | What it does |
|---|---|
| **Execute: Sync MDs from Base** | Runs the sync and shows a summary notification |

## Files

| File | Path |
|---|---|
| `sync-to-vault.sh` | `~/Vault/Products/PKM/Scripts/sync-to-vault.sh` |

## Dependencies

- [`fd`](https://github.com/sharkdp/fd) — fast file finder, installed via Homebrew
- Obsidian Shell Commands plugin

## Shell Commands integration notes

The script is called directly without a shell wrapper. Obsidian does not inherit the user's shell profile, so the script explicitly sets `PATH` to include `/opt/homebrew/bin` (where `fd` lives) at the top:

```bash
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
```

This is the standard pattern for any shell command triggered from Obsidian — always set PATH explicitly in the script rather than relying on login shell initialization.
