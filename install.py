# -*- coding: utf-8 -*- 
import telebot
from telebot import types
import time
import requests
from telebot.types import ReplyKeyboardMarkup , KeyboardButton
import os , sys
#Token joyi
Token = '1830581380:AAFNuWkeivgNHaGu4nAFa31y0yB6j5kmVvM'
bot = telebot.TeleBot(Token)

#Asosiy buttonlar
def asosiy():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        KeyboardButton(text="✅ Biz haqimizda"),
        KeyboardButton(text="🌐 Hamkorlarimiz"),
        KeyboardButton(text="♻️ Filiallarimiz"),
        KeyboardButton(text="📒 Katalog"),
        KeyboardButton(text="📌 Manzil"),
        KeyboardButton(text="📲 Murojaat uchun"),
        KeyboardButton(text="⬅️ Orqaga")
    ])
    return reply_markup
#hamkorlarimiz
def handlePartners():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        KeyboardButton(text="🏢 Biomin"),
        KeyboardButton(text="🏢 MasterRind"),
        KeyboardButton(text="🏢 Nita-Farm"),
        KeyboardButton(text="🏢 BrovaFarma"),
        KeyboardButton(text="🏢 Kanters"),
        KeyboardButton(text="🏢 Seva"),
        KeyboardButton(text="⬅️ Orqaga")
    ])
    return reply_markup
#katalog butons
def handlershox():
    reply_markup = ReplyKeyboardMarkup(row_width = 2 , resize_keyboard= True)
    reply_markup.add(*[
        KeyboardButton(text="📒 Biomin"),
        KeyboardButton(text="📒 MasterRind"),
        KeyboardButton(text="📒 Nita-Farm"),
        KeyboardButton(text="📒 BrovaFarma"),
        KeyboardButton(text="📒 Kanters"),
        KeyboardButton(text="📒 Seva"),
        KeyboardButton(text="⬅️ Orqaga")
    ])
    return reply_markup
#Filiallarimiz 
def handPartners1():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        KeyboardButton(text="🏢 Samarqand"),
        KeyboardButton(text="🏢 Farg`ona"),
        KeyboardButton(text="⬅️ Orqaga")
    ])
    return reply_markup
#start knopkasi 
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.from_user.id , "Assalomu alaykum \n *Sizni o`zimizning kompaniyamizni rasmiy botiga xush kelibsiz!*", reply_markup = asosiy())
#asosit()davomi
@bot.message_handler(content_types= ['text'])
def get_text(message):
    print(message.text)
    if message.text == "✅ Biz haqimizda":
        bot.send_message(message.chat.id,"Vetco Biotec Ltd. \n «VETKO BIOTEK» MCHJ «Ветко Биотек» маьсуляти чекланган жамияти 2020 йил ташкил топган. Жамиятнинг асосий фаолият турларидан бири, чорвачилик ва паррандачиликда ишлатиладиган ветеринария препаратларининг улгуржи савдоси билан шуғилланиш хисобланади. Хозирда жамият, Россиянинг «Нита фарм», Украинанинг «Бровафарма» ва «Укрзооветпромпостач», Нидерландиянинг «Kanters» компанияларининг 100 дан ортиқ препаратларини, хамкорликдаги ветеринария аптекаларига ва фермаларга етказиб беради. Жамият нафақат, дори препаратлар савдоси билан шуғулланади, балки чорвачиликда сифатли озуқа тайёрлашда, силос ва сенаж учун ишлатиладиган биологик консервантлар савдоси ва уларни ишлатишда, Австриянинг «BIOMIN» компанияси билан хамкорликда ишлайди. Юқори малакали мутахассисларимаз, силос ва сенаж тайёрлаш жараёни бўйича маслаҳатлар беради. Бундан ташқари, Биомин компанияси билан бузоқлар учун “Сутстабил” номи билан бузоқлар учун табиий сутни нордонлаштирувчи ишлаб чиқаради. Германиянинг “Мастерринд” компанияси билан ҳамкорликда, наслчилик ва селекция ишларида Республикамиз фермаларида бевосита иштирок этмоқда ва четдан келтирилган наслли буқалар уруғларини фермаларга таклиф этиб, фермалар учун бириктирилган буқаларни танлаб беради.  Жамият Франциянинг «CEVA» компанияси билан ҳамкорликда,  гормонал препаратлар савдоси билан ҳам шуғулланади. Шулар жумласидан, Оврален, Энзапрост ва Прид дельта хозирда сотувда мавжуд ва уларнинг қўлланилиши бўйича маслахатлар беради. Сутчилик ва гўшт ишлаб чиқаришга ихтисослашган қорамолчилик фермалари учун оптимиллаштирилган рационлар тузиб бериш, “Корм оптима” дастури асосида ҳар бир ферма ва гуруҳ учун алоҳида тузиб беради. Қўшимча макро ва микроэлементлар, ҳамда витаминларга талабни қоплаш учун “Агропремикс” МЧЖ билан ҳамкорликда, “Рономикс” номи билан соғин сигирлар ва тиним даври учун премиксларни таклиф этади.  Чорвачилик фермаларида ветеринария даволаш ва профилактика тадбирларини ташкил этиш бўйича амалий ва маслахат бўйича ёрдам беради. Чорвачиликда консалтинг хизматлари Украиналик ва Республикамизнинг юқори малакали мутахасислар томонидан бериб борилади. Юқори частотали УТА (ультратовуш аппарати) аппарати билан мутахассисларимиз сигир ва ғуножинларнинг буғозлиги Юуқори частотали УЗД аппаратлари билан сигир ва ғуножинларни қочирилгандан 32 кундан кейин буғозлликка текшириш. Мутахассисларимиз қисир сигирлар ва ғуножинларнинг тухумдонлари ва бачадонлари холатини аниқлаб беради.")
    elif message.text == "🌐 Hamkorlarimiz":
        bot.send_message(message.chat.id, "Bizning hamkorlarimiz ", reply_markup = handlePartners())
    elif message.text == "♻️ Filiallarimiz":
        bot.send_message(message.chat.id, "Filillarimiz", reply_markup = handPartners1())
    elif message.text == "⬅️ Orqaga":
        bot.send_message(message.chat.id, "Assalomu alaykum \n **Sizni o`zimizning kompaniyamizni rasmiy botiga xush kelibsiz!**", reply_markup =asosiy()  )
    elif message.text == "🏢 Samarqand":
        bot.send_message(message.chat.id, "Самарқанд вилояти филиаллимиз боғланиш учун маълумотлар:\nДиректор: Абдурахмонов Алибек | \n+998 (99) 444-29-41 \n Менежер: Каримов Жафарали |\n +998 (99) 444-68-44 \n Манзил: Самарканд вилояти Гагарин 85а уй\n Оринтер: Самарканд вилояти СОЛИҚ ёнида", reply_markup = handPartners1())
    elif message.text == "🏢 Farg`ona":
        bot.send_message(message.chat.id, "Фарғона вилояти филиаллимиз боғланиш учун маълумотлар:\nДиректор: Юсупов Бехзоджон Одилович | \nТел: +998 (99) 444-29-42\n         +998 (99) 917-91-00 \n Манзил: Фарғона шахар Юксалиш кўчаси 85 уй\n Оринтер: Экстренный больницани олдида", reply_markup = handPartners1())
    elif message.text == "📒 Katalog":
        bot.send_message(message.chat.id, "Bizning hamkorlarimznig kataloglarini tanlang:\n👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻", reply_markup = handlershox())
print("polling")
bot.polling(none_stop =False, interval = 0)

    