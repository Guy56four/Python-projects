import telegram # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from weather import get_weather

#Bot token
TOKEN ="8683367558:AAFipejuCiOFFUBwBkx1K6WEbywYHKymNWQ"

#start command
async def start ( update: telegram.Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello i`m your personal bot! \n')
#help command
async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        " Available commands:\n\n"
        "/start - Start the bot\n"
        "/weather [city] - Get weather for any city\n"
        "/help - Show this message"
    )

async def weather (update: telegram.Update, context:ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a city!")
        return
    city ="".join(context.args)
    result = get_weather(city)
    await update.message.reply_text(result)

#Run the bot
app = ApplicationBuilder ().token(TOKEN).build()
app.add_handler (CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("weather", weather))
print('Bot is runnig....')
app.run_polling()

