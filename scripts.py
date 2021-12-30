class Scripted(object):    


    PROGRESS_DIS = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├<b>📁 : {1} | {2}</b>
│
├<b>🚀 : {0}%</b>
│
├<b>⚡ : {3}/s</b>
│
├<b>⏱️ : {4}</b>
╰─────────────────⍟"""

    HELP_TEXT = """
<i>𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 <a href='https://t.me/Z_Bots/21'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></i>\n
<i>𝐒𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐚𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (optional)</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (or) 𝐌𝐞𝐝𝐢𝐚 𝐟𝐫𝐨𝐦 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦</i>\n
<i>𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧𝐭𝐨 𝐯𝐢𝐝𝐞𝐨 𝐮𝐬𝐞 /convert 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞.ext</i>\n
<i>𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /sthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐃𝐞𝐥𝐞𝐭𝐞 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /dthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>"""


    ABOUT_TEXT = """
╭────[🔅Rᴇɴᴀᴍᴇʀ Bᴏᴛ🔅]───⍟
│
├<b>🤖 Bᴏᴛ Nᴀᴍᴇ : <a href='t.me/RenamerZ2_0_bot'>Rename 2.0 Bot</a></b>
│
├<b>📢 Cʜᴀɴɴᴇʟ : <a href='https://t.me/Z_Bots'>Z_Bots</a></b>
│
├<b>👥 Vᴇʀsɪᴏɴ : <a href='https://t.me/RenamerZ2_0_bot'>0.9.2 beta</a></b>
│
├<b>💢 Sᴏᴜʀᴄᴇ : <a href='https://github.com/madtoazenzio/RENAMER-2.0-Z'>Click Here</a></b>
│
├<b>🌐 Sᴇʀᴠᴇʀ : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Lɪʙʀᴀʀʏ : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/RenamerZ2_0_bot'>@Z_Admin</a></b>
│
├<b>🚸 Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/Asyn_Editz'>@AsynEditZ</a></b>
│
|<b>🚸 Cᴏ-Pᴏᴡᴇʀᴇᴅ Bʏ : <a href='https://t.me/MLM_CartoonZ_World'>@MLM_CARTOONZ_WORLD</a></b>
╰──────[Thanks 😊]───⍟"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>¥ou Are Banned 🚫</b>"
    BANNED_USER_TEXT = "<i>¥ou are Banned 🚫</i>"
    TRYING_TO_UPLOAD = "<i>Trying to Upload.....</i>"
    CURRENT_THUMBNAIL = "<i>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🎭</i>"
    THUMBNAIL_SAVED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 ✅</i>"
    THUMBNAIL_DELETED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ✅</i>"
    NO_THUMBNAIL_FOUND = "<i>𝐍𝐨 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝 😔</i>"
    TRYING_TO_DOWNLOAD = "<i>Trying to Download....</i>"
    UPLOAD_SUCCESS = "<u><i>TʜᴀɴᴋS Fᴏʀ Usɪɴɢ ᴍᴇ❤ @Z_Bots</i></u>"
    REPLY_TO_MEDIA = "<i>Reply to Media For Converting with Command /convert</i>"
    UPLOAD_START = "<i>📤 Uploading Your File Please wait...</i>\n"
    DOWNLOAD_START = "<i>📥 Downloading Your File Please wait...</i>\n"
    JOIN_NOW_TEXT = "<code>First Join My Updates Channel to Use Me</code>"
    REPLY_TO_FILE = "<i>Reply to that media with /rename new name .ext</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Wrong Contact in Support Group @Z_Bots 😑</i>"
    START_TEXT = "<i>This is a Fastest File Renamer and Converter <a href="https://telegra.ph/file/51217c71df0a1dc7196c8.jpg">Bot</a> With Permanant Thumbnail Support💯</i>"
    UPGRADE_TEXT = "<b>To upgrade your bot <a href='https://t.me/Z_Bots'>[ Click Here]</a></b>"
