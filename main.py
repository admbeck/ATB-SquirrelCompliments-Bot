#!/usr/bin/env python3
from keyboards import *
from database import *
import os

from aiogram import Dispatcher, executor, Bot
from aiogram.types import Message, CallbackQuery,ReplyKeyboardRemove
from dotenv import *

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN, parse_mode='MarkdownV2')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    """Greet user"""
    await message.answer('Hi, Squirrel')
    await show_buttons(message)

async def show_buttons(message: Message):
    """Show buttons to the user"""
    await message.answer("Tap the button", reply_markup=new_compliment())

@dp.message_handler(content_types=['text'])
async def send_compliment(message: Message):
    """Sends random compliment from the database to user"""
    await message.answer(select_compliment())


if __name__ == '__main__':
    executor.start_polling(dp)
