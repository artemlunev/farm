import telebot
import config
import sql_lightlog
import schedule


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


@bot.message_handler(regexp="lamp 1")
def lamp_on(message):
        schedule.add(1, 'lamp')

@bot.message_handler(regexp="lamp 2")
def lamp_on(message):
        schedule.add(2, 'lamp')

@bot.message_handler(regexp="pump 1")
def lamp_on(message):
        schedule.add(1, 'pump')

@bot.message_handler(regexp="pump 2")
def lamp_on(message):
        schedule.add(2, 'pump')





bot.polling()
