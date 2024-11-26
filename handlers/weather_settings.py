from aiogram import types

from router import router
from handlers.weather_data import get_weather_data
from keyboards.inline.save_city import save_city_menu


@router.message(lambda messgae: "☁️ Check weather" == messgae.text)
async def ask_city_name(message: types.Message):
    await message.answer(text="Send the city name! (e.g.,New York)")


@router.message()
async def open_weather(message: types.Message):
    city_name = message.text.strip()
    weather_data = get_weather_data(city_name)
    if weather_data:
        await message.answer(text=weather_data, parse_mode="HTML", reply_markup=save_city_menu(city_name))
    else:
        await message.reply(text="The city name could not be found 😔")
