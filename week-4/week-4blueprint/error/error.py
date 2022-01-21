from flask import Blueprint,render_template,request,session,redirect

error_bp=Blueprint("error",__name__,template_folder="templates")
@error_bp.route("/error")
def error():
    message=request.args.get("msg","登入失敗")
    return render_template("error.html",message=message)