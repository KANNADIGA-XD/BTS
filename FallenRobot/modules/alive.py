import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://te.legra.ph/file/2c1b0fb5787efb1257e22.jpg",
    "https://te.legra.ph/file/2fb0e86e935d0d2c0b51c.jpg",
    "https://te.legra.ph/file/c1a27d53b7255defd16e6.jpg",
    "https://te.legra.ph/file/55ce9f61b08a6d830e2ce.jpg",
    "https://te.legra.ph/file/9bec598cdee9a51ff0b77.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**สแดสโ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n๐ ๐๐  ๐๐ง๐ฆ ๐ฃ๐จ๐ฅ๐ฃ๐๐ ๐๐ข๐งโ~โฅ*\nโโโโโโโโโโโโโโโโโโโ\n\n"
  TEXT += f"ยป **แดส แดแดแด แดสแดแดแดสโ : [๐๐๐๐๐๐ ๐๐๐](https://t.me/mr_agora)** \n\n"
  TEXT += f"ยป **สษชสสแดสส แด แดสsษชแดษด :** `{telever}` \n\n"
  TEXT += f"ยป **แดแดสแดแดสแดษด แด แดสsษชแดษด :** `{tlhver}` \n\n"
  TEXT += f"ยป **แดสสแดษขสแดแด แด แดสsษชแดษด :** `{pyrover}` \nโโโโโโโโโโโโโโโโโ\n\n"
  BUTTON = [[Button.url("สแดสแดโ", "https://t.me/agora_robot?start=help"), Button.url("sแดแดแดแดสแดโ", "https://t.me/karunada_kings_and_queens")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
