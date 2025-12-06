import telebot

bot = telebot.TeleBot('8412499515:AAG6YnFnNkSuieFmTmBAaedV72cTqxhUNkU')
managers = []
customers = [6229491244]
@bot.message_handler()

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in managers and message.from_user.id not in customers:
        bot.send_message(message.chat.id, 'Отказано в доступе')
    elif message.from_user.id not in managers:
        bot.send_message(message.chat.id, 'Здравствуйте')

bot.polling(none_stop=True)