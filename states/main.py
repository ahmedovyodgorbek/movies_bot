from aiogram.fsm.state import State, StatesGroup


class MovieForm(StatesGroup):
    name = State()
    movie_id = State()


class MovieDeleteForm(StatesGroup):
    id = State()
