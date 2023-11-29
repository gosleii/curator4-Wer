import telebot

bot = telebot.TeleBot('6375210050:AAFiUTvyudiMG8E7J2_CXp9s5vHfd8bMXQ0')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здраствуй,если хочешь посмотреть самого лучшего ютубера,пиши /links',
                     parse_mode='Markdown')

@bot.message_handler(commands=['links'])
def main(message):
    bot.send_message(message.chat.id, 'Это канал MrBeast(http://www.youtube.com/@MrBeast)', parse_mode='Markdown')


bot.infinity_polling()