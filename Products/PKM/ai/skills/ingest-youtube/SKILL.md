---
name: ingest-youtube
description: Extract key takeaways from YouTube videos and create well-structured Obsidian notes. Use this skill when the user provides a YouTube URL/link and wants to create a note with video insights, including proper formatting with tags, wiki-links for concepts/products/people, and organized sections. Triggers include "create a note from this YouTube video", "extract takeaways from video", "summarize YouTube video to Obsidian", or any request to process YouTube content into notes.
---

# You Tube Ingestion Skill

This skill extracts transcripts from YouTube videos, creates a source file in `Sources/Transcripts/`, and then follows the standard **Ingest workflow** defined in the vault's Instructions.

## Workflow

### Step 1: Extract Video Data

1. Run the extraction script:
   ```bash
   ${WORKSPACE_ROOT}/.venv/bin/python3 ./yt-transcript.py "<youtube_url>"
   ```

2. The script returns JSON with:
   - `video_id`: YouTube video ID
   - `video_url`: Full YouTube URL
   - `transcript.timestamped`: Transcript with timestamps
   - `transcript.plain`: Plain text transcript
   - `transcript.language`: Language code
   - `transcript.is_auto_generated`: Whether captions are auto-generated

3. If the script fails, inform the user that the video doesn't have transcripts enabled.

### Step 2: Create Source File

Create a markdown file in `Sources/Transcripts/` with this structure:

```markdown
---
title: "[Video Title]"
source: "[Channel Name]"
link: "[YouTube URL]"
video_id: "[Video ID]"
language: "[Language Code]"
auto_generated: [true/false]
created: YYYY-MM-DD
tags:
  - clippings
  - transcript
---

[Plain text transcript]
```

**Filename:** Use the video title, cleaned of special characters, under 60 characters.

### Step 3: Standard Ingest

Hand off to the `/ingest` skill, passing the source file path created in Step 2. The standard ingest skill handles: first inspection, discussion, wiki page creation, index/log updates, and git commit & push.

## Quality Guidelines

### Wiki-Link Creation
- Only create wiki-links for significant concepts, not every noun
- Use consistent naming (check existing notes when possible)
- Proper nouns maintain capitalization
- Technologies use official casing (e.g., `[[JavaScript]]`, `[[VS Code]]`)

### Transcript Attribution
- Always note if transcript is auto-generated (may have errors)
- Include language information in frontmatter
- Reference specific timestamps when highlighting key moments (link format: `[MM:SS](https://youtube.com/watch?v=VIDEO_ID&t=SECONDs)`)

## Dependencies

Requires `youtube-transcript-api`. Install if not present:
```bash
uv venv .venv && uv pip install youtube-transcript-api
```

## Error Handling

- **No transcript:** Inform user the video doesn't have captions
- **Invalid URL:** Ask for a valid YouTube link
- **Network errors:** Suggest retry
- **Private videos:** Explain API cannot access private content
