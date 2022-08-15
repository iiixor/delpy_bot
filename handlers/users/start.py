from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
# достаем menu из дир-и delpy_bot -> keyboards -> default
from keyboards.default import menu

emoji = u'\U0001F4A8'

# @dp.message_handler ловит только комманду /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # выводим текст методом message.answer
    # и в аргументе предаем прям тот, текст, который выведется
    # при вводе /start также появляется menu с кнпоками, благодаря
    # reply_markup=menu
    # menu указывается в keyboards->default->menu
    await message.answer(f'<b>Привет</b>,{emoji} {message.from_user.full_name}!', reply_markup=menu)
