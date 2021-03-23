from telebot import *
import telebot
from datetime import datetime
import emoji
import schedule
import time
from random import *

TOKEN = '1460604666:AAE0oASwac6RJzbReQ69iqd-UAP7LcRnczg'

bot = telebot.TeleBot(TOKEN)
key_words = ['start', 'help', 'about']
procents = [160, 240, 562, 416, 165]


@bot.message_handler(commands=['start', 'help'])
# Отправка приветственного сообщения / сбор id всех подключившихся
def send_welcome(message):
    check_file(file='users_id', id=message.chat.id)
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text=emoji.emojize(':rocket: ') + "Показать примеры", callback_data="example")
    markup.add(btn)
    bot.send_message(message.chat.id, "Yoooo! Wazup man?", reply_markup=markup)


@bot.message_handler(commands=['send_all'])
# Рассылка всем пользователям, чей id есть в файле
def send_all(message):
    user_id = str(message.chat.id)
    with open('users_id', 'r') as opened_file:
        for line in opened_file:
            bot.send_message(line, f'Сегодня выдано инсайдов на {message.text[9::]}% прибыли')
        bot.send_message(user_id, 'отправлено')


def notif_day(array):
    with open('users_id', 'r') as opened_file:
        for line in opened_file:
            bot.send_message(line, f'Сегодня выдано инсайдов на {random.choice(array)}% прибыли')


def logging(file, id, text):
    time = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    with open(f'{file}', 'a') as opened_file:
        opened_file.write(f'{time}: "{text}" from {id}\n')


def check_file(file, id):
    user_id = str(id)
    with open(f'{file}', 'r') as opened_file:
        if user_id in opened_file.read():
            pass
        else:
            write_in_file(file, user_id)


def write_in_file(file, id):
    f = open(f'{file}', 'a')
    f.write(id + '\n')
    f.close()


@bot.message_handler(commands=['example'])
# Отправка сообщения
def send_example(message):
    bot.send_message(message.chat.id, "Здесь будут примеры")


@bot.message_handler(content_types=['text'])
# Обработка невалидного текстового сообщения пользователя и перенаправление на /start
def repeat(message):
    logging('log', message.chat.id, message.text)
    bot.send_message(message.chat.id,
                     "Команда не поддерживается.\nДля начала работы введите '/start'.")


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'example':
        send_example(call.message)


if __name__ == '__main__':
    bot.polling()
