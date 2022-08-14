from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

switch_language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='English')
        ],
        [
            KeyboardButton(text='Русский')
        ]
    ],
    resize_keyboard=True
)
