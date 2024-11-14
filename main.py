import requests
import asyncio
import aiohttp
from pyrogram import Client, filters

#My API ID , API HASH & BOT TOKEN
api_id = "13666216"
api_hash = "f3a456b486290011638fb4b312f9be70"
bot_token = "YOUR_BOT_TOKEN"

# Facebook Graph API settings
fb_page_id = "YOUR_FB_PAGE_ID"
fb_access_token = "YOUR_FB_ACCESS_TOKEN"

# Telegram channel ID
telegram_channel = "@your_channel_username"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def fetch_facebook_posts():
    url = f"https://graph.facebook.com/v12.0/{fb_page_id}/posts?access_token={fb_access_token}"
    response = requests.get(url)  # This is still synchronous; consider using an async HTTP library
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print("Failed to fetch posts:", response.status_code)
        return []

async def send_to_telegram(post):
    message = post.get('message', 'No message available')
    await app.send_message(telegram_channel, message)

async def main():
    await app.start()
    while True:
        posts = await fetch_facebook_posts()
        for post in posts:
            await send_to_telegram(post)
        await asyncio.sleep(60)  # Check for new posts every minute
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
