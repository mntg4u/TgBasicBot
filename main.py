import requests
import asyncio
from aiohttp import web
from pyrogram import Client, filters

#My API ID , API HASH & BOT TOKEN
api_id = "13666216"
api_hash = "f3a456b486290011638fb4b312f9be70"
bot_token = "6075431113:AAFV62rWzPN4PRIhGQN1Q6xaFYJ1b7lmR0U"
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Bot is Active!")
    
async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
def download_file(drive_link):
    # Extract file ID from the Google Drive link
    file_id = drive_link.split("/")[-2]
    download_url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(download_url)
    with open("downloaded_file", "wb") as f:
        f.write(response.content)
        
@app.on_message(filters.command("upload"))
def upload_file(client, message):
    drive_link = message.text.split(" ")[1]
    download_file(drive_link)
    client.send_document(chat_id=message.chat.id, document="downloaded_file")

if __name__ == "__main__":
    app.run()
