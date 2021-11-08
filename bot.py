import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from config import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)
@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(
        "**𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝑷𝒐𝒄𝒌𝒆𝒕 𝑭𝒎 𝑯𝒖𝒃 𝒃𝒐𝒕**\n\n"
        "𝑯𝒆𝒓𝒆 𝒀𝒐𝒖 𝒄𝒂𝒏 𝒔𝒆𝒂𝒓𝒄𝒉 𝒂𝒍𝒍 𝒕𝒉𝒆 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒔𝒕𝒐𝒓𝒊𝒆𝒔 𝒐𝒇 𝒑𝒐𝒄𝒌𝒆𝒕 𝒇𝒎 𝒉𝒖𝒃 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒗𝒊𝒔𝒊𝒕𝒏𝒈 𝒄𝒉𝒂𝒏𝒏𝒆𝒍.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗴𝗿𝗼𝘂𝗽", url="https://t.me/pocketfmhubchat"),
             InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/pocketfmhub")],
            [InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗡𝗼𝘄", switch_inline_query_current_chat="")]
        ])
    )


@Bot.on_inline_query()
async def inline_handlers(_, event: InlineQuery):
    answers = list()
    # If Search Query is Empty
    if event.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="𝑻𝒖𝒕𝒐𝒓𝒊𝒂𝒍 𝑽𝒊𝒅𝒆𝒐",
                description="𝗜𝗳 𝘆𝗼𝘂 𝗮𝗿𝗲 𝗳𝗮𝗰𝗶𝗻𝗴 𝗮𝗻𝘆 𝗽𝗿𝗼𝗯𝗹𝗲𝗺 𝗜𝗻 𝗼𝗽𝗲𝗻𝗶𝗻𝗴 𝗧𝗻𝗹𝗶𝗻𝗸, 𝗪𝗮𝘁𝗰𝗵 𝘁𝗵𝗶𝘀 𝘃𝗶𝗱𝗲𝗼...",
                thumb_url="https://i.imgur.com/6jZsMYG.png",
                input_message_content=InputTextMessageContent(
                    message_text="𝗜𝗳 𝘆𝗼𝘂 𝗮𝗿𝗲 𝗳𝗮𝗰𝗶𝗻𝗴 𝗮𝗻𝘆 𝗽𝗿𝗼𝗯𝗹𝗲𝗺 𝗜𝗻 𝗼𝗽𝗲𝗻𝗶𝗻𝗴 𝗹𝗶𝗻𝗸𝘀, 𝗪𝗮𝘁𝗰𝗵 𝘁𝗵𝗶𝘀 𝘃𝗶𝗱𝗲𝗼...",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("𝗧𝗡𝗹𝗶𝗻𝗸", url="https://youtu.be/xamCVwfbaKM"),
             InlineKeyboardButton("𝗗𝗿𝗼𝗽𝗹𝗶𝗻𝗸", url="https://youtube.com/shorts/9Dz3d1f-4Io?feature=share")],
                ])
            )
        )
        answers.append(
            InlineQueryResultArticle(
                title="𝗦𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 & 𝐆𝐫𝐨𝐮𝐩",
                description="𝗖𝗵𝗮𝗻𝗻𝗲𝗹 - @𝗽𝗼𝗰𝗸𝗲𝘁𝗳𝗺𝗵𝘂𝗯\n𝗚𝗿𝗼𝘂𝗽 - @𝗽𝗼𝗰𝗸𝗲𝘁𝗳𝗺𝗵𝘂𝗯𝗰𝗵𝗮𝘁",
                thumb_url="https://i.ibb.co/VCwNryW/IMG-20211107-210909-671.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="Usɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ sᴇᴀʀᴄʜ ᴀʟʟ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀᴜᴅɪᴏʙᴏᴏᴋs ᴏғ ᴘᴏᴄᴋᴇᴛ Fᴍ Hᴜʙ ᴡɪᴛʜᴏᴜᴛ ᴠɪsɪᴛɪɴɢ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ.",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("𝗠𝘆 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/pocketfmhubchat"),
                     InlineKeyboardButton("𝗠𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/pocketfmhub")],
                    [InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗵𝗲𝗿𝗲", switch_inline_query_current_chat="")]
                ])
            )
        )
        try:
            await event.answer(
            results=answers,
            cache_time=0
            )
            print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
        except QueryIdInvalid:
            print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")
    # Search Channel Message using Search Query Words
    else:
        txt="All results\n\n"
        async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=49, query=event.query):
            if message.text:
                answers.append(InlineQueryResultArticle(
                    title="{}".format(message.text.split("\n", 1)[0]),
                    description="{}".format(message.text.rsplit("\n", 1)[-1]),
                    thumb_url="https://i.ibb.co/BwYhZTr/IMG-20210914-015740-238.jpg",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=message.text.markdown,
parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                ))
                txt=txt+"{} - https://t.me/pocketfmhub/{}".format(message.text.split("\n", 1)[0],message.message_id)+"\n\n"
        answers.append(InlineQueryResultArticle(
                    title="All Available Stories",
                    description="All available stories",
                    thumb_url="https://i.ibb.co/4dPd52s/Png-Item-5099442-1.png",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=txt,
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                ))
        try:
            await event.answer(
            results=answers,
            cache_time=0
            )
            print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
        except QueryIdInvalid:
            print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")

class autocaption(Client):
    
    def __init__(self):
        super().__init__(
            session_name="Captioner",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            workers = 20,
            plugins = dict(
                root="plugins"
            )
        )

if __name__ == "__main__" :
    autocaption().run()

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
