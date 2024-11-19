#𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 ⚡

import aiohttp
import asyncio
import requests
from bot import Bot
from pyrogram import Client, filters

async def download_file(drive_link):
    file_id = drive_link.split("/")[-2]
    download_url = f"https://drive.google.com/uc?id={file_id}"
    default_extension = ".bin" 
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url) as response:
            if response.status == 200:
                content_disposition = response.headers.get('Content-Disposition')
                if content_disposition:
                    filename = content_disposition.split('filename=')[1].strip('"')
                    file_extension = os.path.splitext(filename)[1]  # Get the file extension
                else:
                    filename = f"Uploaded By @ExamVault{default_extension}"
                    file_extension = default_extension
                with open(f"Uploaded By @ExamVault{file_extension}", "wb") as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)

                return filename  # Return the filename for sending later
            else:
                raise Exception("Failed to download file.")

@app.on_message(filters.command("upload"))
async def upload_file(client, message):
    # Check if the command has the required argument
    if len(message.command) < 2:
        await message.reply("Please provide a Google Drive link.")
        return

    drive_link = message.command[1]  # Use message.command for better handling
    try:
        filename = await download_file(drive_link)
        await client.send_document(chat_id=message.chat.id, document=f"Uploaded By @ExamVault{os.path.splitext(filename)[1]}")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
