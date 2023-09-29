#测试数据库添加数据
import sqlite3
conn = sqlite3.connect('test.db')
password="123"
username_new="2345"
piont=0
c = conn.cursor()
c.execute("INSERT INTO test(uid,password,piont) VALUES(%s,%s,%d)"%(username_new,password,piont))
conn.commit()
conn.close()
