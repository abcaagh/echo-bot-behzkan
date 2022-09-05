import logging
import os
from aiogram.utils.executor import start_webhook
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5547260249:AAHMBmcEkHb0bRtvzpyx0-ot6PWqAxssknY'
HEROKU_APP = 'echo-bot-behzkan'
logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp)
