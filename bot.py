import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8412718462:AAGfYzR2mWzJWjMamQEn-uPTxgo0FP5m2uM")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("شباحوووو")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling() 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def عبد(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ها اخ الكحبه خليتني اشتغل 24 ساعه شنو عبد يمك اني")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
