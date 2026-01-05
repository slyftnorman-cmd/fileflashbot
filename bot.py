from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message

# 🔑 আপনার তথ্য বসান
api_id = 36897880
api_hash = "8dce511aa79800ba94eb9f327b12fc52"
bot_token = "8054603258:AAGN8ZmJgqhm0WpAZcr1-w130iVk0fR58Y4"

STORAGE_CHANNEL = -1002612384406
FORCE_CHANNEL = -1002673167862
FORCE_CHANNEL_LINK = "https://t.me/FilmStore99"
BOT_USERNAME = "@fileflashbot"

app = Client(
    "fileflash_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# 🔒 Force Subscribe Check
async def is_joined(client, user_id):
    try:
        await client.get_chat_member(FORCE_CHANNEL, user_id)
        return True
    except UserNotParticipant:
        return False

# 📥 File Save
@app.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def save_file(client: Client, message: Message):
    sent = await message.copy(STORAGE_CHANNEL)
    msg_id = sent.id
    link = f"https://t.me/{BOT_USERNAME}?start={msg_id}"

    await message.reply(
        f"✅ Permanent Protected Link:\n{link}",
        disable_web_page_preview=True
    )

# ▶️ Start Command
@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    user_id = message.from_user.id

    if not await is_joined(client, user_id):
        return await message.reply(
            f"📢 আগে আমাদের চ্যানেলে Join করুন\n\n"
            f"👉 {FORCE_CHANNEL_LINK}\n\n"
            f"Join করে আবার লিংকে ক্লিক করুন 🔁"
        )

    if len(message.command) > 1:
        msg_id = int(message.command[1])
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=STORAGE_CHANNEL,
            message_id=msg_id,
            protect_content=True
        )
    else:
        await message.reply(
            "📥 যেকোনো ফাইল বা ভিডিও পাঠান\n"
            "🔒 Forward / Save করা যাবে না"
        )

app.run()
