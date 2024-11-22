#𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 ⚡

import os
import re
import asyncio
from pyrogram import Client, enums, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from script import NEXT_TXT

contact_btn = [
    [
        InlineKeyboardButton(text = 'Reach out to him', url = 'https://t.me/DevKrishnaAjith')
    ]
]

@Bot.on_callback_query(filters.regex(r'^next$'))
async def next_cbq(client: Client, query: CallbackQuery):
    await client.send_message(
        chat_id = query.message.chat.id,
        text = NEXT_TXT,
        reply_markup = InlineKeyboardMarkup(contact_btn),
        disable_web_page_preview = True,
        parse_mode=enums.ParseMode.HTML
    )
     
        
   
