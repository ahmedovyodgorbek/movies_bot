from aiogram import types
from aiogram import F

from router import router
from loader import db, bot
from handlers.check_admin_status import check_admin_status


@router.message(F.text == "📰 advertisement")
async def ads(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        await message.reply(text="send me the ads\n\n for example: !ads text")


@router.message(lambda message: "!ads" in message.text)
async def send_ads(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        text = message.text.replace("!ads", "", 1)
        users = db.get_users()
        for user in users:
            await bot.send_message(int(user.get("telegram_id")), text)
