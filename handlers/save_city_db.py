from aiogram import types

from router import router
from loader import db
from keyboards.reply.cities_menu import generate_cities_menyu


@router.callback_query(lambda call: "save" in call.data)
async def save_city(call: types.CallbackQuery):
    city_name = call.data.split(":")[-1].title()
    user_id = call.from_user.id
    try:
        db.register_city(city_name, user_id)
        await call.message.answer(text=f"{city_name} has been added to my cities",
                                  reply_markup=generate_cities_menyu(user_id))
    except:
        await call.answer(text=f"{city_name} is already in your cities list", show_alert=True)
