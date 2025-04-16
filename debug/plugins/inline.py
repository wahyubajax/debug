from pyrogram import Client, filters

@client.on_message(filters.command("start"))
async start_cmd((client, message):
welcome_teks= """"

perintah 
/addubot

 await reply_to(welcome_teks)
