#!/usr/bin/env bash
# Pre-flight check for agents before any Vault ingestion or wiki write.
set -euo pipefail

VAULT_ROOT="/Users/okumaaltoe/AltoèAgricola.Vault"
PWD_REAL="$(pwd -P)"
VAULT_REAL="$(cd "$VAULT_ROOT" && pwd -P)"

if python3 - "$PWD_REAL" "$VAULT_REAL" <<'PY'
import os
import sys

current = os.path.abspath(sys.argv[1])
vault = os.path.abspath(sys.argv[2])

while True:
    if os.path.samefile(current, vault):
        sys.exit(0)
    parent = os.path.dirname(current)
    if parent == current:
        sys.exit(1)
    current = parent
PY
then
  exit 0
fi

cat >&2 <<EOF
Refusing to continue outside the Obsidian Vault.

Current directory: $PWD_REAL
Expected Vault:    $VAULT_REAL

Run from the Vault root before ingesting or writing notes:
cd "$VAULT_REAL"
EOF

exit 2
