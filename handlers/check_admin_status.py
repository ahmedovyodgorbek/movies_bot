from loader import bot


async def check_admin_status(telegram_id):
    membership = await bot.get_chat_member("@english_kinolar_y", telegram_id)
    return membership.status in ['administrator', 'creator']
