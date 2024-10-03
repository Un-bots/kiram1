from pyrogram import Client, filters
from AviaxMusic import app
from config import BOT_USERNAME
from pyrogram.types import Message


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(6253265083))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1001928799341
 

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ ")
      
