import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    API_ID = int(os.getenv("TELEGRAM_API_ID"))
    API_HASH = os.getenv("TELEGRAM_API_HASH")
    PHONE = os.getenv("TELEGRAM_PHONE")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    CHECKIN_TEXT = os.getenv("CHECKIN_TEXT")
    CHECKOUT_TEXT = os.getenv("CHECKOUT_TEXT")
    ASTU_OPTION_TEXT = os.getenv("ASTU_OPTION_TEXT")
