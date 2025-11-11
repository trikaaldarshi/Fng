import os
import config

# Pull values from environment or fallback to config.py
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", config.TELEGRAM_BOT_TOKEN)
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", config.TELEGRAM_CHAT_ID)
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", getattr(config, "UPDATE_INTERVAL", 3600)))
