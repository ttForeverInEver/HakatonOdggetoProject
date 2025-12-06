import telebot
from telebot import types

bot = telebot.TeleBot('8412499515:AAG6YnFnNkSuieFmTmBAaedV72cTqxhUNkU')
managers = ['6229491244']
customers = ['6229491244']
menu = ["Котлетки с пюрешкой"]
flagUserAdding = False
if flagUserAdding:
    @bot.message_handler()
    def userAdding(message):
        customers.append(str(message.from_user.text))
        flagUserAdding = False


@bot.message_handler(commands=['start'])
def start(message):
    if str(message.from_user.id) not in managers and str(message.from_user.id) not in customers:
        bot.send_message(message.chat.id, 'Отказано в доступе')
    elif str(message.from_user.id) not in customers:
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("Добавить сотрудника", callback_data='addCustomer')
        markup.add(button1)
        bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def calback_inline (call):
    if call.data == 'addCustomer':
        bot.answer_callback_query(call.id, 'скиньте id сотрудника')
        flagUserAdding = True;

bot.polling()