from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *
# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задаавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Получить информацию {emoji_information}'),
            KeyboardButton(text=f'Посмотреть портфолио {emoji_list}')
        ],
        [
            KeyboardButton(text=f'Пройти опрос {emoji_paper_pen}'),
            KeyboardButton(text=f'Поменять язык {emoji_ruflag}')
        ],
        [
            KeyboardButton(text=f'Отзывы {emoji_star}'),
            KeyboardButton(text=f'Прайс {emoji_abacus}')
        ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
