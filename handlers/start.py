from aiogram import types
from aiogram.filters.command import CommandStart

from router import router
from keyboards.reply.main_keyboard import generate_main_menu
from loader import db


@router.message(CommandStart())
async def start(message: types.Message):
    telegram_id = message.from_user.id
    fullname = message.from_user.full_name
    username = message.from_user.username
    first_name = message.from_user.first_name
    try:
        db.register_user(telegram_id, fullname, username)
        await message.answer(text="Assalomu alaykum 😊", reply_markup=generate_main_menu())
    except:
        await message.answer(text=f"I'm glad to see you again {first_name} 👋", reply_markup=generate_main_menu())

