import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import TOKEN
import keyboards as kb
import database as db


bot = Bot(token=TOKEN)
dp = Dispatcher()


# Старт
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "💪 Добро пожаловать в фитнес-бот!\nВыберите действие:",
        reply_markup=kb.main_menu
    )


# Купить абонемент
@dp.message(F.text == "🏋️ Купить абонемент")
async def buy(message: Message):
    await message.answer(
        "Выберите тариф:",
        reply_markup=kb.tariffs_menu
    )


# Тарифы
@dp.message(F.text.contains("месяц"))
async def tariff(message: Message):
    await message.answer(
        "✅ Отличный выбор!\n\n"
        "Для оформления напишите:\n"
        "Имя и телефон через пробел\n\n"
        "Пример: Иван +79991234567"
    )


# Запись клиента
@dp.message(F.text.regexp(r".+\s\+7\d{10}"))
async def register(message: Message):

    data = message.text.split()
    name = data[0]
    phone = data[1]

    db.add_client(
        message.from_user.id,
        name,
        phone
    )

    await message.answer(
        "🎉 Заявка принята!\nТренер свяжется с вами."
    )


# Поддержка
@dp.message(F.text == "📞 Поддержка")
async def support(message: Message):
    await message.answer(
        "📩 Напишите: @your_manager"
    )


# Назад
@dp.message(F.text == "⬅️ Назад")
async def back(message: Message):
    await message.answer(
        "Главное меню:",
        reply_markup=kb.main_menu
    )


async def main():
    db.create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())