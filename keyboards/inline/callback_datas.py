from aiogram.utils.callback_data import CallbackData


# тут пишем так называемые тригеры для кнопок
# в 1м параметре CallbackData предаетсям тип кнопки, а затем один из парметров типа


switch_callback = CallbackData("switcher", "language")

media_callback = CallbackData("media", "platform")

poll_callback = CallbackData("poll", "platform")

review_callback = CallbackData("review", "platform")

price_callback = CallbackData("price", "type")

# то же почти везде копи-паст)))))
