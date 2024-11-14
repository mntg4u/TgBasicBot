import requests
import asyncio
from aiohttp import web
from bs4 import BeautifulSoup
from pyrogram import Client, filters

#My API ID , API HASH & BOT TOKEN
api_id = "13666216"
api_hash = "f3a456b486290011638fb4b312f9be70"
bot_token = "6075431113:AAFV62rWzPN4PRIhGQN1Q6xaFYJ1b7lmR0U"
POST_CHANNEL = -1002446673306
admin = 5465110453
PORT = 8080
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("MG University Updater is Active!")
    
async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
async def fetch_facebook_posts():
    url = "https://m.facebook.com/mgu.ac.in/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = []
        # Example: Find all post elements (you need to adjust the selectors based on the actual HTML structure)
        for post in soup.find_all('div', class_='your-post-class'):
            message = post.get_text()  # Extract the text
            # You can also extract images or other data as needed
            posts.append({'message': message})
        return posts
    else:
        print("Failed to fetch posts:", response.status_code)
        return []
        
async def send_to_telegram(post):
    if 'message' in post:
        message = post['message']
    elif 'photos' in post:
        message = f"Photo post: {post['photos'][0]['url']}"
    else:
        message = 'No message available' 
    await app.send_message(POST_CHANNEL, message)

async def main():
    await app.start()
    bot = web.AppRunner(await web_server())
        await bot.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(bot, bind_address, PORT).start()
    await app.send_message(chat_id=admin, text="**Bot is up now!** ✅")
    while True:
        posts = await fetch_facebook_posts()
        for post in posts:
            await send_to_telegram(post)
        await asyncio.sleep(60)  # Check for new posts every minute
    await app.stop()

    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
