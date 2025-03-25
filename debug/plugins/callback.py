from config import *
from pyrogram import Client, filters 
from main import app
import os

@app.on_callback_quaery()
async def callback_quaery(bot, message):
  await message.delete()
