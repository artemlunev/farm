import pymysql
import time
from pyparsing import Word, alphas, nums
import config


def get():
    db = pymysql.connect(host='server179.hosting.reg.ru',
                         port=3306,
                         user='u0385355_default',
                         password='ao!d3OHo',
                         db='u0385355_farm',
                         cursorclass=pymysql.cursors.DictCursor)
    cur = db.cursor()
    sql = "SELECT * FROM `schedule`"
    cur.execute(sql)
    schedule = {}
    schedule = cur.fetchall()
    db.close()
    print.schedule[0]
    time1 = schedule[0]
    print (time1['id'])


get()
