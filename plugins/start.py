import json
import pytesseract
from PIL import Image
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import Message

# File to store user data
USER_DATA_FILE = "users.json"
ADMIN_ID = 123456789  # Replace with your Telegram user ID

# Function to load user data
def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save user data
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Track users
@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    user_id = str(message.from_user.id)
    users = load_users()

    if user_id not in users:
        users[user_id] = {
            "username": message.from_user.username or "N/A",
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name or "N/A"
        }
        save_users(users)

    await message.reply_text("📸 Send me an image, and I'll extract text from it!")

# Extract text from image
@Client.on_message(filters.photo)
async def extract_text(client, message: Message):
    photo = message.photo
    file_path = await client.download_media(photo.file_id)

    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        if text.strip():
            await message.reply_text(f"📝 **Extracted Text:**\n\n{text}")
        else:
            await message.reply_text("❌ No text found in the image.")
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {e}")

# Admin command to check total users
@Client.on_message(filters.command("stats") & filters.user(ADMIN_ID))
async def stats_command(client, message: Message):
    users = load_users()
    total_users = len(users)
    await message.reply_text(f"📊 **Total Users:** {total_users}")
