from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏋️ Купить абонемент")],
        [KeyboardButton(text="📅 Записаться")],
        [KeyboardButton(text="📞 Поддержка")]
    ],
    resize_keyboard=True
)


tariffs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 месяц — 2500₽")],
        [KeyboardButton(text="3 месяца — 6500₽")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)