from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import SOURCE_CHANNEL


def join_request():
    builder = InlineKeyboardBuilder()
    builder.button(text="Movies", url=f"https://t.me/english_kinolar_y")
    return builder.as_markup()
