import telebot
import config
import sql_lightlog
device = 'string'
bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp="status")
def send_status(message):
        mess = sql_lightlog.get_pump_status_bot()
        bot.send_message(message.chat.id, mess)
        print(mess)

@bot.message_handler(regexp="temp")
def send_status(message):
        mess = sql_lightlog.get_dht_temp_bot()
        bot.send_message(message.chat.id, mess)
        print(mess)

@bot.message_handler(regexp="add")
def add(message):
    #Эти параметры для клавиатуры необязательны, просто для удобства
        keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_lamp = types.InlineKeyboardButton(text="Лампа", callback_data="lamp")
        button_pump = types.InlineKeyboardButton(text="Насос", callback_data="pump")
        button_all = types.InlineKeyboardButton(text="Всё", callback_data="all")
        keyboard.add(button_lamp, button_pump, button_all)
        bot.send_message(message.chat.id, "Что включить?", reply_markup=keyboard)



@bot.callback_query_handler(func=lambda c: True)
def inline(c):
        global device
        if c.data == 'lamp':
                device = 'lamp'
        if c.data == 'pump':
                device = 'pump'
        if c.data == 'all':
                device = 'all'
        keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=time, callback_data=time) for time in ['1', '2', '3', '4', '5']])
        bot.send_message(message.chat.id, "На какое время?", reply_markup=keyboard)



bot.polling()
