# ai_utils.py
# ai_utils.py
import os
from dotenv import load_dotenv
load_dotenv()

import tempfile
from openai import OpenAI
from pytube import YouTube

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, max_chars: int = 5000) -> str:
    ...

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, max_chars: int = 5000) -> str:
    """
    Summarize a given transcript text into key points using GPT-4-mini.
    """
    try:
        if len(text) > max_chars:
            text = text[:max_chars]  # prevent too long input

        prompt = (
            "You are an assistant that summarizes YouTube videos.\n"
            "Summarize this text into clear bullet points and main ideas:\n\n"
            f"{text}"
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
        )

        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"❌ Error summarizing text: {e}"


def transcribe_audio_from_youtube(url: str) -> str:
    """
    Download audio from YouTube and transcribe it using Whisper (OpenAI).
    Used when no transcript is available.
    """
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as tmp_file:
            audio_stream.download(filename=tmp_file.name)
            with open(tmp_file.name, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
                return transcript.text
    except Exception as e:
        return f"❌ Error transcribing audio: {e}"
