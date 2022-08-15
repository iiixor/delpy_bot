from aiogram import types
from loader import dp


# @dp.message_handler ловит только сообщение 'Посмотреть портфолио'
@dp.message_handler(text='Посмотреть портфолио \ud83d\udccb')
async def bot_portfolio(message: types.Message):
    # задаем текст, который будем выводить
    text = 'Наше портфолио:\n@delpy_bot'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text)
