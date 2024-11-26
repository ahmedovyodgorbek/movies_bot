from requests import get as GET
from datetime import datetime

from config import OPEN_WEATHER_API


def get_weather_data(city_name):
    PARAMS = {
        "q": city_name,
        "appid": OPEN_WEATHER_API,
        "units": "metric"
    }
    response = GET(url=f"https://api.openweathermap.org/data/2.5/weather", params=PARAMS)

    if not response.ok:
        return None

    data = response.json()
    sunrise = data['sys']['sunrise']
    sunrise_time = datetime.fromtimestamp(sunrise)
    sunset = data['sys']['sunset']
    sunset_time = datetime.fromtimestamp(sunset)

    text = ""
    text += f"🏙️  ️Today, in <b>{city_name}</b>\n\n"

    text += f"☁️ Weather condition: <b>{data['weather'][0]['description']}</b>\n"
    text += f"🌡️ Temperature: <b>{data['main']['temp']}</b> C\n"
    text += f"💧 Humidity: <b>{data['main']['humidity']}</b> %\n\n"

    text += f"🌅 Sunrise: <b>{sunrise_time}</b>\n"
    text += f"🌇 Sunset: <b>{sunset_time}</b>\n"

    return text
