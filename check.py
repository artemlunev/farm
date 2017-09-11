## настройка ##

import time
import datetime

from time import localtime # берем localtime как основную функцию

import schedule

ON = 1
OFF = 0


def checkinterval(device): #функция проверки времени
    timetable = schedule.get(device)
    now_date = datetime.date.today() #получение текущей даты
    now_time = datetime.datetime.now() #получение текущего времени
    
    
    for i in range(0, len(timetable)):
        time = timetable[i]

        if time['date'] == None: #регулярные событи
            time_from = datetime.datetime(now_date.year, now_date.month, now_date.day, 00, 00 , 00) + time['time_from']
            time_to = datetime.datetime(now_date.year, now_date.month, now_date.day, 00, 00 , 00) + time['time_to']
            

            if time_to > now_time and time_from <= now_time:
                return(ON)
            else:
                return(OFF)
                
        else:
            time_from = datetime.datetime(time['date'].year, time['date'].month, time['date'].day, 00, 00 , 00) + time['time_from']
            time_to = datetime.datetime(time['date'].year, time['date'].month, time['date'].day, 00, 00 , 00) + time['time_to']

            if time_to > now_time and time_from <= now_time:
                return(ON)
            else:
                return(OFF)


checkinterval('lamp')
        
    

#включение функционала по запуску ночного скрипта:

#GPIO.cleanup()
