from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)


@app.route("/")#打开登陆界面
def hello_world():
    return render_template("land.html")

@app.route("/register.html")#由登陆界面跳转到注册界面
def register():
    return render_template("register.html")


@app.route("/sign_in.html")#由注册界面将信息导入到数据库，注册成功并签到，piont=1
def open():
    username_new=request.args.get("username_new")
    password=request.args.get("password")
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO test(uid,password,piont) VALUES(%s,%s,%d)"%(username_new,password,1))
    conn.commit()
    conn.close()
    return ("签到成功"
            "piont=1")

@app.route("/sign_in_old.html")#由登陆界面登陆
def check():
    username=request.args.get("username")
    password=request.args.get("password")
    conn=sqlite3.connect('test.db')
    c=conn.cursor()
    c.execute("SELECT*FROM test where uid = %s"%username)
    rv=c.fetchall()
    conn.commit()
    conn.close()
    if len(rv)==0:#用户不存在
        return ("请先注册")
    elif rv[0][1]!=password:#密码与数据库中的不一样
        return ("密码错误")
    else:#成功登陆，并piont+1
        conn=sqlite3.connect('test.db')
        c=conn.cursor()
        c.execute("update test set piont=%d where uid=%s"%(rv[0][2]+1,username))
        conn.commit()
        conn.close()
        return ("签到成功"
                "piont=%d"%(rv[0][2]+1))
    
if __name__=="__main__":
    app.run()


