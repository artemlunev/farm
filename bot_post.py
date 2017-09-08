import telebot
import config

bot = telebot.TeleBot(config.token)

def send_to_farm(text):
        bot.send_message(-186339805, text)
        print(text)
