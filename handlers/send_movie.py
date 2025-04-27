from aiogram import types
from aiogram import F
from aiogram.fsm.state import default_state

from router import router
from loader import bot
from config import SOURCE_CHANNEL
from handlers.check_membership import check_membership
from handlers.errors import report_error_to_admin
from keyboards.inline.join_channel import join_request
from loader import db


@router.message(F.text.isdigit())
async def send_movie(message: types.Message):
    status = await check_membership(message.from_user.id)
    print("!!!!!!!!!!!!!!!!!!!")
    if status:
        try:
            chat_id = message.from_user.id
            response = db.get_movie_id(message.text.strip())
            movie_id = int(response.get("movie_id"))
            await bot.copy_message(chat_id=chat_id,
                                   from_chat_id=SOURCE_CHANNEL,
                                   message_id=movie_id,
                                   protect_content=True
                                   )
        except Exception as e:
            await report_error_to_admin(e)
            await message.answer(text="""Nothing Found 😔""")

    else:
        await message.reply(text=f"Join the channel to use this bot ⬇️",
                            reply_markup=join_request())
