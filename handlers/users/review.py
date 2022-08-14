from aiogram import types
from loader import dp


# @dp.message_handler ловит только сообщение 'Посмотреть портфолио'
@dp.message_handler(text='Оставить отзыв')
async def bot_portfolio(message: types.Message):
    # задаем текст, который будем выводить
    text = 'Наше портфолио:\n@delpy_bot\n'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer_poll(question: 'Выберете свою оценку', options: ['5', '4', '3', '2', '1'])
