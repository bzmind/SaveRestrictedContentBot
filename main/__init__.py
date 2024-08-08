#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25115384
API_HASH = "1a53b1195b049269f8ab21d65a5864b3"
BOT_TOKEN = "7212205658:AAGW5fXOzIVWm5gyjBRNkmrQNgk5kwuQuvg"
SESSION = "BAF_OvgAvL-7f-JWiQSh6tKWngpcTvWxiZ2mQ02YZgzL0soQ7kJyU7QprHn0CM9lQGHNOQYuHYIM_l5EdxlPhasdXB1LxaBMHwhHSR3vHklSYZQUGtpSMc0hY-_bIYXyYxz_xMLEVJM2pekxyDhTBNTXx_6jFOZef2ey4eRyVuoItZLOeEbJhAMaAu8vW_fI8-dW98H5Ee8sKoDLkmwCWw6Y7qRYWYCsrsFQ8jjispiTEHMd-8U9N4JLo2lqLtMW3lpFp1iDqI1eV3HwcfPc23lHAemzvZjuj-lpyiQXTamrCHBLgrz5YrHoyKT0BOb_UOLgtjm8EHhskyIBiwrLjcMq9PzgfQAAAAGt4YZaAQ"
FORCESUB = "melodicmind"
AUTH = 7369755354

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
