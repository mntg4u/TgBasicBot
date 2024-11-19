# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿

import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler
from time import time

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13666216"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f3a456b486290011638fb4b312f9be70")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2092454280"))

#Port
PORT = os.environ.get("PORT", "8080")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#bot token
TG_BOT_TOKEN = int(os.environ.get("TG_BOT_TOKEN", "6075431113:AAFV62rWzPN4PRIhGQN1Q6xaFYJ1b7lmR0U"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
