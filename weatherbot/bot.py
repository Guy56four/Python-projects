import telegram # type: ignore
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, filters, ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from weather import get_weather
import random

#Bot token
TOKEN ="8683367558:AAFdebAaM9MznQ2FbA-qACgaVQVG05MzstE"
#active games for each user
games ={}
tasks = {}

#start command
async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Callculator", callback_data='to-do')],
        [InlineKeyboardButton("Calculator",callback_data='calc')],
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
        user_id = query.from_user.id
        games[user_id] = {'number': random.randint(1,100), 'attempts' : 0}
        await query.edit_message_text("I picked a number  between 1-100!\n Send your gueess!")
    elif query.data =="help":
        await query.message.reply_text(
            "Available commands: \n"
            "/start -Start the bot\n"
            "/weather [city] - Get weather\n " 
            "/help - Show this message")
    elif query.data == "calc": 
        await query.edit_message_text("Send me a math  expression! \nExample: 10/5")
    elif query.data =="todo":
        await query.edit_message_text("To do list commands \n\n"
                                      "/addtask [task] - Add a tsk \n"
                                      "viewtasks- view all tasks \n"
                                      "/deleteatsk[number]- delete a rask")
        

        
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

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

async def addtask(update : Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Please provide a task /n Example: /addtask\nExample  Buy groceriec")
        return
    task = " ". join(context.args)
    if user_id not in tasks:
        tasks[used_id] = []
    tasks[user_id].append(task)
    await update.message.reply_text(f"Task added: {task}")

async def viewtasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in tasks or len(tasks[user_id]) == 0:
        await update.message.reply_text("No tasks yet!")
        return
    task_list ="\n".join([f"{i+1}. {t}" for i, t in enumerete (tasks[user_id])])
    await update.message.reply_text(f"Your tasks: \n\n{task_list}")

async def deletetask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Please provide a task number!\nExample: /deletetask 1")
        return
    try:
        num = int(context.args[0]) -1
        removed = tasks [used_id].pop (num)
        await update.message.reply_text (f" Deleted task{removed}")
    except:
        await update.message.reply_text (f"Invalid task number")


    if user_id in games:
        try:
            guess = int(text)
            games[user_id]['attempts'] +=1
            secret = games [user_id]['number']

            if guess < secret:
                await update.message.reply_text("Too low! Try again!")
            elif guess > secret: 
                await update.message.reply_text("Too high! Try again!")
            else:
                attempts = games [user_id]['attempts']
                del games [user_id]
                await update.message.reply_text(f" You got it in {attempts} attempts!")
        except ValueError:
            await update.message.reply_text("Please send a number!")
    else:
        try:
            result = eval (text)
            await update.message.reply_text(f"Result: { result}")
        except:
            await update.message.reply_text("I do not understand that. Try \start   ")


#Run the bot
app = ApplicationBuilder ().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler (CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("weather", weather))
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(CommandHandler("addtask", addtask))
app.add_handler(CommandHandler("viewtask", viewtasks))
app.add_handler(CommandHandler("deletetask", deletetask))
print('Bot is runnig....')
app.run_polling()