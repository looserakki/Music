import os
from config import BOT_USERNAME   
from helpers.filters import command
from helpers.filters import other_filters2
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""𝙃𝙀𝙔 𝙏𝙃𝙀𝙍𝙀 {message.from_user.mention()} \n\n 𝙈𝙔 𝙎𝙀𝙇𝙁 𝙈𝙐𝙎𝙄𝘾𝘽𝙊𝙏 𝘾𝙍𝙀𝘼𝙏𝙀𝘿 𝘽𝙔 [𝙊𝙐𝙍𝙎𝙀𝙇𝙁](https://t.me/gulu_gulu_garden)\n\n 𝘐 𝘊𝘈𝘕 𝘚𝘛𝘙𝘌𝘈𝘔 𝘈𝘜𝘋𝘐𝘖 𝘍𝘐𝘓𝘌𝘚 𝘍𝘙𝘖𝘔. 𝘠𝘖𝘜𝘛𝘜𝘉𝘌 𝘈𝘕𝘋 𝘈𝘓𝘚𝘖 𝘍𝘙𝘖𝘔 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔 𝘍𝘐𝘓𝘌𝘚""",
        reply_markup=InlineKeyboardMarkup(
           [
            [                    
                    InlineKeyboardButton("⚙️𝐇𝐞𝐥𝐩", callback_data="cbhelp"),                    
                    InlineKeyboardButton("🔥𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://github.com/kishannn07/music")
            ], 
            [
                    InlineKeyboardButton("⚒️𝐒𝐮𝐩𝐩𝐨𝐫𝐭", callback_data="cbsupport"), 
                    InlineKeyboardButton("🗑𝐂𝐥𝐨𝐬𝐞", callback_data="close")
            ]              
           ]
        ),
        disable_web_page_preview=True,
    )




    

