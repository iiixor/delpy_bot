from aiogram import types
from loader import dp


from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text='Получить информацию')
async def bot_info(message: types.Message):
    # перменной text присваиваем строку, которую в дальнешем будем выводить
    text = f'Добро пожаловать в студию разработки Delpy Studio!\n\n# НАПИСАТЬ ТЕКСТ'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    photo = '/home/egor/Documents/github/delpy_bot/media/Delpy.png'
    # методом message.answer_photo отправляем фото и передаем туда photo
    await message.answer_photo(types.InputFile(photo))
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text, reply_markup=media_buttons)
