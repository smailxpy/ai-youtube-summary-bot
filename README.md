# 🤖 AI YouTube Summary Bot

A Telegram bot that **summarizes any YouTube video using AI** — powered by GPT-4-mini and Whisper.  
It automatically extracts the transcript or audio and gives you **key insights, main ideas, and shortcuts** from any video 📺💡

---

## 🚀 Features

- 🧠 **AI Summaries** – GPT-4-mini creates short, smart bullet-point summaries  
- 🎧 **Whisper Transcription** – if no captions exist, it transcribes the video audio  
- 🔗 **YouTube Integration** – just send a YouTube link to the bot  
- ⚙️ **Fast & Async** – built with Aiogram v3 for smooth Telegram performance  
- 💾 **Clean Code** – modular structure (`bot.py`, `ai_utils.py`, `youtube_utils.py`)  

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.9+ |
| **Framework** | Aiogram v3 |
| **AI Engine** | OpenAI GPT-4-mini & Whisper |
| **Tools** | youtube-transcript-api, pytube |
| **Env** | `.env` for API keys and bot token |

---

## ⚡ Setup & Run Locally

## 🧭 Future Roadmap

- [ ] Add Hugging Face fallback  
- [ ] Deploy on Render  
- [ ] Add Premium Mode  

### 1️⃣ Clone the repo
```bash
git clone https://github.com/smailxpy/ai-youtube-summary-bot.git
cd ai-youtube-summary-bot

