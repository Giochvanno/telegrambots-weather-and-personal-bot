import telebot
import webbrowser
from telebot import types
import sqlite3


bot = telebot.TeleBot('7181289804:AAFzJiqx8dwK1HP4KKY61jBJs3PJ6aPs8EA')
name = None





@bot.message_handler(commands=['start'])
def userinf(message):
    conn = sqlite3.connect('idream.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()


    markup = types.ReplyKeyboardMarkup()
    btn1_1 = types.KeyboardButton('Привет😎')
    markup.row(btn1_1)
    btn1_2 = types.KeyboardButton('О себе🤩')
    btn1_3 = types.KeyboardButton('ID⚙️')
    file = open('./aksh.jfif', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    markup.row(btn1_2, btn1_3)
    bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name}! Мы тебя еще раз зарегистрируем, введи свой никнейм</b>', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    conn = sqlite3.connect('idream.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users(name) VALUES ('%s')" % (name))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Вы зарегистрованы!')
    


def on_click(message):
    if message.text.lower() == 'привет😎':
        bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name}</b>', parse_mode='html')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'о себе🤩':
        bot.reply_to(message, f'Меня зовут iDream TeleBot! я являюсь основыным ботом гидом Армана(IDream)')   


@bot.message_handler(commands=['help'])
def helpinf(message):
    bot.send_message(message.chat.id, '<b>Help information ↓</b>', parse_mode='html')
    bot.send_message(message.chat.id, '<b>Введите /more для подробности</b>', parse_mode='html')

@bot.message_handler(commands=['more'])
def moreinf(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('TikTok', url="https://www.tiktok.com/@idream.awarden"))
    markup.add(types.InlineKeyboardButton('YouTube', url="https://www.youtube.com/channel/UCzG2G6HU7GM7RPjqJbsvLmQ"))
    bot.send_message(message.chat.id, '<b>More information ↓</b>', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['roomtub'])
def userinf(message):
    bot.send_message(message.chat.id, f'<b>YouTube: imper0rEYEE(https://www.youtube.com/channel/UCzG2G6HU7GM7RPjqJbsvLmQ) </b>', parse_mode='html')


@bot.message_handler(commands=['roomtok'])
def userinf(message):
    bot.send_message(message.chat.id, f'<b>YouTube: idream.awarden(https://www.tiktok.com/@idream.awarden) </b>', parse_mode='html')


@bot.message_handler(commands='musicp')
def call(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Изменить песню', callback_data='edit')
    btn2 = types.InlineKeyboardButton('Скипнуть', callback_data='skip')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Хмююю песня', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data =='skip':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# ----------------------------------------------------------------------------
    
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Вот это фото!')


@bot.message_handler(content_types=['audio'])
def get_photo(message):
    bot.reply_to(message, 'Вот это аудио!')


@bot.message_handler(content_types=['video'])
def get_photo(message):
    bot.reply_to(message, 'Вот это видео!')

# -----------------------------------------------------------------------------



@bot.message_handler()
def textinf(message):
    if message.text.lower() == 'привет😎' or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name}</b>', parse_mode='html')
    elif message.text.lower() == 'id' or message.text.lower() == 'id⚙️':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'о себе🤩' or message.text.lower() == 'о себе':
        bot.reply_to(message, f'Меня зовут iDream TeleBot! я являюсь основыным ботом гидом Армана(IDream)')


bot.polling(none_stop=True)