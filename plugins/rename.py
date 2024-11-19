import os
import asyncio
from bot import Bot
from pyrogram import Client, filters

@Bot.on_message(filters.command("rename") & filters.reply)
async def handle_rename(client, message):
    # Check if the replied message contains a document
    if message.reply_to_message and message.reply_to_message.document:
        original_file_name = message.reply_to_message.document.file_name
        original_file_path = await client.download_media(message.reply_to_message.document.file_id)

        # Split the command to get the new name
        new_name = message.text.split(" ", 1)
        if len(new_name) < 2:
            await message.reply("❌ Please provide a new filename along with the /rename command.")
            return

        new_name = new_name[1].strip()  # Get the new name and strip any extra spaces
        original_extension = os.path.splitext(original_file_name)[1]  # Get the original file extension
        renamed_file_path = os.path.join(os.path.dirname(original_file_path), f"{new_name}{original_extension}")

        try:
            # Rename the file
            os.rename(original_file_path, renamed_file_path)

            # Prepare thumbnail and caption
            thumb = "https://envs.sh/5UR.jpg"
            caption = f"<b><i>{new_name}\n\n© @ExamVault</i></b>"

            # Send the renamed file back to the chat
            await client.send_document(chat_id=message.chat.id, document=renamed_file_path, caption=caption, thumb=thumb)

            # Clean up the renamed file
            os.remove(renamed_file_path)
        except Exception as e:
            await message.reply(f"❌ An error occurred while renaming the file: {str(e)}")
    else:
        await message.reply("❌ Please reply to a document with the /rename command.")
