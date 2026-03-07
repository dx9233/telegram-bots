from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Buy Aboniment")],
        [KeyboardButton(text="Recording")],
        [KeyboardButton(text="Support")]
    ],
    resize_keyboard=True
)


tariffs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 mounth — 10$")],
        [KeyboardButton(text="3 mounth — 20$")],
        [KeyboardButton(text="Back")]
    ],
    resize_keyboard=True
)