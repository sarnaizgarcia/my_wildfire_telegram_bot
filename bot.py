import telebot
from telebot import types

bot = telebot.TeleBot('978325959:AAEbFC7LndG8iK8lwXwot0WiiSoJW_4sI0s')

# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py


class User:
    def __init__(self):
        self.id = id
        self.answer = None


user = User()


@bot.message_handler(commands=['start'])
def welcome(message):
    # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # markup.add('Yes', 'No')
    msg = bot.reply_to(
        message, 'Hi! Would you like to help me to find wildfires?')  # , reply_markup=markup)
    print('-----------------------------1', msg)

    bot.register_next_step_handler(msg, get_coords)


def get_coords(message):
    if (message.text == 'Yes'):
        msg = bot.reply_to(message, 'Great!!')
    else:
        msg = bot.reply_to(message, 'Buhhhhh!!')
        print('-----------------------------2', msg)


bot.polling()
