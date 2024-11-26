from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
OPEN_WEATHER_API = env.str("OPEN_WEATHER_API")
DB_NAME = env.str("DB_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_USER = env.str("DB_USER")
DB_PORT = env.int("DB_PORT")
DB_HOST = env.str("DB_HOST")
