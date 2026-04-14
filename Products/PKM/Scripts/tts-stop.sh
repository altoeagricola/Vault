#!/usr/bin/env bash
# Stop any running TTS playback.
PID_FILE="/tmp/tts-read.pid"
stopped=false

# Kill tracked afplay process
if [[ -f "$PID_FILE" ]]; then
  pid=$(cat "$PID_FILE" 2>/dev/null || true)
  if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
    kill "$pid" 2>/dev/null || true
    stopped=true
  fi
  rm -f "$PID_FILE"
fi

# Also kill any stray afplay/edge-tts from our script
pkill -f "afplay /tmp/tts-read-" 2>/dev/null && stopped=true
pkill -f "edge-tts.*tts-read-" 2>/dev/null && stopped=true

if $stopped; then
  echo "Stopped TTS playback."
else
  echo "No active playback."
fi
