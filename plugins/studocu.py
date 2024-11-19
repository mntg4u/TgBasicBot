import asyncio
import os
import aiohttp  # Import aiohttp for asynchronous HTTP requests
from bot import Bot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyrogram import Client, filters

# Replace these with your Studocu credentials
STUDOCU_EMAIL = "daniejoseph32@gmail.com"
STUDOCU_PASSWORD = "danie008"

async def download_studocu(studocu_link):
    # Set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    options.add_argument('--disable-gpu')  # Applicable to Windows OS only
    options.add_argument('--window-size=1920x1080')  # Set window size

    # Use ChromeDriverManager to automatically manage ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        # Navigate to the Studocu login page
        driver.get("https://www.studocu.com/en/login")

        # Log in to Studocu
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        email_input.send_keys(STUDOCU_EMAIL)
        password_input.send_keys(STUDOCU_PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()

        # Wait for login to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'my-documents')]"))
        )

        # Navigate to the provided Studocu link
        driver.get(studocu_link)

        # Wait for the download button to be available
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'download-button')]"))
        )

        # Get the download link
        download_link = download_button.get_attribute("href")

        # Download the file using aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(download_link) as response:
                if response.status == 200:
                    filename = os.path.basename(download_link)
                    with open(filename, "wb") as f:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            f.write(chunk)
                    return filename
                else:
                    raise Exception("Failed to download file.")
    finally:
        driver.quit()

@Bot.on_message(filters.command("studocu"))
async def upload_studocu(client, message):
    # Check if the command has the required argument
    if len(message.command) < 2:
        await message.reply("<code>Please provide a Studocu link.</code>")
        return

    studocu_link = message.command[1]  # Use message.command for better handling
    try:
        # Notify the user that the upload is starting
        upload_message = await message.reply("<code>Trying to Upload File from Studocu...</code>")
        
        filename = await download_studocu(studocu_link)
        
        # Send the downloaded file
        await client.send_document(chat_id=message.chat.id, document=filename)
        
        # Delete the upload message
        await upload_message.delete()
        
        # Notify the user that the file has been uploaded successfully
        await message.reply("<code>File Uploaded successfully ✅</code>")
        
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
