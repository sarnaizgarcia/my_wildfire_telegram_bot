import pendulum

import telebot

from telebot import types
from repository.images_repo import images_repo

from credentials import key

bot = telebot.TeleBot(key)

# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py

LON = -120.70418
LAT = 38.32974
BEGIN = '2000-01-01, END'
END = pendulum.now('UTC').date().isoformat()


@bot.message_handler(commands=['start'])
def welcome(message):
    # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # markup.add('Yes', 'No')
    msg = bot.reply_to(
        message, 'Hi! Would you like to help me to find wildfires?')  # , reply_markup=markup)
    bot.register_next_step_handler(msg, find_fire)


@bot.message_handler(commands=['Yes', 'yes', 'Y', 'y'])
def find_fire(message):
    msg = bot.reply_to(message, 'Great!!')
    images = images_repo.create_images(LON, LAT, BEGIN, END)
    image = images_repo.request_image()
    msg = bot.reply_to(message, 'Do you see the fire?')


@bot.message_handler(commands=['Yes', 'yes', 'Y', 'y'])
def afirmative_answer(message):
    msg = images_repo.question_request('Y')


@bot.message_handler(commands=['No', 'no', 'N', 'n'])
def negative_answer(message):
    msg = images_repo.question_request('N')
    images = images_repo.create_images(LON, LAT, BEGIN, END)
    image = images_repo.request_image()


bot.polling()
