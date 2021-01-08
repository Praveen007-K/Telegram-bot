#pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler

#YOUR UNIQUE TOKEN from BotFather (Bot in telegram - Use commands /start, /newbot respectively)
updater = Updater(token='YOUR UNIQUE TOKEN',use_context=True)
dispatcher = updater.dispatcher

#Setting reply Hello World function
def hello(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text='Hello World')

#Connecting the function call to /hello command using handler and attaching handler to dispatcher
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

#Start running
updater.start_polling()


