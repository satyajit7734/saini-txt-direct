#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "1393027"))
API_HASH = environ.get("API_HASH", "12c455c1c1ea2ababc4661d5b741f7ff")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "5480731852"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5480731852').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
