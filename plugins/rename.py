import os
import asyncio
from bot import Bot
from pyrogram import Client, filters

pending_renames = {}

@Bot.on_message(filters.reply & filters.document)
async def handle_document(client, message):
    # When a document is sent, ask for the new name
    await message.reply("Please send the new file name (without extension).")

    # Store the user's message ID and the original file path
    original_file_path = await client.download_media(message.reply_to_message.document.file_id)
    pending_renames[message.chat.id] = (original_file_path, message.reply_to_message.document.file_name)

@Bot.on_message(filters.text & filters.private)
async def handle_new_name(client, message):
    # Check if the user has a pending rename request
    if message.chat.id in pending_renames:
        original_file_path, original_file_name = pending_renames[message.chat.id]
        new_name = message.text.strip()

        if not new_name:
            await message.reply("❌ You must provide a valid new name.")
            return

        original_extension = os.path.splitext(original_file_name)[1]
        renamed_file_path = os.path.join(os.path.dirname(original_file_path), f"{new_name}{original_extension}")

        # Notify the user that renaming is in progress
        await message.reply("Renaming... Please wait.")

        try:
            # Rename the file
            os.rename(original_file_path, renamed_file_path)

            # Prepare thumbnail and caption
            thumb = "https://envs.sh/5UR.jpg"
            caption = f"<b><i>{new_name}{original_extension}\n\n© @ExamVault</i></b>"

            # Send the renamed file back to the chat
            await client.send_document(chat_id=message.chat.id, document=renamed_file_path, caption=caption, thumb=thumb)

            # Notify the user that renaming was successful
            await message.reply("✅ Renaming successful!")
            
            # Clean up the renamed file
            os.remove(renamed_file_path)
        except Exception as e:
            await message.reply(f"❌ An error occurred while renaming the file: {str(e)}")
        finally:
            # Remove the user from the pending renames
            del pending_renames[message.chat.id]
    else:
        await message.reply("❌ Please send a document first to rename it.")
