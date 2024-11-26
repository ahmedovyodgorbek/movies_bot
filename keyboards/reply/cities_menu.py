from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from loader import db


def generate_cities_menyu(telegram_id):
    builder = ReplyKeyboardBuilder()
    cities = db.get_cities(telegram_id)
    for city in cities:
        builder.button(text=city.get("city_name"))

    builder.adjust(2)

    builder.row(
        KeyboardButton(text="🗑️ Delete my cities list")
    )
    return builder.as_markup(resize_keyboard=True)
