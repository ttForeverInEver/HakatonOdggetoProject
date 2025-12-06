from http.client import responses

import telebot
import requests
from pyexpat.errors import messages

from telebot import types

bot = telebot.TeleBot('8412499515:AAG6YnFnNkSuieFmTmBAaedV72cTqxhUNkU')
managers = ['']
customers = ['6229491244']
menu = ["кот"]
flagUserAdding = False
UNSPLASH_ACCESS_KEY =''
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
    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        button2 = types.InlineKeyboardButton("Меню", callback_data='getMenu')
        markup.add(button2)
        bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def calback_inline (call):
    if call.data == 'addCustomer':
        bot.answer_callback_query(call.id, 'скиньте id сотрудника')
    if call.data == 'getMenu':
        theme = menu[0]


        img_url = get_unsplash_image_url(theme)

        bot.send_photo(call.message.chat.id, img_url, caption=f"Тема: {theme}")
        bot.answer_callback_query(call.id)


bot.polling()