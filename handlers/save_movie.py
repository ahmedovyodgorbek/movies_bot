from aiogram import types
from aiogram import F
from aiogram.fsm.context import FSMContext
import traceback

from handlers.check_admin_status import ads_supervisor
from router import router
from loader import db, bot
from states.main import MovieForm


@router.message(F.text == "🎥 Add movie")
async def start_save_movie(message: types.Message, state: FSMContext):
    status = await ads_supervisor(message.from_user.id)
    if status:
        await message.answer("*Send the name of the movie:*", parse_mode="Markdown")
        await state.set_state(MovieForm.name)
    else:
        await message.answer(text=f"You do not have the permission")


@router.message(MovieForm.name)
async def get_movie_name(message: types.Message, state: FSMContext):
    movie_name = message.text.strip()
    await state.update_data(name=movie_name)
    await message.answer("*Send an unique id for the movie:*", parse_mode="Markdown")
    await state.set_state(MovieForm.movie_id)


@router.message(MovieForm.movie_id)
async def get_movie_id(message: types.Message, state: FSMContext):
    movie_id = message.text.strip()
    movie = db.get_movie_id(movie_id=movie_id)
    if movie is not None:
        await message.answer("Movie exists with this id")
        return

    movie_data = await state.get_data()
    name = movie_data['name']
    if db.add_movie(name=name, movie_id=movie_id):
        await message.answer("The movie has been added")
    else:
        await message.answer("Something went wrong")

    await state.clear()
