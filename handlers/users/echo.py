from aiogram import types
from loader import dp


# ловит в хендлер в фото
# @dp.message_handler(content_types = types.ContentTypes.PHOTO)

@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f'Cам ты {message.text}')

    # оформить, как ответ на конретное сообщение
    # await message.reply(f'Cам ты {message.text}')
