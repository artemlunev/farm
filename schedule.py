import pymysql
import time
from pyparsing import Word, alphas, nums
import config


def get():
    db = pymysql.connect(host = config.host_web,
                         port = config.port_web,
                         user = config.user_web,
                         password = config.password_web,
                         db = config.db_web,
                         cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor()
    sql = "SELECT * FROM `schedule`"
    cur.execute(sql)
    schedule = {}
    schedule = cur.fetchall()
    db.close()
    
    i = 0
    schedule_len = len(schedule)

    while i < schedule_len:
        print (schedule[i])
        i = i + 1
    
    

   
    print (schedule_len)
    time1 = schedule[0]
    
    print (time1['id'])


get()
