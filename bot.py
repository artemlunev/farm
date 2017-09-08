import telebot
import config
import sql_lightlog

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


bot.polling()
