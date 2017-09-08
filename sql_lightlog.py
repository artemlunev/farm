import pymysql
import time
from time import localtime # берем localtime как основную функцию
from pyparsing import Word, alphas, nums
import config

#db_local = pymysql.connect(host='localhost', user='root', password='290173', db='farm')

#db_web = pymysql.connect(host='server179.hosting.reg.ru', port=3306, user='u0385355_default', password='ao!d3OHo', db='u0385355_farm')


def gettime(): #функция получения количества минут
    mytimefake = localtime()
    mytime = mytimefake.tm_min
    return mytime

def light(st, action):
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    mytime = gettime()
    
    sql = "INSERT INTO `lightLog` (`datetime`, `status`, `minute`, `action`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (datetimeWrite, st, mytime, action))
    db.commit()
    db.close()
    
def light_web(st, action):
    db = pymysql.connect(host='server179.hosting.reg.ru', port=3306, user='u0385355_default', password='ao!d3OHo', db='u0385355_farm')
    cur = db.cursor()
    
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    mytime = gettime()
    
    sql = "INSERT INTO `lightLog` (`datetime`, `status`, `minute`, `action`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (datetimeWrite, st, mytime, action))
    db.commit()
    db.close()

def dht(humidity, temp):
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    mytime = gettime()
    
    sql = "INSERT INTO `dht` (`datetime`, `humidity`, `temp`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (datetimeWrite, humidity, temp))
    db.commit()
    db.close()

    
def getstatus(): ## light
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    sql = "SELECT `id`, `status`, `minute` FROM `lightLog` ORDER BY `id` DESC LIMIT 1"
    cur.execute(sql)
    status = cur.fetchone()
    db.close()
    return status


def pump(st, action):
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    mytime = gettime()
    
    sql = "INSERT INTO `pump` (`datetime`, `status`, `minute`, `action`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (datetimeWrite, st, mytime, action))
    db.commit()
    db.close()
    
def pump_web(st, action):
    db = pymysql.connect(host='server179.hosting.reg.ru', port=3306, user='u0385355_default', password='ao!d3OHo', db='u0385355_farm')
    cur = db.cursor()
    
    datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    mytime = gettime()
    
    sql = "INSERT INTO `pump` (`datetime`, `status`, `minute`, `action`) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (datetimeWrite, st, mytime, action))
    db.commit()
    db.close()

def get_pump_status():
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    sql = "SELECT `id`, `status`, `minute` FROM `pump` ORDER BY `id` DESC LIMIT 1"
    cur.execute(sql)
    status = cur.fetchone()
    db.close()
    return status

def get_pump_status_bot():
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    sql = "SELECT `status` FROM `pump` ORDER BY `id` DESC LIMIT 1"
    cur.execute(sql)
    pump_status = str((cur.fetchone()))
    if pump_status == "(0,)":
        text = "OFF"
    elif pump_status == "(1,)":
        text = "ON"
    else: text = pump_status
    db.close()
    return text

def get_dht_temp_bot():
    db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
    cur = db.cursor()
    sql = "SELECT `temp` FROM `dht` ORDER BY `id` DESC LIMIT 1"
    cur.execute(sql)
    temp = str((cur.fetchone()))

    sql = "SELECT `humidity` FROM `dht` ORDER BY `id` DESC LIMIT 1"
    cur.execute(sql)
    humidity = str((cur.fetchone()))
    

    text = 'Temp = %s, humidity = %s' % (temp, humidity)
    return text
