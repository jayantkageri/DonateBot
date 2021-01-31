# <! Functions >
from telethon import TelegramClient, events, functions, Button
from telethon.tl.functions.users import GetFullUserRequest

TOKEN = os.environ.get("TOKEN")
APP_ID = os.environ.get("API_ID")
APP_HASH = os.environ.get("API_HASH")
DONATE_TEXT = os.environ.get("DONATE_TEXT")

bot = TelegramClient("bot", api_id=APP_ID, api_hash=APP_HASH)
MainBot = bot.start(bot_token=TOKEN)

@MainBot.on(events.NewMessage(pattern="^ ?(.*)"))
async def donateme(event):
    await event.reply(DONATE_TEXT)

def startbot():
    MainBot.run_until_disconnected()

import logging
logging.basicConfig(level=logging.WARNING)

print("Donatation Bot is Redy !")
print("Be Thankful to @JAYANTKAGERI")

if __name__ == "__main__":
    startbot()

# <! Functions Ends >
