from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from utils.config import TOKEN

from commands.system import sysinfo, processes
from commands.screenshot import screenshot
from commands.clipboard import clipboard
from commands.shell import shell
from commands.help import help_command

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Online ✅")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sysinfo", sysinfo))
app.add_handler(CommandHandler("processes", processes))
app.add_handler(CommandHandler("screenshot", screenshot))
app.add_handler(CommandHandler("clipboard", clipboard))
app.add_handler(CommandHandler("shell", shell))
app.add_handler(CommandHandler("help", help_command))

print("Bot Running...")
app.run_polling()