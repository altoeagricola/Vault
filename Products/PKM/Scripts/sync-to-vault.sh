#!/usr/bin/env bash
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
# sync-to-vault.sh
# Symlinks all markdown files from ~/Base into ~/Vault, mirroring folder structure.
# - Skips ~/Base/Archive
# - Respects .gitignore automatically (uses fd)
# - Strips leading dots from folder names so hidden dirs appear in Obsidian
# - Creates destination folders as needed
# - Skips files that are already correctly symlinked
#
# Requires: fd (https://github.com/sharkdp/fd)

set -uo pipefail

BASE="$HOME/Base"
VAULT="$HOME/Vault"

created=0
skipped=0
errors=0
total=0
last_dir=""

echo "Syncing markdown files from $BASE -> $VAULT"
echo ""

while IFS= read -r src_file; do
    total=$((total + 1))
    rel_path="${src_file#$BASE/}"

    # Strip leading dots from folder names so hidden dirs are visible in Obsidian
    # e.g. Products/Foo/.github/docs/bar.md -> Products/Foo/github/docs/bar.md
    vault_rel_path="$(echo "$rel_path" | sed 's|/\.|/|g')"

    # Print current folder context when it changes
    current_dir="$(dirname "$vault_rel_path")"
    if [[ "$current_dir" != "$last_dir" ]]; then
        last_dir="$current_dir"
        echo ""
        echo "[$current_dir]"
    fi

    # README.md -> FolderName.md (Obsidian folder note convention)
    if [[ "$(basename "$vault_rel_path")" == "README.md" ]]; then
        folder_name="$(basename "$(dirname "$vault_rel_path")")"
        vault_rel_path="$(dirname "$vault_rel_path")/${folder_name}.md"
    fi

    dest_file="$VAULT/$vault_rel_path"
    dest_dir="$(dirname "$dest_file")"

    # Create destination directory if needed
    if [[ ! -d "$dest_dir" ]]; then
        mkdir -p "$dest_dir"
        echo "  MKDIR: $dest_dir"
    fi

    # Skip if already correctly symlinked
    if [[ -L "$dest_file" ]]; then
        existing_target="$(readlink "$dest_file")"
        if [[ "$existing_target" == "$src_file" ]]; then
            echo "  OK: $(basename "$rel_path")"
            skipped=$((skipped + 1))
            continue
        else
            echo "  RELINK: $(basename "$rel_path")"
            rm "$dest_file"
        fi
    elif [[ -e "$dest_file" ]]; then
        echo "  WARNING: $(basename "$rel_path") exists as regular file, skipping"
        errors=$((errors + 1))
        continue
    fi

    ln -s "$src_file" "$dest_file"
    echo "  LINKED: $(basename "$rel_path")"
    created=$((created + 1))

done < <(fd --type f --hidden --extension md --exclude Archive --absolute-path . "$BASE")

echo ""
echo "========================================="
echo "Done: $total processed, $created linked, $skipped skipped, $errors warnings"
