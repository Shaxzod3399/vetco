from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telebot import types
updater = Updater('1782094572:AAEvuFSk4RVtCod5qTz9fu3s0hzbxoo74ME')
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Man Shaxzodman assalomu alaykum {update.effective_user.first_name}')
updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.send_message(message.chat.id, 'Biz haqimizdagi ma`lumotli shu yerda olas?!')
updater.dispatcher.add_handler(CommandHandler('help', hello))
updater.start_polling()
updater.idle()