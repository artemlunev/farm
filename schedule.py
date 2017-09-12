import pymysql
import time
import datetime
import config


def get(device):
    db = pymysql.connect(host = config.host_web,
                         port = config.port_web,
                         user = config.user_web,
                         password = config.password_web,
                         db = config.db_web,
                         cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor()
    sql = "SELECT * FROM `schedule` WHERE `device`=%s"
    cur.execute(sql, (device))
    schedule = {}
    schedule = cur.fetchall()
    db.close()
    return(schedule)

def add(interval, device):
    db = pymysql.connect(host = config.host_web,
                         port = config.port_web,
                         user = config.user_web,
                         password = config.password_web,
                         db = config.db_web,
                         cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor()
    
    now_date = datetime.date.today() #получение текущей даты
    now_time = datetime.datetime.now() #получение текущего времени
    time_from = datetime.time(now_time.hour, now_time.minute, now_time.second)
    time_to = datetime.time(now_time.hour + interval, now_time.minute, now_time.second)

    sql = "INSERT INTO `schedule` (`date`, `time_from`, `time_to`, `device`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (now_date, time_from, time_to, device))
    db.commit()
    db.close()
    print(time_to)



