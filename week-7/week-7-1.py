from mysql.connector import pooling
from flask import Flask,render_template,request,redirect,session
from flask import jsonify


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
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    connection_object = connection_pool.get_connection()
    #db_Info = connection_object.get_server_info() 此方法以字符串形式逐字返回 MySQL 服務器信息  
    #This method returns the MySQL server information verbatim as a string, for example '5.6.11-log', or None when not connected.
    cursor = connection_object.cursor()
    cursor.execute("SELECT `username` FROM `members` WHERE `username`=%s;",[username])
    result=cursor.fetchone()
    if result!=None:
        return redirect("/error?msg=帳號已經被註冊")
    data = (name,username,password)
    insert = "INSERT INTO `members` (`name`,`username`,`password`) VALUES (%s, %s,%s);"
    cursor.execute(insert, data)
    connection_object.commit()
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
    return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    connection_object = connection_pool.get_connection()
    #db_Info = connection_object.get_server_info() 
    cursor = connection_object.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `members` WHERE `username`=%s AND `password`=%s;",[username,password])
    result=cursor.fetchone()
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    session["username"]=result["username"]
    session["name"]=result["name"]
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
    return redirect("/member")

@app.route("/member")
def member():
    if "username" in session:
        name=session["name"]
        return render_template("member.html",name=name)  
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg","登入失敗")
    return render_template("error.html",message=message)

@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


@app.route("/api/members")
def api_members():
    member_username=request.args.get("username"," ")
    connection_object = connection_pool.get_connection()
    #db_Info = connection_object.get_server_info() 
    cursor = connection_object.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `members` WHERE `username`=%s" ,[member_username])
    result=cursor.fetchone()
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
    if result==None:
        return jsonify({
            "data":None
        })
    else:
        return jsonify({
            "data":{
                "id":result["id"],
                "name":result["name"],
                "username":result["username"]
            }
        })

@app.route("/api/member",methods=["POST"])
def api_member():    
    if "username"  not in session:
        return  jsonify ({"error":True})
    username=session["username"]
    new_name=request.json["name"]
    connection_object = connection_pool.get_connection()
    #db_Info = connection_object.get_server_info()   
    cursor = connection_object.cursor(dictionary=True)
    cursor.execute("UPDATE `members` SET `name`= %s  WHERE `username`=%s;",[new_name,username])
    connection_object.commit()
    session["name"]=new_name
    if connection_object.is_connected():
        cursor.close()
        connection_object.close()
    return  jsonify ({"OK":True})
app.run(port=3000)

