from flask import Flask,render_template,request,redirect,session,Blueprint
from member.member import member_bp
from error.error import error_bp
from task.task import task_bp

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="secret"
app.register_blueprint(member_bp)
app.register_blueprint(task_bp)
app.register_blueprint(error_bp)

@app.route("/")
def index():
    return render_template("index.html")



    
app.run(port=3000)
