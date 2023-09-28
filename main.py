from telegram import *
import Constants as keys
from telegram.ext import *
import Responses as R
updater = Updater(token="5643520143:AAFCPxpSs9-yT9QIvntO4a7qeIFkj89qr8g")
dispatcher = updater.dispatcher
print("Bot started....")
def startCommand(update: Update, context: CallbackContext):
update.message.reply_text('Welcome to CareHealth :) \nWe hope you are doing good and prioritizing health over everything. Please let us know how we can help you? 😇. Enter "Help" to continue further')


dispatcher.add_handler(CommandHandler("start", startCommand))

#
# def start_command(update, context):

def help_command(update, context):
    update.message.reply_text('If you need help! you should ask for it on Google!')

def handle_message(update, context):
   text=str(update.message.text).lower()
   response= R.sample_responses(text)

   update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling(2)
    updater.idle()
main()
updater.start_polling(0)
