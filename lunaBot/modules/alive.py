import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/7c3c26e0ed938aec91209.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Halo aku robot!** \n\n"
  LUNA += "š“ **saya bekerja dengan benar** \n\n"
  LUNA += "š“ **saya pengaman grup anda** \n\n"
  LUNA += f"š“ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"š“ **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**terima kasih telah menambahkan saya di sini**"
  BUTTON = [[Button.url("Źį“Źį“", "https://t.me/custombot?start=help")]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "ā **bot restarted successfully**\n\nā¢ Admin list has been **updated**"
  BUTTON = [[Button.url("š” Bot", "https://t.me/{BOT_NAME}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
