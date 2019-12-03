from flask import Flask,render_template,request,redirect,session,url_for
from functools import wraps


app = Flask(__name__)
app.config.from_object("settings.Pro")
app.secret_key = "djasdjds"


@app.before_request
def auth():
    if request.path == "/login":
        return None
    if session.get("user"):
        return None
    return redirect('/login')


def login_requiry(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if not session.get("user"):
            return redirect(url_for('login'))

        ret = func(*args,**kwargs)
        return ret
    return inner


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user == "moke" and pwd == "123":
        session["user"] = user
        return redirect('/')
    return render_template('login.html',error="用户名或密码错误")


student_dict = {
    1:{"name":"root","age":1},
    2:{"name":"pooy","age":2},
    3:{"name":"fult","age":3},
}

@app.route('/')
# @login_requiry
def index():
    return render_template('index.html',stu_dic=student_dict)


@app.route('/delate/<int:id>')
# @login_requiry
def delate(id):
    del student_dict[id]
    return redirect(url_for('index'))


@app.route('/detail/<int:id>')
# @login_requiry
def detail(id):
    info = student_dict[id]
    return render_template('detail.html',info=info)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




if __name__ == '__main__':
    app.run()
