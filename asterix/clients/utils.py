import time
import platform

import logging 
from config import Config
from telegraph import Telegraph
from asterix.pyrogramx.methods import Methods
from pyrogram import __version__ as pyro_version
from asterix.database import Database
from asterix.helpers import Helpers




class Utils(Methods, Config, Database, Helpers):
	# versions /

	userbot_version = "v.0.0.1"
	assistant_version = "v.0.0.1"
	python_version = str(platform.python_version())
	pyrogram_version = str(pyro_version)

	# containers /

	CMD_HELP = {}

	# owner details /

	owner_name = "🆂нιναηѕн 🇮🇳[Oғғʟιɴᴇ]"
	owner_id = 1986676404
	owner_username = "@Ryoishin"

	# other /

	Repo = "https://github.com/TeamAsterix/AsterixUB.git"
	StartTime = time.time()

	# debugging /

	logging.getLogger("pyrogram.syncer").setLevel(logging.CRITICAL) # turn off pyrogram logging
	logging.getLogger("pyrogram").setLevel(logging.CRITICAL)
	
	logging.basicConfig(format="%(asctime)s %(message)s")
	log = logging.getLogger("———")

	# telegraph /

	telegraph = Telegraph()
	telegraph.create_account(short_name=Config.TL_NAME if Config.TL_NAME else "Asterix Userbot")

