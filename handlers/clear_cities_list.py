from aiogram import types

from router import router
from loader import db


@router.message(lambda message: "🗑️ Delete my cities list" == message.text)
async def clear_cities(message: types.Message):
    await message.reply(text="Successfully cleared", reply_markup=types.ReplyKeyboardRemove())
    db.clear_cities(message.from_user.id)
