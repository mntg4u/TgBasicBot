import os
import subprocess
import asyncio
from bot import Bot
from pyrogram import Client, filters

async def convert_to_pdf(downloaded_file):
    if not downloaded_file.endswith(('.docx', '.pptx')):
        return None
    output_file = f"{os.path.splitext(downloaded_file)[0]}.pdf"
    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', downloaded_file, '--outdir', os.path.dirname(output_file)], check=True)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return None

@Bot.on_message(filters.command("pdf") & filters.reply)
async def handle_pdf_conversion(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        file_id = message.reply_to_message.document.file_id
        file_name = message.reply_to_message.document.file_name
        downloaded_file = await client.download_media(file_id)
        pdf_file = await convert_to_pdf(downloaded_file)
        if pdf_file:
            await client.send_document(chat_id=message.chat.id, document=pdf_file)
            os.remove(downloaded_file)
            os.remove(pdf_file)
        else:
            await message.reply("<i>❌ Failed to convert the document. Please ensure it is a <b>DOCX</b> or <b>PPTX</b> file.</i>")
    else:
        await message.reply("<i>❌ Please reply to a DOCX or PPTX file with the /pdf command.</i>")
