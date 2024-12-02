from loader import bot
from config import SOURCE_CHANNEL


async def check_admin_status(telegram_id):
    membership = await bot.get_chat_member("@english_kinolar_y", telegram_id)
    return membership.status in ['administrator', 'creator']


async def ads_supervisor(telegram_id):
    membership = await bot.get_chat_member(SOURCE_CHANNEL, telegram_id)
    return membership.status in ['administrator', 'creator', 'owner']
