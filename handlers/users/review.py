from aiogram import types
from loader import dp


# @dp.message_handler ловит только сообщение 'Оставить отзыв'
@dp.message_handler(text='Оставить отзыв')
async def bot_portfolio(message: types.Message):
    # задаем текст, который будем выводить
    text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text)

    # вот как можно отправить опрос
    # await message.answer_poll(question='Выберете свою оценку', options=['5', '4', '3', '2', '1'], is_anonymous=False)
    # QESTION:  передаетеся название опроса
    # в options передаютеся поля опроса
