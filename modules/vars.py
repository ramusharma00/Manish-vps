import os

API_ID    = os.environ.get("API_ID", "25567551")
API_HASH  = os.environ.get("API_HASH", "45993062e6b160a7a360d648ecc8e43a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "75333666:AAGIveG6g9ilEv_IHXrCRidXIxcqwLMEA") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
