## настройка ##

import time
import RPi.GPIO as GPIO
import sql_lightlog
from pyparsing import Word, alphas, nums
from time import localtime # берем localtime как основную функцию
import bot_post
import datetime
import pymysql

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #"включение" GPIO

light = 11
pump = 13

GPIO.setup(light, GPIO.OUT) # установка light порта как выхода
GPIO.setup(pump, GPIO.OUT) # установка pump порта как выхода
#GPIO.setup(test, GPIO.OUT)
#GPIO.output(test, 0)

def lighton():
    GPIO.output(light, 1) # on light
    text = "Light ON:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.light(1, 1)
    bot_post.send_to_farm(text)

def lightoff():
    GPIO.output(light, 0) # off light
    text = "Light OFF:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.light(0, 1)
    bot_post.send_to_farm(text)

def pumpon():
    GPIO.output(pump, 1) # off pump
    pump_status = 1 # flag on
    text = "Pump ON:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.pump(1, 1)
    bot_post.send_to_farm(text)

def pumpoff():
    GPIO.output(pump, 0) # off light
    text = "Pump OFF:" + time.strftime("%d.%m.%Y %H:%M:%S")
    print(text)
    sql_lightlog.pump(0, 1)
    bot_post.send_to_farm(text)




def gethour(): #функция получения количества часов
    mytimefake = localtime()
    mytime = mytimefake.tm_hour
    return int(mytime)

def getminute():
    mytimefake = localtime()
    mytime = mytimefake.tm_min
    return int(mytime)

def getseconds():
    mytimefake = localtime()
    mytime = mytimefake.tm_sec
    return int(mytime)

def getlastmin_inserted():
    status = str(sql_lightlog.getstatus())
    if status == "None":
        return 100
    else:
        greet = '(' + Word(nums) + ',' + Word(nums) + ',' + Word(nums) + ')'
        fd = greet.parseString(status)
        return int(fd[5])

def getlaststatus_inserted():
    status = str(sql_lightlog.getstatus())
    if status == "None":
        return 3
    else:
        greet = '(' + Word(nums) + ',' + Word(nums) + ',' + Word(nums) + ')'
        fd = greet.parseString(status)
        return int(fd[3])



light_status = getlaststatus_inserted() # 0 выключено, 1 включено, 2 скрипт запустился не изменил, 3 пустая таблица
last_min_inserted = getlastmin_inserted()
cur_min = getminute()

dif_min = cur_min - last_min_inserted

if light_status == 3:
    stillworking = 0
else:
    if dif_min < 0 and dif_min > -56:
        stillworking = 0
    elif dif_min <= -56:
        stillworking = 1
    elif dif_min >= 0 and dif_min <= 2:
        stillworking = 1
    elif dif_min > 2:
        stillworking = 0




#включение функционала по запуску ночного скрипта:

db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
sql = "SELECT `time_start`, `time_end` FROM `schedule` WHERE `device` = 'light'"
cur = db.cursor()
cur.execute(sql)

def turn_light():#функция проверки времени и включения тампы по если ок
    for time_start, time_end in cur:
        if stillworking == 1:
            if getseconds() >= time_start.seconds and getseconds() < time_end.seconds:
                if light_status == 0:
                    lighton()
                    break
                elif light_status == 1:
                    sql_lightlog.light(1, 0)
            else:
                if light_status == 1:
                    lightoff()
                    
                else:
                    sql_lightlog.light(0, 0)
                
        elif stillworking == 0:
            if getseconds() >= time_start.seconds and getseconds() < time_end.seconds:
                lighton()
                break
            else:
                lightoff()

turn_light()

db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
sql = "SELECT `time_start`, `time_end` FROM `schedule` WHERE `device` = 'pump'"
cur = db.cursor()
cur.execute(sql)

def turn_pump():#функция проверки времени и включения тампы по если ок
    for time_start, time_end in cur:
        if stillworking == 1:
            if getseconds() >= time_start.seconds and getseconds() < time_end.seconds:
                if light_status == 0:
                    pumpon()
                    break
                elif light_status == 1:
                    sql_lightlog.light(1, 0)
            else:
                if light_status == 1:
                    pumpoff()
                    
                else:
                    sql_lightlog.light(0, 0)
                
        elif stillworking == 0:
            if getseconds() >= time_start.seconds and getseconds() < time_end.seconds:
                pumpon()
                break
            else:
                pumpoff()
turn_pump()
#GPIO.cleanup()
