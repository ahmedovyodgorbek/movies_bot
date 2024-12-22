from aiogram import types
from aiogram import F

from handlers.check_admin_status import ads_supervisor
from router import router
from loader import db
from logs import logger


@logger
@router.message(F.text == "🎥 how to save movie")
async def send_movie(message: types.Message):
    status = await ads_supervisor(message.from_user.id)
    if status:
        await message.reply(text="movie_name*movie_id")
    else:
        await message.reply(text=f"You do not have the permission")


@logger
@router.message(lambda message: '*' in message.text)
async def save_movie(message: types.Message):
    status = await ads_supervisor(message.from_user.id)
    if status:
        movie_name = (message.text.split('*'))[0]
        movie_id = (message.text.split('*'))[1]
        if db.add_movie(movie_name, movie_id) is True:
            last_movie = db.get_last_movie()
            id = last_movie.get('id')
            await message.answer(text=f"{id} | {movie_id}. {movie_name} has been added successfully !")
        else:
            await message.answer(text="There is something wrong !")
