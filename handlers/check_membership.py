from loader import bot


async def check_membership(telegram_id):
    # try:
    membership = await bot.get_chat_member("@english_kinolar_y", telegram_id)
    return membership.status in ['member', 'administrator', 'creator']
# except:
#     return False
