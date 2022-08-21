from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Получить информацию {emoji_information}')
async def bot_info(message: types.Message):
    text = 'Добро пожаловать в студию разработки Delpy Studio!\nРады вас видеть в нашем официальном телеграм боте Delpy Studio! Здесь вы сможете:\n- Посмотреть перечень наших услуг\n- Получить ссылку на наш Git Hub, Kwork\n- Задать вопрос нашим админам\n- Составить ваш заказ на Google forms'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    photo = 'media/Delpy.png'
    # методом message.answer_photo отправляем фото и передаем туда photo
    await message.answer_photo(types.InputFile(photo))
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text, reply_markup=media_buttons)
    # await bot.delete_message(message.chat.id, message.message_id)

# УДАЛЕНИЕ СООБЕЩНИЙ

# @dp.message_handler()
# async def bot_delete(message: types.Message):
#     await bot.delete_message(message.chat.id, message.message_id-2)



#@dp.message_handler()
# async def bot_delete(message: types.Message):
#     if message.from_user.id == (await bot.me).id:
#         await bot.delete_message(message.)
