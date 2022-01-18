from flask import Flask,render_template,request,redirect,session
app=Flask(
    __name__,
    static_folder="templates",
    static_url_path="/"
)
app.secret_key="secret"

@app.route("/")
def index():
    return render_template("index.html")

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
