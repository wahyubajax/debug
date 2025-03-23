from pyrogram import Client,  filters
from pyrogram import Client
from pyrogram import idle
import loging
import os


app = Client(
  name"debug",
  api_id=API_HASH,
  api_hash=API)_HASH,
  bot_token=BOT_TOKEN,
)

async def star():
    await app.start()
    await idle()
