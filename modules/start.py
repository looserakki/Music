from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music on groups through the new Telegram's voice chats!**
💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**
🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("⚙️𝐇𝐞𝐥𝐩", callback_data="cbhelp"),
                    InlineKeyboardButton("⚒️𝐒𝐮𝐩𝐩𝐨𝐫𝐭", callback_data="cbsupport")
                ]
                [
                    InlineKeyboardButton("🔥𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://github.com/kishannn07/music"),
                ]              
            ]
        ),
        disable_web_page_preview=True,
    )




    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing music on your Group voice chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


