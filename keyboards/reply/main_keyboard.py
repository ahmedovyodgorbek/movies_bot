from aiogram.utils.keyboard import ReplyKeyboardBuilder


def generate_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="☁️ Check weather")
    return builder.as_markup(resize_keyboard=True)
