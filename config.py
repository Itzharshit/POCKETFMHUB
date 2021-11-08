import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001424956575))
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    DB_URL = os.environ.get("DATABASE_URL", "")
