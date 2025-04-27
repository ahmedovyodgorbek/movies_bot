from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def confirm():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Yes", callback_data="confirm_delete")],
            [InlineKeyboardButton(text="❌ No", callback_data="cancel_delete")]
        ]
    )
    return keyboard
