#!/usr/bin/env bash
# Read an Obsidian note aloud using Edge TTS.
# Reads from stdin (piped note content) or a file path argument.
#
# Usage from Obsidian: pipe note content via stdin
# Usage from CLI:      tts-read.sh /path/to/note.md

set -euo pipefail

export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"

VOICE="${VOICE:-en-US-AvaNeural}"
RATE="${RATE:-+0%}"
AUDIO="/tmp/tts-read-$$.mp3"
PID_FILE="/tmp/tts-read.pid"

# Kill any previous TTS playback
if [[ -f "$PID_FILE" ]]; then
  prev_pid=$(cat "$PID_FILE" 2>/dev/null || true)
  if [[ -n "$prev_pid" ]] && kill -0 "$prev_pid" 2>/dev/null; then
    kill "$prev_pid" 2>/dev/null || true
    wait "$prev_pid" 2>/dev/null || true
  fi
  rm -f "$PID_FILE"
fi

cleanup() {
  rm -f "$AUDIO" "$PID_FILE"
}
trap cleanup EXIT

# Read content: from stdin if piped, otherwise from file argument
if [[ ! -t 0 ]]; then
  raw=$(cat)
elif [[ -n "${1:-}" && -f "$1" ]]; then
  raw=$(cat "$1")
else
  echo "No input. Pipe note content or pass a file path." >&2
  exit 1
fi

# Strip frontmatter, code blocks, wiki-link markup, HTML, and image embeds
text=$(echo "$raw" | sed -E '
  /^---$/,/^---$/d
  /^```/,/^```/d
  s/!\[\[([^]|]*)\|?[^]]*\]\]//g
  s/\[\[([^]|]*\|)?([^]]*)\]\]/\2/g
  s/<[^>]+>//g
  s/^[#]+[[:space:]]+//
  s/\*\*([^*]+)\*\*/\1/g
  s/\*([^*]+)\*/\1/g
  s/`[^`]+`//g
  s/^[-*] \[.\] //
  s/^[-*>] //
  /^[[:space:]]*$/d
')

if [[ -z "$text" ]]; then
  echo "No text to read." >&2
  exit 1
fi

# Generate audio and play
edge-tts --voice "$VOICE" --rate="$RATE" --text "$text" --write-media "$AUDIO" 2>/dev/null

afplay "$AUDIO" &
echo $! > "$PID_FILE"
echo "Reading aloud..."
wait $!
