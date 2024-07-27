from pyrogram.errors import FloodWait
import time
from .screenshotbot import ScreenShotBot

app = ScreenShotBot()

if __name__ == "__main__":
    while True:
        try:
            app.run()
        except FloodWait as e:
            print(f"Flood wait error: {e.x} seconds. Waiting...")
            time.sleep(e.x)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  # Break the loop or handle other errors as needed
