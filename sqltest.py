import pymysql
import time
db = pymysql.connect(host='localhost', user='root', password='290173', db='farm')
cur = db.cursor()
datetimeWrite = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
sql = "INSERT INTO `testLog` (`datetime`, `status`) VALUES (%s, %s)"
cur.execute(sql, (datetimeWrite, '1'))

db.commit()

sql = "SELECT `datetime`, `status` FROM `testLog` WHERE `status`=%s"
cur.execute(sql, ('1'))
result = cur.fetchone()
print(result)
db.close()
