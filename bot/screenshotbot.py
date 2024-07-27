from pyrogram import Client
from .config import Config
from .database import Database

class ScreenShotBot(Client):

    def __init__(self):
        super().__init__(
            session_name="screenshotbot",  # Use session_name here
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="bot/plugins"
            )
        )

        self.db = Database(Config.DATABASE_URL, "screenshotbot")
        self.CURRENT_PROCESSES = {}
        self.CHAT_FLOOD = {}
        self.broadcast_ids = {}
