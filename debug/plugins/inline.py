from pyrogram import Client, filters

@client.on_message(filters.command("start"))
async start_cmd((client, message):
