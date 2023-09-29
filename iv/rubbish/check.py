#测试数据库查找数据
import sqlite3
username="2345"
password="123"
conn =sqlite3.connect('test.db')
c = conn.cursor()
c.execute("SELECT*FROM test where uid = %s"%username)
rv=c.fetchall()
conn.commit()
conn.close()