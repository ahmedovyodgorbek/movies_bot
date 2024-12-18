from aiogram.utils.keyboard import ReplyKeyboardBuilder


def generate_admin_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="👥 Users")
    builder.button(text="🎥 Movies")
    builder.button(text="📰 advertisement")
    builder.button(text="🎥 how to save movie")

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
