from telegram import Update
from telegram.ext import CallbackContext

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Salam. Mən Student Project satışları üçün Munir Nəsibzadə tərəfindən dizayn edildim!\n\n"
        "/start - Botu başlat\n"
        "/help - Botun əmrlərini gör"
    )