#创建新的数据库

import sqlite3
conn = sqlite3.connect('test.db')
print ("数据库打开成功")
c = conn.cursor()
c.execute('''create table test(uid text,password text,piont integer)''')
print ("数据表创建成功")
conn.commit()
conn.close()
