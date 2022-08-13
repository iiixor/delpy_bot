from aiogram import types
from loader import dp


@dp.message_handler(text='Получить ссылку')
async def bot_info(message: types.Message):
    url = f'https://core.telegram.org/bots/api#copymessage'
    await message.answer(url)
