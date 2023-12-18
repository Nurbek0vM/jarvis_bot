from aiogram import Dispatcher,Bot
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
GROUP_ID = config("GROUP_ID")
MEDIA_DESTINATION = config("MEDIA_DESTINATION")