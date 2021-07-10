import telebot
from telebot import types
import time
Token = '1810937242:AAHOn94btHhZ4z3oJ41THU9HSPqflSmQZzg'
bot = telebot.TeleBot(Token)
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message , "Assalomu alaykumpip")
print(dir(telebot))
bot.polling()
        