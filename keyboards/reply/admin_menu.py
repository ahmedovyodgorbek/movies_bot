from aiogram.utils.keyboard import ReplyKeyboardBuilder


def generate_admin_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="👥 Users")
    builder.button(text="🎥 Movies")
    builder.button(text="🎥 Add movie")
    builder.button(text="🎥 Delete movie")

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
