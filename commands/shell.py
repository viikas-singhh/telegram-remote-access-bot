from telegram import Update
from telegram.ext import ContextTypes

import subprocess


async def shell(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        command = " ".join(context.args)

        if not command:
            await update.message.reply_text("Usage: /shell <command>")
            return

        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )

        if len(result) > 4000:
            result = result[:4000]

        await update.message.reply_text(f"Output:\n\n{result}")

    except Exception as e:
        await update.message.reply_text(f"Error:\n{e}")