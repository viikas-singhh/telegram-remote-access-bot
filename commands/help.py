from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = """
🤖 Telegram Remote Bot Commands

/start - Check bot status

/sysinfo - Show system information

/screenshot - Capture desktop screenshot

/processes - Show running processes

/clipboard - Show clipboard text

/shell <command> - Run shell command

Examples:
/shell whoami
/shell ipconfig
/shell tasklist
"""

    await update.message.reply_text(message)