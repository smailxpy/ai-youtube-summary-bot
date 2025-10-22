import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from youtube_utils import extract_video_id, get_youtube_transcript
from ai_utils import summarize_text, transcribe_audio_from_youtube

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("❌ BOT_TOKEN not found. Add it in .env file.")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
@dp.message(Command("help"))
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Hi! Send me a YouTube link, and I’ll give you key insights and summaries using AI."
    )

@dp.message()
async def handle_youtube_link(message: types.Message):
    url = message.text.strip()
    video_id = extract_video_id(url)

    if not video_id:
        await message.answer("❌ Please send a valid YouTube link.")
        return

    await message.answer("⏳ Analyzing video... Please wait a moment.")

    # Try to get transcript
    transcript_text = get_youtube_transcript(video_id)

    if "Error" in transcript_text or "❌" in transcript_text:
        await message.answer("⚠️ No captions found. Using Whisper to transcribe audio...")
        transcript_text = transcribe_audio_from_youtube(url)

    # If Whisper also failed
    if transcript_text.startswith("❌"):
        await message.answer(transcript_text)
        return

    await message.answer("🧠 Summarizing the key points with AI...")

    summary = summarize_text(transcript_text)

    await message.answer(f"✅ Summary ready:\n\n{summary}")

async def main():
    print("🚀 Bot is running... Press Ctrl+C to stop.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
