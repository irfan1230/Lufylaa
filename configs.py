import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "12380656"))
  API_HASH = os.environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6289968122:AAGxHai-BPG3-cO_oMBTTMUregDAdpo1R6U")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Eren_Yeager_007_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001939577738"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1581901379"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001939577738")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001939577738"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/aka_oreo)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n **Hᴇʟʟᴏ Stranger🦋 ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ Fɪʟᴇ ᴛᴏ ʟɪɴᴋ + ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ **⚡️
"""
