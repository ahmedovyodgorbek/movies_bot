from aiogram import types
from aiogram import F

from router import router
from loader import bot
from config import SOURCE_CHANNEL
from handlers.check_membership import check_membership
from keyboards.inline.join_channel import join_request
from loader import db


@router.message(F.text.isdigit())
async def send_movie(message: types.Message):
    status = await check_membership(message.from_user.id)
    if status:
        try:
            chat_id = message.from_user.id
            response = db.get_movie_id(message.text)
            movie_id = int(response.get("movie_id"))
            await bot.copy_message(chat_id=chat_id,
                                   from_chat_id=SOURCE_CHANNEL,
                                   message_id=movie_id,
                                   protect_content=True
                                   )
            await message.answer(text="""Here is your movie. I am happy to help 😊""")
        except:
            await message.reply(text="""there is no movie with this id ❌\n\nTry again 😊""")

    else:
        await message.reply(text=f"Join the channel to use this bot ⬇️",
                            reply_markup=join_request())
