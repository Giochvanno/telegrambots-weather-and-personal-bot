import telebot
from telebot import types
import requests
import json



bot = telebot.TeleBot('6117746531:AAG3SdBt8QWH6GQWGXmTDY5enXinj_swKZ8')
API = '26f126549ecb33823f5c219140fe6b01'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! nice to meet you. Write name of country/city!')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Now weather: {temp}')

        image = 'coldy.png' if temp < 0 else 'sunny.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)

    else:
        bot.reply_to(message, 'Unknown country/city!')



bot.polling(non_stop=True)

