from aiogram import types
from loader import dp


@dp.message_handler(text='Получить информацию')
async def bot_info(message: types.Message):
    text = f'Добро пожаловать в студию разработки Delpy Studio!\n\n# НАПИСАТЬ ТЕКСТ'

    photo = '/home/egor/Documents/github/delpy_bot/media/Delpy.png'
    await message.answer_photo(types.InputFile(photo))
    await message.answer(text)

    # как удалить сообщение удаления сообщения
    # await message.answer(text).delete()
