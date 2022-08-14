from aiogram import types
from loader import dp
from keyboards.default import switch_language
from keyboards.default import menu


# если в боте сообщение Поменять язык или Switch language
@dp.message_handler(text=('Поменять язык' or 'Switch language'))
async def bot_switch_language(message: types.Message):
    text = 'Выберете язык'
    # задаем текст, который будем выводить (в переменную url)
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=switch_language)


# после шага выше спавняться кнопки, которые заданы в
# keyboads -> default -> switch_language


# если Русский
@dp.message_handler(text=('Русский'))
async def bot_get_russian(message: types.Message):
    text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    await message.answer(text, reply_markup=menu)


# если English
@dp.message_handler(text=('English'))
async def bot_get_russian(message: types.Message):
    text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    await message.answer(text, reply_markup=menu)
