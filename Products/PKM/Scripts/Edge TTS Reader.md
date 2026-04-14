Reads the current Obsidian note aloud using Microsoft Edge's neural text-to-speech voices.

## Why

The [Edge TTS Obsidian plugin](https://github.com/travisvn/obsidian-edge-tts) stopped working reliably after Microsoft began blocking the browser WebSocket workaround it depends on (December 2025 onwards). This shell-based solution uses the actively maintained [`edge-tts`](https://github.com/rany2/edge-tts) Python CLI, which handles Microsoft's API changes and authentication tokens independently.

## How it works

1. Obsidian's Shell Commands plugin pipes the current note content (`{{note_content}}`) via stdin to `tts-read.sh`
2. The script strips YAML frontmatter, code blocks, wiki-link markup, HTML tags, image embeds, and markdown formatting
3. `edge-tts` generates an MP3 via Microsoft's TTS API with word-level timing
4. `afplay` (macOS) plays the audio in the background
5. The playback PID is tracked in `/tmp/tts-read.pid` so it can be stopped

## Commands

| Command palette entry | What it does |
|---|---|
| **Execute: Read note aloud (Edge TTS)** | Reads the active note. Stops any previous playback first. |
| **Execute: Stop TTS playback** | Stops the current reading. |

## Configuration

Edit `tts-read.sh` or set environment variables:

| Variable | Default | Description |
|---|---|---|
| `VOICE` | `en-US-AvaNeural` | Microsoft Edge voice identifier |
| `RATE` | `+0%` | Speed adjustment (`-50%` to `+100%`) |

Browse available voices with `edge-tts --list-voices`.

## Files

| File | Purpose |
|---|---|
| `tts-read.sh` | Main reader script |
| `tts-stop.sh` | Stops active playback |

## Dependencies

- `edge-tts` Python CLI — installed via `pipx install edge-tts`
- `afplay` — built into macOS
- Obsidian Shell Commands plugin

## CLI usage

```bash
# Read a file directly
./tts-read.sh ~/Vault/Wiki/Concepts/SomeConcept.md

# Pipe content
cat note.md | ./tts-read.sh

# Custom voice and speed
VOICE="en-GB-SoniaNeural" RATE="+20%" ./tts-read.sh note.md
```
