import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ---------- Flask App ----------
app = Flask(_name_)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---------- Telegram Bot ----------
API_ID = int(os.environ.get("36897880"))
API_HASH = os.environ.get("8dce511aa79800ba94eb9f327b12fc52")
BOT_TOKEN = os.environ.get("8054603258:AAGN8ZmJgqhm0WpAZcr1-w130iVk0fR58Y4")

bot = Client(
    "fileflashbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("✅ FileFlashBot চালু আছে!\nফাইল পাঠান।")

@bot.on_message(filters.private & (filters.document | filters.video))
async def protect_file(_, message):
    await message.copy(
        chat_id=message.chat.id,
        protect_content=True
    )

def run_bot():
    bot.run()

# ---------- Main ----------
if name == "main":
    threading.Thread(target=run_flask).start()
    run_bot()
