import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import TOKEN
import keyboards as kb
import database as db


bot = Bot(token=TOKEN)
dp = Dispatcher()


# Start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Welcome To Fitness Bot!\nChoose The Action:",
        reply_markup=kb.main_menu
    )


# Buy Plan
@dp.message(F.text == "Buy Aboniment")
async def buy(message: Message):
    await message.answer(
        "Choose The Plan:",
        reply_markup=kb.tariffs_menu
    )


# Plans
@dp.message(F.text.contains("месяц"))
async def tariff(message: Message):
    await message.answer(
        "Successfull!!\n\n"
        "For order write:\n"
        "First Name and Last Name\n\n"
        "Example: John +79991234567"
    )


# Recording Client
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
        "Order Successfull!\nThe coach will contact you."
    )


# Поддержка
@dp.message(F.text == "Support")
async def support(message: Message):
    await message.answer(
        "Write: @your_manager"
    )


# Назад
@dp.message(F.text == "Back")
async def back(message: Message):
    await message.answer(
        "Home:",
        reply_markup=kb.main_menu
    )


async def main():
    db.create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())