import os

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
LOGGER_ID = int(os.environ.get("LOGGER_ID", "0"))
STRING_SESSION = os.environ.get("STRING_SESSION", "")
PORT = int(os.environ.get("PORT", "8080"))

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH and BOT_TOKEN are required")

if not STRING_SESSION:
    raise ValueError("STRING_SESSION is required")
