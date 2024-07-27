from pyrogram import Client
from .config import Config
from .database import Database

class ScreenShotBot(Client):

    def __init__(self):
        super().__init__(
            session="sample_bot",  # Use "session" for the parameter name
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="bot/plugins"
            )
        )

        self.db = Database(Config.DATABASE_URL, "sample_bot")
        self.CURRENT_PROCESSES = {}
        self.CHAT_FLOOD = {}
        self.broadcast_ids = {}
