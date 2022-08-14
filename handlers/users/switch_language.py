from aiogram import types
from loader import dp
from keyboards.default import switch_language
from keyboards.default import menu


@dp.message_handler(text=('Поменять язык' or 'Switch language'))
async def bot_switch_language(message: types.Message):
    text = 'Выберете язык'
    # задаем текст, который будем выводить (в переменную url)
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=switch_language)


@dp.message_handler(text=('Русский'))
async def bot_get_russian(message: types.Message):
    text = 'Z'
    await message.answer(text, reply_markup=menu)


@dp.message_handler(text=('English'))
async def bot_get_russian(message: types.Message):
    text = 'Я ОСУЖДАЮ'
    await message.answer(text, reply_markup=menu)
