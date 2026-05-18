from telegram import Update
from telegram.ext import ContextTypes

import pyautogui


async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):

    image = pyautogui.screenshot()

    path = "screenshots/screen.png"

    image.save(path)

    await update.message.reply_photo(photo=open(path, "rb"))