import os

# Directly read from Heroku Config Vars
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 3600))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
