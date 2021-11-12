from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_callback_query(filters.regex("cbsupport"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is Our Support Details**""",
        reply_markup=InlineKeyboardMarkup(
            [
             [
               InlineKeyboardButton("📕 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/gulu_gulu_garden"), 
               InlineKeyboardButton("📕 𝙐𝙥𝙙𝙖𝙩𝙚", url="https://t.me/kishu_music")
             ], 
             [ 
               InlineKeyboardButton("🈯𝙎𝙤𝙪𝙧𝙘𝙚", url="https://github.com/kishannn07/music") 
             ]
            ]
        ),
    )






@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()



@Client.on_callback_query(filters.regex("chelp"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the commands**

🎧 [ VOICE CHAT  CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/current - show the music currently playing
/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite userbot join to your group
/userbotleave - order the userbot to leave your group
/musicplayer - (on / off) - disable / enable music player in your group
/start (in private) - see the bot alive status
/reload - reload bot and refresh the admin list

⚡ __Powered by **KiShaN** A.I__""",
  )
