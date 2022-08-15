from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задаавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить информацию \ud83d\udccc'),
            KeyboardButton(text='Посмотреть портфолио \ud83d\udccb')
        ],
        [
            KeyboardButton(text='Пройти опрос\ud83d\udcdd'),
            KeyboardButton(text='Поменять язык \ud83c\uddf7\ud83c\uddfa')
        ],
        [
            KeyboardButton(text='Отзывы \u2b50\ufe0f'),
            KeyboardButton(text='Прайс \ud83e\uddee')
        ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
