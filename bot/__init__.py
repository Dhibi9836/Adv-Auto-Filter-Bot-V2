#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get(5530754))

API_HASH = os.environ.get("5e51ecf5945605c711fffe7b376fa2a8")

BOT_TOKEN = os.environ.get("5694714864:AAHBWW5y2eZ-6xyGuygZOxhLWV5CxaA40HU")

DB_URI = os.environ.get("mongodb+srv://123:123@cluster0.jypxi61.mongodb.net/test")

USER_SESSION = os.environ.get("BQB_nNsE1PEkULOcrwVt--IBeVF0rMdWQJ-_mnf1DiJ8CI1TSmxS98HVj6ypLTG1brVbpvYRrkYwWMAEEHa-l8hIiQNFpwSgJ2Zt-5mODv8BcwR6bhvWiXAk_8cl14R8ST21lGYKPSVqYZGYBBME8MZ59i2GqJc7dpB76wUR2KrcuYp6sM-C-8A0mo1I7EsMLM8dHXhkM-amjbL-BWFD_5JAvD59TuChPOuzP8qWFELR2SpASfgiPDynaj58VnkUyLNnLBfjqjj8QAsHry8RpvhizcnGqxDPB-NhhZ6qMXZ0U6a9cadp3UrzeuYKLY2itQZLrFvG4C6MMGPFWSd3zyXdRcYZbgA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
