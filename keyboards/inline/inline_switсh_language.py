from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import *


# пишем ссылки для тех кнопок, которые перекидывают на ссылки
GIT_HUB_LINK = "https://github.com/wywdelpy"
KWORK_LINK = "https://kwork.ru/user/alex_odin"
ADMIN_LINK = "https://t.me/wywmusic"

# по своей структуре очень похоже на созадние обычных кнопок
# добавляем клавиатуру и передаем в нее метод inline_keyboard
# внутри которого добавляем сами кнопки с обязательным параметром text
# также внутрь передаем callback_data для созданию тригера на кнопку тк сказать
# обратите внимание на то, как меняется callback_data при первом упоминании и при втором


switch_language = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Русский', callback_data=switch_callback.new(language='russian'))
        ],
        [
            InlineKeyboardButton(text='English', callback_data="switcher:english")
        ]
    ]
)
# по сути то же самое, что сверху
# однако тут обратите внимание, что еще передается url, данный параметр
# при нажатии кнопку пересылатет по ссылке

media_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text='Git Hub', callback_data=media_callback.new(platform='git_hub'), url=GIT_HUB_LINK)
        ],
        [
            InlineKeyboardButton(text='Kwork', callback_data="media:kwork", url=KWORK_LINK)
        ],
        [
            InlineKeyboardButton(text='Задать вопрос', callback_data="media:answer", url=ADMIN_LINK)
        ]
    ]
)

# по сути то же самое, что сверху

poll_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Google Forms', callback_data=poll_callback.new(platform='google_forms'))
        ]
    ]
)

# на этом шаге, я думаю понятно, как создавать кнопки в этой дир-и

review_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Платформа №1', callback_data=review_callback.new(platform='platform_1'))
        ],
        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data="review:write_a_review")
        ]
    ]
)


price_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text='Разработка Telegram ботов', callback_data=price_callback.new(type='TG_Bots'))
        ],
        [
            InlineKeyboardButton(text='Работа с API Google Sheets', callback_data="price:ggsh_api")
        ]
    ]
)
