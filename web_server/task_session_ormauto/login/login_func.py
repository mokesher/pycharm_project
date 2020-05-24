from django.shortcuts import HttpResponse, render, redirect, HttpResponseRedirect
from login import models
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.forms import Form
from django.forms import fields


class LoginForm(Form):
    user = fields.CharField(
        max_length=16,
        min_length=2,
        required=True,
        error_messages={
            'required': "用户名不能为空",
            'min_length': "用户名至少8个字符",
            'max_length': "用户名过长",
        }
    )

    password = fields.CharField(
        max_length=16,
        required=True,
        error_messages={
            'required': "密码不能为空",
        }
    )

    box = fields.CharField(
        max_length=2,
        required=False,
    )


class RegisteForm(Form):
    user = fields.CharField(
        max_length=16,
        min_length=2,
        required=True,
        error_messages={
            'required': "用户名不能为空",
            'min_length': "用户名至少8个字符",
            'max_length': "用户名过长",
        }
    )

    password = fields.CharField(
        max_length=16,
        required=True,
        error_messages={
            'required': "密码不能为空",
        }
    )

    gender = fields.CharField(
        max_length=5,
        required=True,
    )

    confirm_password = fields.CharField(
        max_length=16,
        required=True,
        error_messages={
            'required': "密码不能为空",
        }
    )


@method_decorator(csrf_protect, name="dispatch")
class Login(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        obj = LoginForm(request.POST)
        if obj.is_valid():
            next_url = request.GET.get("next")
            user = obj.cleaned_data.get("user")
            pwd = obj.cleaned_data.get("password")
            user_obj = models.UserInfo.objects.filter(username=user).first()
            if user_obj:
                gender = user_obj.gender
                session_time = obj.cleaned_data.get('box')
                print(session_time)
                if gender == 1:
                    obj = models.UserInfo.objects.filter(gender=1, username=user, password=pwd).first()
                else:
                    obj = models.UserInfo.objects.filter(gender=2, username=user, password=pwd).first()

                if obj:
                    if session_time == "1":
                        request.session.set_expiry(20000)
                    if next_url:
                        rep = redirect(next_url)
                    else:
                        rep = redirect('/index/')
                    # ret.set_cookie('token',"djasdjds")
                    request.session['user_info'] = {'user': user, 'gender': gender}
                    return rep
                else:
                    error = "用户名或密码错误"
                    return render(request, "login.html", {"error": error})
        else:
            print(obj.errors)
            return render(request, "login.html", {"obj": obj})


@method_decorator(csrf_protect, name="dispatch")
class registe(View):

    def get(self, request):
        return render(request, "registe.html")

    def post(self, request):
        obj = RegisteForm(request.POST)
        if obj.is_valid():
            registe_user = obj.cleaned_data.get("user")
            registe_gender = obj.cleaned_data.get("gender")
            registe_pwd = obj.cleaned_data.get("password")
            confirm_pwd = obj.cleaned_data.get("confirm_password")
            print(registe_gender)
            if registe_pwd != confirm_pwd:
                error = "密码不一致"
                return render(request, "registe.html", {"error": error})

            if registe_gender == "man":
                gender = 1
                obj = models.UserInfo.objects.filter(gender=1, username=registe_user).first()
            else:
                gender = 2
                obj = models.UserInfo.objects.filter(gender=2, username=registe_user).first()
            if obj:
                error = "用户名已存在！"
                return render(request, "registe.html", {"error": error})
            else:
                models.UserInfo.objects.create(gender=gender, username=registe_user, password=registe_pwd)
            return redirect("/login/")

        else:
            return render(request, "registe.html", {"obj": obj})


def logout(request):
    print("logout")
    ret = HttpResponseRedirect('/index/')
    # ret.delete_cookie('token')
    # del request.session['is_login']
    request.session.clear()  # 超时时间清空
    return redirect("/login/")
