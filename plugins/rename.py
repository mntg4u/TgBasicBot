import os
import subprocess
import asyncio
from bot import Bot
from pyrogram import Client, filters

CMD = ["rename", "r"]

@Bot.on_message(filters.command(CMD) & filters.reply)
async def handle_rename(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        original_file_name = message.reply_to_message.document.file_name
        original_file_path = await client.download_media(message.reply_to_message.document.file_id)
        new_name = message.text.split(" ", 1)
        if len(new_name) < 2:
            await message.reply("❌ Please provide a new filename along with the /rename command.")
            return
        new_name = new_name[1].strip() 
        original_extension = os.path.splitext(original_file_name)[1]  
        renamed_file_path = os.path.join(os.path.dirname(original_file_path), f"{new_name}{original_extension}")
        os.rename(original_file_path, renamed_file_path)
        await client.send_document(chat_id=message.chat.id, document=renamed_file_path)
        os.remove(renamed_file_path)
    else:
        await message.reply("❌ Please reply to a document with the /rename command.")
