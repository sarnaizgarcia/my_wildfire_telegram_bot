import telebot

bot = telebot.TeleBot('978325959:AAEbFC7LndG8iK8lwXwot0WiiSoJW_4sI0s')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Would you like to help me find wildfires?")


@bot.chosen_inline_handler(func=lambda message == 'Yes': True)
def test_chosen(message):
    # if message == 'Yes':
    bot.reply_to(message, 'Lets find them!!')
    # if message == 'No':
    #     bot.reply_to(message, 'Let them burn!!')


bot.polling()
