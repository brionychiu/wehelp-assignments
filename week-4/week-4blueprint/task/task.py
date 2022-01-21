from flask import Blueprint,render_template,request,session,redirect
#藍圖物件可看成一個縮小版的app物件
#flask框架自帶的模組Blueprint，Blueprint 是一個儲存操作方法的容器
#它相當於一個縮小版的app應用，但是一個Blueprint並不是一個完整的應用，它不能獨立於應用執行，而必須要註冊到某一個應用中。
#藍圖的作用：解耦，模組化開發(把路由切割成不同的模組檔案)
task_bp=Blueprint("task",__name__,template_folder="templates")
@task_bp.route("/signin",methods=["POST"])
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

@task_bp.route("/signout")
def signout():
    del session["account"]
    return redirect("/")