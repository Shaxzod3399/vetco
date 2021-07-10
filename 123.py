from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, commandhandler, dispatcher
def start(update, context):
    user = update.message.from_user
    update.message.reply_html('Assalomu alaykum <b>{}</b> Botimizga xush kelibsiz',
    format(user.first_name))
'''
    buttons = [
        [
        InlineKeyboardButton('Biz haqimizda', callback_data='shax'),
        InlineKeyboardButton('Filiallarimiz', callback_data='shox')
        ]
    ]'''
    
    def main():
        updater = Updater('1782094572:AAEvuFSk4RVtCod5qTz9fu3s0hzbxoo74ME',use_context= True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(commandhandler('start',start))
        updater.start_polling()
        updater.idle()