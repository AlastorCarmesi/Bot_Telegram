#Librerias para el bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola soy tu bot, Hola mundo")

    app = ApplicationBuilder().token("8626115500:AAFn4g4MADGi_iI-OyiS_X1rHAO5xo99tI8").build()
    app.add_handler(CommandHandler("start", say_hello))
    app.run_polling(allowing_updates=update.ALL_TYPES)