#!/usr/bin/env python3
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def new_compliment():
    """button to get new compliment"""
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="🐿️")]
        ], resize_keyboard=True)
