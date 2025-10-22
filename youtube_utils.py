# youtube_utils.py
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    """
    Extracts the 11-character YouTube video ID from a given URL.
    """
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be\/([0-9A-Za-z_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_youtube_transcript(video_id: str) -> str:
    """
    Fetch the transcript text for a given YouTube video ID.
    Works with your version of youtube-transcript-api.
    """
    try:
        api = YouTubeTranscriptApi()
        transcript_snippets = api.fetch(video_id)

        # Join text correctly depending on object type
        text = " ".join([getattr(entry, "text", str(entry)) for entry in transcript_snippets])

        if not text.strip():
            return "❌ No transcript text found."
        return text
    except Exception as e:
        return f"❌ Error getting transcript: {e}"
