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
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠 𝗕𝗧𝗦 𝗣𝗨𝗥𝗣𝗟𝗘 𝗕𝗢𝗧​~❥*\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐏𝐔𝐑𝐏𝐋𝐄 𝐁𝐎𝐘](https://t.me/mr_agora)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/agora_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/karunada_kings_and_queens")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
