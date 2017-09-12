## настройка ##

import time
import RPi.GPIO as GPIO
import sql_lightlog
from pyparsing import Word, alphas, nums
from time import localtime # берем localtime как основную функцию
import bot_post
import Adafruit_DHT
import schedule
import check

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #"включение" GPIO

light = 11
pump = 13

GPIO.setup(light, GPIO.OUT) # установка light порта как выхода
GPIO.setup(pump, GPIO.OUT) # установка pump порта как выхода
#GPIO.setup(test, GPIO.OUT)
#GPIO.output(test, 0)

light_status = 2
pump_status = 2

def lighton(): #включение света
    GPIO.output(light, 1) # on light
    text = "Light ON:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.light(1, 1)
    sql_lightlog.light_web(1, 1)
    bot_post.send_to_farm(text) # отправка в бот
    global light_status
    light_status = 1

def lightoff(): #выключение света
    GPIO.output(light, 0) # off light
    text = "Light OFF:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.light(0, 1)
    sql_lightlog.light_web(0, 1)
    bot_post.send_to_farm(text)
    global light_status
    light_status = 0

def pumpon():
    GPIO.output(pump, 1) # off pump
    text = "Pump ON:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.pump(1, 1)
    sql_lightlog.pump_web(1, 1)
    bot_post.send_to_farm(text)
    global pump_status
    pump_status = 1

def pumpoff():
    GPIO.output(pump, 0) # off light
    text = "Pump OFF:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.pump(0, 1)
    sql_lightlog.pump_web(0, 1)
    bot_post.send_to_farm(text)
    global pump_status
    pump_status = 0




def gethour(): #функция получения количества часов
    mytimefake = localtime()
    mytime = mytimefake.tm_hour
    return int(mytime)

def getminute(): #функция получения количества минут
    mytimefake = localtime()
    mytime = mytimefake.tm_min
    return int(mytime)


def main():#функция проверки времени и включения тампы по если ок
    lamp_check = check.checkinterval('lamp')
    pump_check = check.checkinterval('pump')
    
    if lamp_check == 1:
        if light_status == 0 or light_status == 2: #прверка, что лампа не включена
            lighton()
            pumpon()
    else:
        if light_status == 1 or light_status == 2:
            lightoff()
            pumpoff()


                
    if pump_check == 1:
        if pump_status == 0 or pump_status == 2: #прверка, что лампа не включена
            lighton()
            pumpon()
    else:
        if pump_status == 1 or pump_status == 2:
            lightoff()
            pumpoff()
             
while True:
    main()
    print(light_status)
    time.sleep(60) 

    

#включение функционала по запуску ночного скрипта:

#GPIO.cleanup()
