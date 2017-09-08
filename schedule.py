import datetime
import pymysql
from time import localtime


db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
sql = "SELECT `id`, `time_start`, `time_end`, `device` FROM `schedule`"
cur = db.cursor()
schedule = list()
cur.execute(sql)
print(cur.id)
for id, time_start, time_end, device in cur:
    schedule.extend([[id, device, time_start.seconds, time_end.seconds]])
    print(schedule)
i = len(schedule)
print(i)
print(schedule.pop(1))


def getseconds():
    mytimefake = localtime()
    mytime = mytimefake.tm_seconds
    return int(mytime)



#schedule = cur.fetchone()
#i = len(schedule)/3
#print(schedule)
#print(i)


db.close()
