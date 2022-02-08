import mysql.connector
from flask import Flask,render_template,request,redirect,session
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
    member_db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="password123",
    database="member_db"
)
    cursor = member_db.cursor()
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    cursor.execute("SELECT `account` FROM `member_ship` WHERE `account`=%s;",[account])
    result=cursor.fetchone
    if result!=None:
        return redirect("/error?msg=帳號已經被註冊")
    data = (account,password,name)
    insert = "INSERT INTO `member_ship` VALUES (%s, %s,%s);"
    cursor.execute(insert, data)
    member_db.commit()
    if (member_db.is_connected()):
        cursor.close()
        member_db.close()
    return redirect("/")
    # for a_account in cursor:
    #     if a_account==account:
    #         return redirect("/error?msg=帳號已經被註冊")
    # with member_db.cursor() as cursor:
    #     cursor.execute("SELECT `account` FROM `member_ship`;")
    #     result=cursor.fetchall()
    #     for a in result:
    #         if a==account:
    #             return redirect("/error?msg=帳號已經被註冊")
  

@app.route("/signin",methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test" :
        session["account"]=account
        return redirect("/member")
    elif account.strip()==''or password.strip()=='':
        return redirect("/error?msg=請輸入帳號、密碼")
    elif account!="test" or password!="test":
        return redirect("/error?msg=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else :
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

