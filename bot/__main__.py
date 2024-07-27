from .screenshotbot import ScreenShotBot
from flask import Flask
import threading
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Flask(__name__)

@bot.route('/')
def hello_world():
    return 'Hello, World!'

@bot.route('/health')
def health_check():
    return 'Healthy', 200

def run_flask():
    bot.run(host='0.0.0.0', port=8080)

app = ScreenShotBot()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    
    try:
        app.run()
    except Exception as e:
        logger.error(f"Pyrogram client error: {e}")
