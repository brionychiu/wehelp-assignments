import mysql.connector
from flask import Flask,render_template,request,redirect,session
member_db = mysql.connector.connect(
host="localhost",
port="3306",
user="root",
password="password123",
database="member_db"
)
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="secret key can't revel"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    cursor = member_db.cursor()
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    cursor.execute("SELECT `account` FROM `member_ship` WHERE `account`=%s;",[account])
    result=cursor.fetchone()
    if result!=None:
        return redirect("/error?msg=帳號已經被註冊")
    data = (account,password,name)
    insert = "INSERT INTO `member_ship` VALUES (%s, %s,%s);"
    cursor.execute(insert, data)
    member_db.commit()
    cursor.close()
    return redirect("/")
  
@app.route("/signin",methods=["POST"])
def signin():
    cursor = member_db.cursor()
    account=request.form["account"]
    password=request.form["password"]
    cursor.execute("SELECT * FROM `member_ship` WHERE `account`=%s AND `password`=%s;",[account,password])
    result=cursor.fetchone()
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    session["account"]=result[0]
    session["name"]=result[2]
    cursor.close()
    return redirect("/member")

@app.route("/member")
def member():
    if "account" in session:
        name=session["name"]
        return render_template("member.html",name=name)  
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg","登入失敗")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")

app.run(port=3000)

