from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT, DB_HOST
from utils.db_api.db import Database

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

db = Database(db_name=DB_NAME,
              db_password=DB_PASSWORD,
              db_user=DB_USER,
              db_port=DB_PORT,
              db_host=DB_HOST
              )

db.create_users_table()
db.create_cities_table()
