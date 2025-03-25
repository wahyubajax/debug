from config import * 
from pyrogram import Client, filters
from main import app

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
  print("hi bang")
