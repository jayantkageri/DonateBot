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

import os

ENV = os.environ.get("ENV")



class Var(object):
  if ENV:
    API_ID = int(os.environ.get('API_ID'))
    APP_HASH = os.environ.get('API_HASH')
    TOKEN = os.environ.get('TOKEN')
    OWNER_ID = int(os.environ.get('OWNER_ID'))
    DONATE_TEXT = os.environ.get('DONATE_TEXT')

  else:
    API_ID = int("Put you API_ID here (in the String)")
    API_HASH = "Put your API_HASH here (in the String)"
    TOKEN = "Put your Bot Token here (in the String)"
    OWNER_ID = int("Put your Telegram ID here (in the String)")
    DONATE_TEXT = "Put your Donat Text/Message to be repeated here (in the String)"
