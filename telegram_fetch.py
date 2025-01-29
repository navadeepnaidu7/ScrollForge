import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv(dotenv_path='session/secrets.env')

# Replace with your credentials in secrets.env file inside session folder
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

# Initialize Telegram client
client = TelegramClient("session_name", api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Logged in successfully!")

client.loop.run_until_complete(main())
