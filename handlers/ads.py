import time
from aiogram import types
from aiogram import F

from router import router
from loader import db, bot
from handlers.check_admin_status import check_admin_status, ads_supervisor


@router.message(F.text == "📰 advertisement")
async def ads(message: types.Message):
    status = await check_admin_status(message.from_user.id)
    if status:
        await message.reply(text="send me the ads\n\n for example: !ads text")


@router.message()
async def send_ads(message: types.Message):
    status = await ads_supervisor(message.from_user.id)
    if status:
        if len(message.text) >= 10:
            users = db.get_users()
            for user in users:
                user_id = int(user.get("telegram_id"))
                await bot.copy_message(
                    chat_id=user_id,
                    from_chat_id=message.from_user.id,
                    message_id=message.message_id
                )
