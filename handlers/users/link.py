from aiogram import types
from loader import dp


@dp.message_handler(text='Перейти на сайт')
async def bot_link(message: types.Message):
    # задаем текст, который будем выводить (в переменную url)
    url = f'# ДОБАВИТЬ РЕАЛЬНУЮ ССЫЛКУ\n\n На гит например'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(url)
