from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

switch_language = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Русский', callback_data='russian')
        ]
    ]
)
