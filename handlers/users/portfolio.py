from aiogram import types
from loader import dp


@dp.message_handler(text='Посмотреть портфолио')
async def bot_info(message: types.Message):
    text = 'Наше портфолио:\n@delpy_bot\n'
    await message.answer(text)
