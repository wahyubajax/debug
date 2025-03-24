from pyrogram import Client,  filters
from pyrogram import Client
import aiorun
import os

class App(Client):
  def __init__(self):
     super().__init__(
       name="debug",
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=BOT_TOKEN,
       plugins=dict(root="debug.plugins"),
       worker='50',
)

async def start(self):
    await super().start()
    me = await self.get.me()
    self.username = "@" + me.username
    print(f"{me.fist_name} start {me.username}")



async def stop(self):
    await super().stop()
    print("bot stop bye")


if __name__ == "__main__":
   aiorun.run(start(),
   shutdown_callback=stop())

    
