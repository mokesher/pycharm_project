from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from blog.forms import LoginForm, SetpwdForm, RegisterForm, SetInfoForm
from blog import models
from django.http import JsonResponse
from django.views.generic import FormView
from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME


# def check_login(func):
#     @wraps(func)
#     def inner(request, *args, **kwargs):
#         if request.session.get("is_login") == "1":
#             return func(request, *args, **kwargs)
#         else:
#             next_url = request.get_full_path()
#             return redirect(f"/login/?next={next_url}")
#     return inner


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        form = LoginForm(data=self.request.POST, request=self.request)

        if form.is_valid():
            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return self.render_to_response({
                'form': form
            })


def logout(request):
    auth.logout(request)
    return redirect('/login/')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "register.html"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return self.render_to_response({
                'form': form
            })


def check_username(request):
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    if models.UserInfo.objects.filter(username=username):
        ret["status"] = 1
        ret["msg"] = "用户名已存在"
    return JsonResponse(ret)


@login_required
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
            if not user.check_password(old_password):
                error_msg = "旧密码错误"
            else:
                if new_password != repeat_password:
                    error_msg = "密码不一致"
                elif new_password == old_password:
                    error_msg = "新密码不能和旧密码重复"
                else:
                    user.set_password(repeat_password)
                    user.save()
                    return redirect("/login/")

        return render(request, "set_password.html", {"setpwd_obj": setpwd_obj, "error_msg": error_msg})


@login_required
def set_info(request):
    edit_obj = models.UserInfo.objects.filter(username=request.user.username).first()
    SetInfo_obj = SetInfoForm(instance=edit_obj)
    if request.method == "POST":
        SetInfo_obj = SetInfoForm(request.POST, request.FILES, instance=edit_obj)
        # avatar_img = request.FILES.get("pic")
        if SetInfo_obj.is_valid():
            SetInfo_obj.save()
            # file_path = os.path.join(settings.MEDIA_ROOT, avatar_img.name)
            # if os.path.exists(file_path):
            #     fix = datetime.now().strftime('%Y%m%d%H%M%S')
            #     file_path = os.path.join(settings.MEDIA_ROOT, fix + avatar_img.name)
            # else:
            #     fix = ""
            # with open(file_path, "wb") as f:
            #     for chunk in avatar_img.chunks():
            #         f.write(chunk)
            #
            # models.UserInfo.objects.filter(username=request.user.username).update(**SetInfo_obj.cleaned_data, pic=(fix+avatar_img.name))
            return redirect("/index/")

    return render(request, "set_info.html", {"SetInfo_obj": SetInfo_obj})
