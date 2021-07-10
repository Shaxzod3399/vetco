from telebot
from configure
from telebot import types
client = telebot.Telebot(configure.config['1830581380:AAFNuWkeivgNHaGu4nAFa31y0yB6j5kmVvM'])
#inlinKeyboardMarkup
@client.message_handler(commands = ['start'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(text = 'Biz haqimizda', callback_data = 'shax')
    item1 = types.InlineKeyboardButton(text = 'Biz haqimizda2', callback_data = 'shox')
    markup_inline.add(item,item1)
    client.send_message(message.chat.id, 'Biz haqimizdagi ma`lumotli shu yerda olas?!', 
        reply_markup = markup_inline )
@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'shax':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        Bizhaqimizda = types.KeyboardButton('Biz haqimizda')
        Filiallarimiz = types.KeyboardButton('Filiallarimiz')
        Kataloglar = types.KeyboardButton('Kataloglar')
        Hamkorlarimiz = types.KeyboardButton('Hamkorlarimiz')
        Murojaat_uchun = types.KeyboardButton('Murojaat uchun')
        Adressimiz = types.KeyboardButton('Adressimiz')
        Bosh_menyu = types.KeyboardButton('Bosh menyu')
        markup_reply.add(Bizhaqimizda,Filiallarimiz,Kataloglar,Hamkorlarimiz,Murojaat_uchun,Adressimiz,Bosh_menyu)
        client.send_message(call.message.chat.id, reply_markup = markup_reply)
    elif call.data == 'shox':
        pass
client.polling(none_stop = True , interval = 0)