from datetime import datetime
from sys import version_info
from time import time

from config import BOT_USERNAME   
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"""𝙃𝙀𝙔 𝙏𝙃𝙀𝙍𝙀 {message.from_user.mention()} \n\n 𝙈𝙔 𝙎𝙀𝙇𝙁 𝙈𝙐𝙎𝙄𝘾𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝘽𝙔 [𝙊𝙐𝙍𝙎𝙀𝙇𝙁](https://t.me/gulu_gulu_garden)\n\n 𝘐 𝘊𝘈𝘕 𝘚𝘛𝘙𝘌𝘈𝘔 𝘈𝘜𝘋𝘐𝘖 𝘍𝘐𝘓𝘌𝘚 𝘍𝘙𝘖𝘔. 𝘠𝘖𝘜𝘛𝘜𝘉𝘌 𝘈𝘕𝘋 𝘈𝘓𝘚𝘖 𝘍𝘙𝘖𝘔 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔 𝘍𝘐𝘓𝘌𝘚""",
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




    

