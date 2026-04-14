#!/usr/bin/env bash
# Validates that wiki pages written by the agent have required frontmatter fields.
# Claude Code PreToolUse hook for Edit|Write on Wiki/ files.
#
# Receives JSON on stdin with tool_input.file_path and tool_input.content.
# Exit 0 = allow, Exit 2 = block (reason on stderr).
set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null || echo "")

# Skip Index.md, Log.md, and .gitkeep files
case "$FILE_PATH" in
  */Wiki/Index.md|*/Wiki/Log.md|*/.gitkeep)
    exit 0
    ;;
esac

# For Edit tool, we get old_string/new_string not full content — skip validation
# (we can only validate full writes, not partial edits)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null || echo "")
if [ "$TOOL_NAME" = "Edit" ]; then
  exit 0
fi

# Extract content for Write tool
CONTENT=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('content',''))" 2>/dev/null || echo "")

if [ -z "$CONTENT" ]; then
  exit 0
fi

# Check for frontmatter opening
if ! echo "$CONTENT" | head -1 | grep -q "^---"; then
  echo "Wiki page $FILE_PATH is missing YAML frontmatter (must start with ---)" >&2
  exit 2
fi

# Extract frontmatter block
FRONTMATTER=$(echo "$CONTENT" | sed -n '1,/^---$/p' | tail -n +2)

REQUIRED_FIELDS=("title:" "type:" "created:" "updated:" "confidence:")
MISSING=()

for field in "${REQUIRED_FIELDS[@]}"; do
  if ! echo "$FRONTMATTER" | grep -q "^${field}"; then
    MISSING+=("$field")
  fi
done

if [ ${#MISSING[@]} -gt 0 ]; then
  echo "Wiki page $FILE_PATH is missing required frontmatter: ${MISSING[*]}" >&2
  exit 2
fi

# Validate type value
TYPE_VALUE=$(echo "$FRONTMATTER" | grep "^type:" | head -1 | sed 's/^type:[[:space:]]*//')
VALID_TYPES="Concept Entity Figure Tool Summary Analysis Comparison Insight"
if ! echo "$VALID_TYPES" | grep -qw "$TYPE_VALUE"; then
  echo "Wiki page $FILE_PATH has invalid type '$TYPE_VALUE'. Must be one of: $VALID_TYPES" >&2
  exit 2
fi

exit 0
