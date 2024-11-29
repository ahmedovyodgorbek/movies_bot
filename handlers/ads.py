from aiogram import types
from aiogram import F

from router import router
from loader import db, bot
from check_admin_status import check_admin_status
from keyboards.reply.admin_menu import generate_admin_menu


@router.message(F.text == "📰 advertisement")
async def ads(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        await message.reply(text="send me the ads\n\n for example: !ads text")


@router.message(lambda message: "!ads" in message.text)
async def send_ads(messgae: types.Message):
    text = messgae.text.replace("!ads", "", 1)
    users = db.get_users()
    for user in users:
        await bot.send_message(int(user.get("telegram_id")), text)
