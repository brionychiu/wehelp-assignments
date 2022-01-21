from flask import Blueprint,render_template,request,session,redirect

member_bp=Blueprint("member",__name__,template_folder="templates")
@member_bp.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else :
        return redirect("/")