from aiogram import types
from aiogram import F

from router import router
from check_admin_status import check_admin_status
from keyboards.reply.admin_menu import generate_admin_menu
from loader import db


@router.message(F.text == "admin")
async def admin_work(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        await message.answer(text="Select one ⬇️",
                             reply_markup=generate_admin_menu())


@router.message(F.text == "👥 Users")
async def admin_work(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        users = db.get_users()
        text = ""
        for index, user in enumerate(users):
            text += f"{index}. <b>{user.get("fullname")}</b> | {user.get("username")} | {user.get("telegram_id")}\n"
        await message.answer(text=text, parse_mode="HTML")


@router.message(F.text == "🎥 Movies")
async def admin_work(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        movies = db.get_movies()
        text = ""
        for index, movie in enumerate(movies):
            text += f"{index}. <b>{movie.get("name")}</b> | {movie.get("movie_id")}\n"
        await message.answer(text=text, parse_mode="HTML")
