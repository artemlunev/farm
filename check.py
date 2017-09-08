## настройка ##

import time
import datetime

from time import localtime # берем localtime как основную функцию

import schedule


def checkinterval(): #функция проверки времени
    timetable = schedule.get('lamp')
    now_time = datetime.datetime.now()
    now_date = datetime.date.today()
    print(now_date)
    for i in range(0, len(timetable)):
        time = timetable[i]
        print(time['time_from'] + now_time)
        if time['time_from'] < datetime.datetime.now():
            print(0)
        else:
            print(1)

checkinterval()
        
    

#включение функционала по запуску ночного скрипта:

#GPIO.cleanup()
