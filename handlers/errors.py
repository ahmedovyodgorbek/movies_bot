from aiogram import Bot
import traceback

from config import ADMIN_ID
from loader import bot


async def report_error_to_admin(error_message):
    """Send error report to admin"""
    try:
        await bot.send_message(chat_id=ADMIN_ID, text=f"⚠️ Error occurred:\n\n{error_message}")
    except Exception as send_error:
        print("Failed to report error:", send_error)
