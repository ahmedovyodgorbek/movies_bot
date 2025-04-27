from aiogram import types
from aiogram import F
from aiogram.fsm.context import FSMContext

from handlers.check_admin_status import ads_supervisor
from router import router
from loader import db
from states.main import MovieDeleteForm
from keyboards.inline.delete_confirmation import confirm


@router.message(F.text == "🎥 Delete movie")
async def start_save_movie(message: types.Message, state: FSMContext):
    status = await ads_supervisor(message.from_user.id)
    if status:
        await message.answer("*Send the id of the movie:*", parse_mode="Markdown")
        await state.set_state(MovieDeleteForm.id)
    else:
        await message.answer(text=f"You do not have the permission")


@router.message(MovieDeleteForm.id)
async def get_movie_id(message: types.Message, state: FSMContext):
    id = message.text.strip()
    movie = db.get_movie_id(movie_id=id)
    if movie is not None:
        await message.answer("Confirm to delete", reply_markup=confirm())
        await state.update_data(id=id)
    else:
        await message.answer("Nothing found")


@router.callback_query(F.data == "confirm_delete")
async def confirm_delete(callback: types.CallbackQuery, state: FSMContext):
    """User confirmed deletion"""
    await callback.message.edit_text("✅ Movie has been deleted.")
    movie_data = await state.get_data()
    id = int(movie_data.get("id"))
    await callback.answer("deleted")
    try:
        db.delete_movie(id=id)
    except:
        await callback.answer("❌ Something went wrong")

    await state.clear()
    await callback.answer()


@router.callback_query(F.data == "cancel_delete")
async def cancel_delete(callback: types.CallbackQuery, state: FSMContext):
    """User cancelled deletion"""
    await callback.message.edit_text("✅ Deletion has been cancelled.")
    await state.clear()
    await callback.answer()
