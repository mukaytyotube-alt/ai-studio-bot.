
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎨 Создать фото")],
        [KeyboardButton(text="🎬 Создать видео")],
        [KeyboardButton(text="🖼️ Редактировать фото")],
        [KeyboardButton(text="ℹ️ Помощь")]
    ],
    resize_keyboard=True
)

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Добро пожаловать в AI Studio! 🚀\n"
        "Выбери, что хочешь создать:",
        reply_markup=keyboard
    )

@dp.message(F.text == "🎨 Создать фото")
async def photo(message: Message):
    await message.answer("🎨 Скоро здесь появится генерация фото!")

@dp.message(F.text == "🎬 Создать видео")
async def video(message: Message):
    await message.answer("🎬 Скоро здесь появится генерация видео!")

@dp.message(F.text == "🖼️ Редактировать фото")
async def edit(message: Message):
    await message.answer("🖼️ Скоро здесь появится редактирование фото!")

@dp.message(F.text == "ℹ️ Помощь")
async def help_message(message: Message):
    await message.answer("AI Studio — твоя ИИ-студия!")

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN не настроен")

    bot = Bot(token=token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
