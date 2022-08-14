from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задаавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить информацию'),
            KeyboardButton(text='Посмотреть портфолио')
        ],
        [
            KeyboardButton(text='Перейти на сайт')
        ]
    ],
    resize_keyboard=True
)
