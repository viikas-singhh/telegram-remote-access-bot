from telegram import Update
from telegram.ext import ContextTypes

import platform
import psutil


async def sysinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    info = f"""
System: {platform.system()}
Machine: {platform.node()}
CPU Usage: {cpu}%
RAM Usage: {ram}%
"""

    await update.message.reply_text(info)


async def processes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    process_list = []

    for proc in psutil.process_iter(['name']):

        try:
            name = proc.info['name']

            if name:
                process_list.append(name)

        except:
            pass

    unique_processes = list(set(process_list))

    output = "\n".join(unique_processes[:30])

    await update.message.reply_text(output)