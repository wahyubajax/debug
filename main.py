from pyrogram import Client,  filters
from pyrogram import Client
import aiorun
import os

app - Client(
    name="debug",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="debug.plugins"),
    worker='50',
)

async def start_client():
    await app.start()
    me = await self.get.me()
    self.username = "@" + me.username
    print(f"{me.fist_name} start {me.username}")



async def stop_client():
    await app.stop()
    print("bot stop bye")


if __name__ == "__main__":
   aiorun.run(start_client(), 
   shutdown_callback=stop_client()0

    
