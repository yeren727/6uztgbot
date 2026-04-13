import asyncio
from os import getenv
from dotenv import load_dotenv  # 1. Добавили импорт

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()  # 2. Загрузили переменные из файла .env

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram.")

@dp.message(Command("salom"))
async def command_salom_handler(message: Message) -> None:
    await message.answer("Salom! Men 24/7 Telegram Botman!.")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
