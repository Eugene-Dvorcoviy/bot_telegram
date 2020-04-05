import telebot
import config
import random
import datetime

from DOLLAR import Dollar
from Hryvnia import Hryvnia

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
dollar_currency = Dollar()
hryvnia_currency = Hryvnia()


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, config.RULES)


@bot.message_handler(commands=['start'])
def welcome(message):
    #add begin picture
    sti = open('data/img/wolf_1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("ПРАВИЛА")

    markup_1.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, который не выступает в цирке.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup_1)


@bot.message_handler(commands=['currency'])
def currency(message):
    img_currency = open("data/img/money.webp", 'rb')
    bot.send_sticker(message.chat.id, img_currency)

    markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Dollars")
    item_2 = types.KeyboardButton("Hryvnia")

    markup_2.add(item_1, item_2)
    bot.send_message(message.chat.id, "Выбери любую валюту..", parse_mode='html', reply_markup=markup_2)

@bot.message_handler(commands=['time'])
def time(message):
    bot.send_message(message.chat.id, datetime.datetime.now().time())


@bot.message_handler(commands=['date'])
def date(message):
    bot.send_message(message.chat.id, datetime.datetime.now().date())


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == "ПРАВИЛА":
            bot.send_message(message.chat.id, config.RULES)
        elif message.text == "Dollars":
            bot.send_message(message.chat.id,
                             "Сейчас курс Доллара к Рублю: {}".format(dollar_currency.get_currency_price()))
        elif message.text == "Hryvnia":
            bot.send_message(message.chat.id,
                             "Сейчас курс Гривны к Рублю: {}".format(hryvnia_currency.get_currency_price()))
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
if __name__ == '__main__':
    bot.polling(none_stop=True)