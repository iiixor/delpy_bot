from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


switch_language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='English \ud83c\uddec\ud83c\udde7')
        ],
        [
            KeyboardButton(text='Русский \ud83c\uddf7\ud83c\uddfa')
        ]
    ],
    resize_keyboard=True
)
