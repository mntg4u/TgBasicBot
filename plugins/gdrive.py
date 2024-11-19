#𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 ⚡

import os
import aiohttp
import asyncio
import requests
from bot import Bot
from pyrogram import Client, filters
from bs4 import BeautifulSoup

async def download_file(file_url, original_filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                content_disposition = response.headers.get('Content-Disposition')
                if content_disposition:
                    # Extract filename from Content-Disposition header
                    filename = content_disposition.split('filename=')[1].strip('"')
                else:
                    # Default filename if not found
                    filename = original_filename
                
                # Save the file with the original filename
                with open(filename, "wb") as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                
                return filename  # Return the filename for sending later
            else:
                raise Exception("Failed to download file.")

async def get_file_links_from_folder(folder_link):
    async with aiohttp.ClientSession() as session:
        async with session.get(folder_link) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                links = []
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if "/file/d/" in href:
                        file_id = href.split("/file/d/")[1].split("/")[0]
                        download_url = f"https://drive.google.com/uc?id={file_id}"
                        links.append((download_url, a.text))  # Append download URL and filename
                return links
            else:
                raise Exception("Failed to access the folder.")

async def handle_individual_file(file_link):
    if "/file/d/" in file_link:
        file_id = file_link.split("/file/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?id={file_id}"
    return None

@Bot.on_message(filters.text)
async def handle_drive_link(client, message):
    if "drive.google.com" in message.text:
        link = message.text.strip()
        try:
            upload_message = await message.reply("<code>Trying to Upload...</code>")
            if "folders/" in link:
                file_links = await get_file_links_from_folder(link)
                for file_url, filename in file_links:
                    local_filename = await download_file(file_url, filename)  # Use original filename
                    await client.send_document(chat_id=message.chat.id, document=local_filename)
            elif "/file/d/" in link:
                file_url = await handle_individual_file(link)
                if file_url:
                    local_filename = await download_file(file_url, link.split("/")[-1])  # Use the last part of the link as filename
                    await client.send_document(chat_id=message.chat.id, document=local_filename)
            await upload_message.delete()
            await message.reply("<code>Files Uploading completed ✅</code>")
        except Exception as e:
            await message.reply("<code>❌ Invalid Google Drive link. Please provide a valid file or folder link!</code>")
