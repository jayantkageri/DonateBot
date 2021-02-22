#    Donate Bot, A Simple Telegram Bot to tell How to Donate you
#    Copyright (C) 2021 Jayant Kageri
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


# <! Functions >

import os
from telethon import TelegramClient, events, functions, Button
from telethon.tl.functions.users import GetFullUserRequest

TOKEN = os.environ.get("TOKEN")
APP_ID = int(os.environ.get("API_ID"))
APP_HASH = os.environ.get("API_HASH")
DONATE_TEXT = os.environ.get("DONATE_TEXT")
OWNER_ID = int(os.environ.get("OWNER_ID")

bot = TelegramClient("bot", api_id=APP_ID, api_hash=APP_HASH)
MainBot = bot.start(bot_token=TOKEN)

@MainBot.on(events.NewMessage(pattern="^ ?(.*)"))
async def _(event):
    await MainBot.send_message(event.chat_id, DONATE_TEXT)

@MainBot.on(events.NewMessage(pattern="^ ?(.*)"))
async def _(event):
    incoming = event.raw_text
    who = event.sender_id
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.forward_to(OWNER_ID)

def startbot():
    MainBot.run_until_disconnected()

import logging
logging.basicConfig(level=logging.WARNING)

print("Donatation Bot is Redy !")
print("Be Thankful to @JAYANTKAGERI")

if __name__ == "__main__":
    startbot()

# <! Functions Ends >
