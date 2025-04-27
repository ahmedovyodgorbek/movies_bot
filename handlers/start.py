from aiogram import types
from aiogram.filters.command import CommandStart
import traceback

from router import router
from loader import db
from handlers.check_membership import check_membership
from keyboards.inline.join_channel import join_request
from handlers.errors import report_error_to_admin


@router.message(CommandStart())
async def start(message: types.Message):
    status = await check_membership(message.from_user.id)
    if status:
        try:
            telegram_id = message.from_user.id
            fullname = message.from_user.full_name
            username = message.from_user.username
            db.register_user(telegram_id, fullname, username)
            await message.answer(text=f"""
                <b>{message.from_user.username} Hi 👋 </>\n\nSend the movie id ⬇️
            """, parse_mode="HTML")

        except Exception as e:
            await message.answer(text=f"""
                <b>{message.from_user.username} Hi 👋 </>\n\nSend the movie id ⬇️
            """, parse_mode="HTML")
    else:
        await message.reply(text=f"Join the channel to use this bot ⬇️",
                            reply_markup=join_request())
