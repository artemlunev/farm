import pymysql
import time
from pyparsing import Word, alphas, nums
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
