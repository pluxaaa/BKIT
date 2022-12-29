import time
import telebot
from telebot import types
import pytz
import datetime
from datetime import datetime


TOKEN = '5817249581:AAHSyo0jBKAW1_NHdmsfXFh0XjcMLluBGZ8'
bot = telebot.TeleBot(TOKEN)

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%m/%d/%y %H:%M:%S")
datetimeNY = datetime.strptime(currentTimeInNewYork, "%m/%d/%y %H:%M:%S")

moscowTz = pytz.timezone("Europe/Moscow") 
timeInMoscow = datetime.now(moscowTz)
currentTimeInMoscow = timeInMoscow.strftime("%m/%d/%y %H:%M:%S")
datetimeMSC = datetime.strptime(currentTimeInMoscow, "%m/%d/%y %H:%M:%S")

tokyoTz = pytz.timezone("Asia/Tokyo") 
timeInTokyo = datetime.now(tokyoTz)
currentTimeInTokyo = timeInTokyo.strftime("%m/%d/%y %H:%M:%S")
datetimeTK = datetime.strptime(currentTimeInTokyo, "%m/%d/%y %H:%M:%S")

LOCAL = datetime.strptime(datetime.now().strftime("%m/%d/%y %H:%M:%S"), "%m/%d/%y %H:%M:%S")


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Нью-Йорк")
    item2=types.KeyboardButton("Москва")
    item3=types.KeyboardButton("Токио")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, 'Выберите город:', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Нью-Йорк':
        bot.send_message(message.chat.id, 'Время в Нью-Йорке: ' + currentTimeInNewYork)
        bot.send_message(message.chat.id, 'Разница с локальным: ' +
                         (str(abs((LOCAL - datetimeNY).total_seconds()/3600)) + " ч"))

    elif message.text.strip() == 'Москва':
        bot.send_message(message.chat.id, 'Время в Москве: ' + currentTimeInMoscow)
        bot.send_message(message.chat.id, 'Разница с локальным: ' +
                         (str(abs((LOCAL - datetimeMSC).total_seconds()/3600)) + " ч"))

    elif message.text.strip() == 'Токио':
        bot.send_message(message.chat.id, 'Время в Токио: ' + currentTimeInTokyo)
        bot.send_message(message.chat.id, 'Разница с локальным: ' +
                         (str(abs((LOCAL - datetimeTK).total_seconds()/3600)) + " ч"))
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')

bot.infinity_polling()