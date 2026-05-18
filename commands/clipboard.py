from telegram import Update
from telegram.ext import ContextTypes

import pyperclip


async def clipboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = pyperclip.paste()

    if not text:
        text = "Clipboard is empty"

    await update.message.reply_text(f"Clipboard:\n\n{text}")