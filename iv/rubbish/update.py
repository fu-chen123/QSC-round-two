#测试数据库上传数据
import sqlite3
username="2345"
conn=sqlite3.connect('test.db')
c=conn.cursor()
c.execute("SELECT*FROM test where uid = %s"%username)
rv=c.fetchall()
conn.commit()
conn.close()
print(rv)