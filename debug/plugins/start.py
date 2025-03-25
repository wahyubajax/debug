from config import * 
from pyrogram import Client, filters
from pyrogram import Client

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
  print("hi bang")
