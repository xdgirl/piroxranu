# © @OXYGEN474

import heroku3

from os import getenv
from config import SUDO_USERS, ALIVE_PIC, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

from pyrogram import Client, filters
from pyrogram.types import Message


FIRST_TEXT = f"""★ ™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★

**» ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/BWANDARLOK/11)
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/BWANDARLOK/12)
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/BWANDARLOK/13)
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/PRADHAN474/14)"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], [".", "!", "/"]))
async def help(client: Client, message: Message):
    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_PIC,
        caption=FIRST_TEXT
    )


@Client.on_message(filters.user(OWNER_ID) & filters.command(["sudo"], ["/", ".", "!"]))
async def addsudo(event):
    if not message.reply_to_message:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ  ꜱᴜᴅᴏ...__🚀🚀")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ ™°‌**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")     
