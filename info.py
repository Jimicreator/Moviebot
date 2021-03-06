import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')

# Messages
default_start_msg = """
**πHey<a href="tg://settings"> π Nyc Name </a>, 
πΌπ π½π°πΌπ΄ <a href="https://t.me/Jimi_Group_Bot"> Jimi Movie Bot </a> πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π πΈπ½ πΆππΎππΏπ,**

πΈπ'π ππ΄ππ π΄π°ππ. πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½, ππ·π°ππ π°π»π», πΈ'π»π» πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π ππ·π΄ππ΄ π€

Hey <a href="https://t.me/Jimi_Group_Bot?startgroup=true"> add me to your grp and make me an admin </a>

Send me /id and give your id and group id
βββββββββββββ
Β©οΈMα΄ΙͺΙ΄α΄α΄ΙͺΙ΄α΄D BΚ :<a href="https://t.me/Jimi_Bots"> Jimi Bots </a>
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
