import telegram # type: ignore
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from weather import get_weather

#Bot token
TOKEN ="8683367558:AAGXtHDMcwipyCqSv6QGu2VaWQtt-44X-tI"

#start command
async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Weather",callback_data="weather")],
        [InlineKeyboardButton("Guess number", callback_data ="guess")],
        [InlineKeyboardButton("Help",callback_data = "help")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello, I`m your personal bot! \nWhat would you like to do?",
        reply_markup=reply_markup
    )
#button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "weather":
        await query.message.reply_text("Send me a city name")
    elif query.data == "guess":
        await query.message.reply_text("Starting number guess game!")
    elif query.data =="help":
        await query.message.reply_text(
            "Available commands: \n\n"
            "/start -Start the bot\n"
            "/weather [city] - Get weather\n " 
            "/help - Show this message"
        )
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
app.add_handler(CallbackQueryHandler(button_click))
app.run_polling()