from aiogram import types
from aiogram import F

from router import router
from handlers.check_admin_status import check_admin_status
from keyboards.reply.admin_menu import generate_admin_menu
from loader import db
from handlers.errors import report_error_to_admin


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
        total = db.get_total_users()
        text = ""
        for index, user in enumerate(users, start=1):
            fullname = user.get("fullname")
            username = user.get("username")
            telegram_id = user.get("telegram_id")
            text += f"{index}. <b>{fullname}</b> | {username} | {telegram_id}\n"
        try:
            text += f"\n<b>total users: {total['COUNT(*)']}</b>"
            await message.answer(text=text, parse_mode="HTML")
        except Exception as e:
            await report_error_to_admin(e)
            await message.answer(text="error with getting users")


@router.message(F.text == "🎥 Movies")
async def admin_work(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        movies = db.get_movies()
        if not movies:
            await message.answer("Nothing found")
            return
        text = ""
        try:
            for movie in movies:
                id = movie.get("id")
                name = movie.get("name")
                movie_id = movie.get("movie_id")
                text += f"{id}. <b>{name}</b> | {movie_id}\n"
            await message.answer(text=text, parse_mode="HTML")
        except:
            await message.answer(text="error with getting movies")
