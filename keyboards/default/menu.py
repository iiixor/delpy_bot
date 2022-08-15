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
            KeyboardButton(text='Пройти опрос'),
            KeyboardButton(text='Поменять язык')
        ],
        [
            KeyboardButton(text='Отзывы'),
            KeyboardButton(text='Прайс')
        ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
