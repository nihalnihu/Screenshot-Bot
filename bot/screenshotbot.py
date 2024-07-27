from pyrogram import Client
from .config import Config
from .database import Database

class ScreenShotBot(Client):

    def __init__(self):
        super().__init__(
            name=Config.SESSION_NAME,  # Correct argument for session name
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="bot/plugins"
            ),
            proxy=dict(
                scheme="http",          # Proxy scheme (http or https)
                hostname="localhost",   # Proxy server hostname
                port=8000                # Proxy server port
            )
        )

        self.db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
        self.CURRENT_PROCESSES = {}
        self.CHAT_FLOOD = {}
        self.broadcast_ids = {}
