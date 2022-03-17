#    Donate Bot, A Simple Telegram Bot to tell How to Donate you
#    Copyright (C) 2021 Jayant Kageri
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
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
from . import *

API_ID = Var.API_ID
API_HASH = Var.API_HASH
TOKEN = Var.TOKEN
OWNER_ID = Var.OWNER_ID
DONATE_TEXT = Var.DONATE_TEXT

telegram = TelegramClient("telegram_client", api_id=API_ID, api_hash=API_HASH).start(bot_token=TOKEN)

@telegram.on(events.NewMessage(pattern="^ ?(.*)"))
async def _(event):
    # Send Donate Message
    await telegram.send_message(event.chat_id, DONATE_TEXT)

    # Forword Message to the Owner
    incoming = event.raw_text
    who = event.sender_id
    if incoming.startswith("/start"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.forward_to(OWNER_ID)

import logging
logging.basicConfig(level=logging.WARNING)

print("Donatation Bot is Redy !")
print("Be Thankful to @JAYANTKAGERI")

telegram.run_until_disconnected()

# <! Functions Ends >
