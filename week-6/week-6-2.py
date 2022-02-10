from mysql.connector import pooling
from flask import Flask,render_template,request,redirect,session

connection_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                  pool_size=5,
                                                  pool_reset_session=True,
                                                  host='localhost',
                                                  database='member_db',
                                                  user='root',
                                                  password='password123')

    # Get connection object from a pool

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
    name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    connection_object = connection_pool.get_connection()
    db_Info = connection_object.get_server_info()   
    cursor = connection_object.cursor()
    cursor.execute("SELECT `account` FROM `member_ship` WHERE `account`=%s;",[account])
    result=cursor.fetchone()
    if result!=None:
        return redirect("/error?msg=帳號已經被註冊")
    data = (account,password,name)
    insert = "INSERT INTO `member_ship` VALUES (%s, %s,%s);"
    cursor.execute(insert, data)
    connection_object.commit()
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
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
    connection_object = connection_pool.get_connection()
    db_Info = connection_object.get_server_info() 
    cursor = connection_object.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `member_ship` WHERE `account`=%s AND `password`=%s;",[account,password])
    result=cursor.fetchone()
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    session["account"]=result["account"]
    session["name"]=result["name"]
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
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

