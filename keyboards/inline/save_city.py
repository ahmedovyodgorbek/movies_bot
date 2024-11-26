from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def save_city_menu(city_name):
    builder = InlineKeyboardBuilder()
    builder.button(text="Add to my cities", callback_data=f"save:{city_name}")
    return builder.as_markup()

