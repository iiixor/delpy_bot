from gettext import dpgettext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    #Сюда попадает сообщение пользователю, что он начал тестирование
    await message.answer(


    
    )
    #Тут находится то, что отвечает бот
    await Test.Q1.set()
    #await Test.first()
    dp.message_handler(state=Test.Q1)
    async def answer_q1(message: types.Message, FSMContext):
    #Присвоение состояния ответа на первый вопрос
         anwser = message.text

         await state.update_data(answer1=answer)

         await message.answer(


         )
         await Test.next()
    @dp.message_handler(state=Test.Q1)
    async def answer_q2(message: Types.Message, state: FSMContext):   
        data = await state.get_data()
        answer = data.get('answer1')
        answer2 = message.text

        await message.answer()
        #await message.answer()
        #await message.answer()
        #тут находятся ответы
        await state.reset_state()
        #сброс состояния
         
