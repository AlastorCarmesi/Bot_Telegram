#Librerias para el bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TK = "8626115500:AAEoxJrhlmjXAnGAuA3PzMMB5c8rHdPGOOQ"

#Metodos para el bot
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!, bot iniciado correctamente")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.args)

application = ApplicationBuilder().token(TK).build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( CommandHandler( "echo", echo ) )
application.add_handler( CommandHandler( "help", say_hello ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)