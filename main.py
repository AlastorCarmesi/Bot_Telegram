#Librerias para el bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!, bot iniciado correctamente")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

application = ApplicationBuilder().token("8626115500:AAEoxJrhlmjXAnGAuA3PzMMB5c8rHdPGOOQ").build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( CommandHandler( "echo", echo ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)