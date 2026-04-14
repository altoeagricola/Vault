#!/usr/bin/env python3
"""
Extract YouTube video transcript and metadata for creating Obsidian notes.
Requires: youtube-transcript-api
Install: pip install youtube-transcript-api --break-system-packages
"""

import sys
import json
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url_or_id):
    """Extract video ID from YouTube URL or return ID if already provided."""
    # If it's already just an ID (11 characters, alphanumeric with dash/underscore)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Parse various YouTube URL formats
    parsed_url = urlparse(url_or_id)
    
    # Standard watch URL: youtube.com/watch?v=VIDEO_ID
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
        query_params = parse_qs(parsed_url.query)
        if 'v' in query_params:
            return query_params['v'][0]
    
    # Short URL: youtu.be/VIDEO_ID
    if parsed_url.hostname in ['youtu.be', 'www.youtu.be']:
        return parsed_url.path.lstrip('/')
    
    # Embed URL: youtube.com/embed/VIDEO_ID
    if '/embed/' in parsed_url.path:
        return parsed_url.path.split('/embed/')[1].split('?')[0]
    
    raise ValueError(f"Could not extract video ID from: {url_or_id}")


def get_transcript_with_timestamps(video_id):
    """Fetch transcript with timestamps from YouTube."""
    try:
        # New API (v1.0.0+): instantiate then use list() and fetch()
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)

        # Find best transcript: prefer manual English, then auto English, then any
        manual_en = None
        auto_en = None
        fallback = None

        for transcript in transcript_list:
            if transcript.language_code.startswith('en'):
                if not transcript.is_generated:
                    manual_en = transcript
                else:
                    auto_en = transcript
            if fallback is None:
                fallback = transcript

        # Select best available
        selected = manual_en or auto_en or fallback
        if selected is None:
            raise Exception("No transcripts available for this video")

        entries = api.fetch(video_id, languages=[selected.language_code])

        return {
            'entries': entries,
            'language': selected.language_code,
            'is_auto_generated': selected.is_generated
        }
    except Exception as e:
        raise Exception(f"Could not fetch transcript: {str(e)}")


def format_timestamp(seconds):
    """Convert seconds to MM:SS or HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def extract_youtube_data(video_url_or_id):
    """Main function to extract all YouTube data."""
    try:
        video_id = extract_video_id(video_url_or_id)
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        # Get transcript
        transcript_data = get_transcript_with_timestamps(video_id)
        
        # Format transcript with timestamps for analysis
        # New API returns dataclass objects with .text, .start, .duration attributes
        full_transcript = []
        for entry in transcript_data['entries']:
            timestamp = format_timestamp(entry.start)
            full_transcript.append(f"[{timestamp}] {entry.text}")

        # Also create a plain text version
        plain_transcript = ' '.join([entry.text for entry in transcript_data['entries']])
        
        return {
            'success': True,
            'video_id': video_id,
            'video_url': video_url,
            'transcript': {
                'timestamped': '\n'.join(full_transcript),
                'plain': plain_transcript,
                'language': transcript_data['language'],
                'is_auto_generated': transcript_data['is_auto_generated']
            }
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({
            'success': False,
            'error': 'Usage: python extract_youtube.py <youtube_url_or_video_id>'
        }))
        sys.exit(1)
    
    result = extract_youtube_data(sys.argv[1])
    print(json.dumps(result, indent=2))