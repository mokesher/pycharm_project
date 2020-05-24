from django.shortcuts import render, redirect, HttpResponse
from auth_login import models
from functools import wraps
from django.forms import Form, fields, widgets
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.session.get("is_login") == "1":
            return func(request, *args, **kwargs)
        else:
            next_url = request.get_full_path()
            return redirect(f"/login/?next={next_url}")

    return inner


class LoginForm(Form):
    username = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=widgets.TextInput(),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }

    )

    password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=widgets.TextInput(),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )


class SetpwdForm(Form):
    new_password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=widgets.TextInput(),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )
    old_password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=widgets.TextInput(),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )
    repeat_password = fields.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=widgets.TextInput(),
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短2位"
        }
    )


# @login_required
@check_login
def index(request):
    return render(request, "index.html")


def login(request):
    error_msg = ""

    if request.method == "GET":
        Form_obj = LoginForm()
        return render(request, "login.html", {"Form_obj": Form_obj})

    if request.method == "POST":
        Form_obj = LoginForm(request.POST)
        if Form_obj.is_valid():
            username = Form_obj.cleaned_data.get("username")
            password = Form_obj.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            print(username, password)
            if user:
                auth.login(request, user)
                request.session["is_login"] = "1"
                return redirect('/index/')
            else:
                error_msg = "用户名或密码错误"
        return render(request, "login.html", {"error_msg": error_msg, "Form_obj": Form_obj})


def logout(request):
    auth.logout(request)

    return redirect('/login/')


def regeist(request):
    if request.method == "GET":
        reg_obj = LoginForm()
        return render(request, "regeist.html", {"reg_obj": reg_obj})

    else:
        reg_obj = LoginForm(request.POST)
        if reg_obj.is_valid():
            reg_name = reg_obj.cleaned_data.get("username")
            reg_pwd = reg_obj.cleaned_data.get("password")
            user = User.objects.create_user(username=reg_name, password=reg_pwd, email="")
            if user:
                return redirect("/login/")

        error_msg = "错误发生"
        return render(request, "regeist.html", {"reg_obj": reg_obj, "error_msg": error_msg})


@check_login
def change_pwd(request):
    if request.method == "GET":
        setpwd_obj = SetpwdForm()
        return render(request, "set_password.html", {"setpwd_obj": setpwd_obj})

    if request.method == "POST":
        error_msg = ""
        user = request.user
        setpwd_obj = SetpwdForm(request.POST)
        if setpwd_obj.is_valid():
            old_password = setpwd_obj.cleaned_data.get("old_password")
            new_password = setpwd_obj.cleaned_data.get("new_password")
            repeat_password = setpwd_obj.cleaned_data.get("repeat_password")
            if user.check_password(old_password):
                if new_password != repeat_password:
                    error_msg = "密码不一致"
                elif new_password == old_password:
                    error_msg = "新密码不能和旧密码重复"
                else:
                    user.set_password(repeat_password)
                    user.save()
                    return redirect("/login/")

        return render(request, "set_password.html", {"setpwd_obj": setpwd_obj, "error_msg": error_msg})


def upload(request):
    if request.method == "GET":
        return render(request, "upload.html")
    if request.method == "POST":
        filename = request.FILES.get("file").name
        with open(f"files/{filename}", "wb") as f:
            for chunk in request.FILES["file"].chunks():
                f.write(chunk)

        return HttpResponse("ok")
