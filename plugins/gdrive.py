#𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 ⚡

import aiohttp
import asyncio
import requests
from bot import Bot
from pyrogram import Client, filters

async def download_file(drive_link):
    file_id = drive_link.split("/")[-2]
    download_url = f"https://drive.google.com/uc?id={file_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url) as response:
            with open("downloaded_file", "wb") as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

@Bot.on_message(filters.command("upload"))
async def upload_file(client, message):
    drive_link = message.text.split(" ")[1]
    await download_file(drive_link)
    await client.send_document(chat_id=message.chat.id, document="downloaded_file")
