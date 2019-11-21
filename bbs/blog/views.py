from django.shortcuts import render, redirect, HttpResponse
from blog import models
from functools import wraps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from blog.forms import LoginForm,SetpwdForm,RegForm,SetInfoForm
from django.http import JsonResponse
import time,requests,json,os
from django.db.models import F,Count
from django.conf import settings
from datetime import datetime
from bs4 import BeautifulSoup

# def check_login(func):
#     @wraps(func)
#     def inner(request, *args, **kwargs):
#         if request.session.get("is_login") == "1":
#             return func(request, *args, **kwargs)
#         else:
#             next_url = request.get_full_path()
#             return redirect(f"/login/?next={next_url}")
#     return inner


@login_required
# @check_login
def index(request):
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


def login(request):
    error_msg = ""

    if request.method == "GET":
        Form_obj = LoginForm()
        return render(request, "login.html", {"Form_obj": Form_obj})

    if request.method == "POST":
        Form_obj = LoginForm(request.POST)
        if Form_obj.is_valid():
            user = auth.authenticate(**Form_obj.cleaned_data)
            if user:
                auth.login(request, user)
                request.session["is_login"] = "1"
                return redirect('/index/')
            else:
                error_msg = "用户名或密码错误"
        return render(request,"login.html",{"error_msg": error_msg,"Form_obj": Form_obj})


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def register(request):

    if request.method == "GET":
        reg_obj = RegForm()
        return render(request, "register.html", {"reg_obj": reg_obj})
    else:
        ret = {"status": 0, "msg": ""}
        reg_obj = RegForm(request.POST, request.FILES)
        if reg_obj.is_valid():
            # file = reg_obj.cleaned_data["pic"]
            # with open(f"pics/{file.name}", "wb") as f:
            #     for chunk in file.chunks():
            #         f.write(chunk)
            models.UserInfo.objects.create_user(**reg_obj.cleaned_data)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            ret["status"] = 1
            ret["msg"] = reg_obj.errors
            return JsonResponse(ret)
            # return render(request, "register.html", {"reg_obj": reg_obj, "error_msg": error_msg})


def check_username(request):
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    if models.UserInfo.objects.filter(username=username):
        ret["status"] = 1
        ret["msg"] = "用户名已存在"
    return JsonResponse(ret)


# @check_login
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

        return render(request,"set_password.html", {"setpwd_obj": setpwd_obj, "error_msg": error_msg})

# @check_login
@login_required
def set_info(request):
    if request.method == "GET":
        SetInfo_obj = SetInfoForm()
        return render(request, "set_info.html", {"SetInfo_obj": SetInfo_obj})
    else:
        SetInfo_obj = SetInfoForm(request.POST)
        avatar_img = request.FILES.get("pic")
        if SetInfo_obj.is_valid():
            file_path = os.path.join(settings.MEDIA_ROOT, avatar_img.name)
            if os.path.exists(file_path):
                fix = datetime.now().strftime('%Y%m%d%H%M%S')
                file_path = os.path.join(settings.MEDIA_ROOT, fix + avatar_img.name)
            else:
                fix = ""
            with open(file_path, "wb") as f:
                for chunk in avatar_img.chunks():
                    f.write(chunk)

            models.UserInfo.objects.filter(username=request.user.username).update(**SetInfo_obj.cleaned_data, pic=(fix+avatar_img.name))
            return redirect("/index/")
        else:
            return render(request, "set_info.html", {"SetInfo_obj": SetInfo_obj})


def home(request,username):
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("404")
    else:
        blog = user.blog
        article_list = models.Article.objects.filter(user=user)

        return render(request, "blog/home.html", {
            "username": username,
            "blog": blog,
            "article_list": article_list,
        })


def article_detail(request, username, article_id):
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse(404)
    blog = user.blog
    article_obj = models.Article.objects.filter(pk=article_id).first()
    comment_obj = models.Comment.objects.filter(article_id=article_id)

    return render(request, "blog/article_detail.html", {
        "username": username,
        "article_obj": article_obj,
        "comment_obj": comment_obj,
        "blog": blog})


def up_down(request):
    is_up = json.loads(request.POST.get("is_up"))
    article_id = request.POST.get("article_id")
    user = request.user
    response = {"state": True}
    try:
        models.ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        if is_up:
            models.Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
        else:
            models.Article.objects.filter(pk=article_id).update(down_count=F("down_count")+1)
    except Exception as e:
        response["state"] = False
        response["fisrt_action"]=models.ArticleUpDown.objects.filter(user=user,article_id=article_id).first().is_up

    return  JsonResponse(response)


def comment(request):
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    pid = request.POST.get("pid")
    if not pid:
        comment_obj = models.Comment.objects.create(article_id=article_id,content=content,user_id=request.user.pk)
    else:
        comment_obj = models.Comment.objects.create(article_id=article_id, content=content, user_id=request.user.pk,parent_comment_id=pid)
    data= {}
    data["username"] = comment_obj.user.username
    data["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %H:%M")
    data["content"] = comment_obj.content
    data["parent_commen_id"] = comment_obj.parent_comment_id
    data["pk"] = comment_obj.pk

    return JsonResponse(data)


def del_comment(request,username,article_id,del_id):
    models.Comment.objects.filter(pk=del_id).delete()
    return redirect(f"/blog/{username}/article/{article_id}")


def change_comment(request, pk):
    pass


def comment_tree(request,article_id):
    comment_list = list(models.Comment.objects.filter(article_id=article_id).values("pk","content","parent_comment_id","user__username","create_time"))
    for comment in comment_list:
        comment["create_time"] = comment["create_time"].strftime("%Y-%m-%d %H:%M")

    print(comment_list)
    return JsonResponse(comment_list, safe=False)


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        article_content = request.POST.get("article_content")
        soup = BeautifulSoup(article_content,"html.parser")
        desc = soup.text+"..."
        for tag in soup.find_all():
            if tag.name in ["script", "link"]:
                tag.decompose()

        article_obj = models.Article.objects.create(title=title,user=request.user,desc=desc[0:150])
        models.ArticleDetail.objects.create(content=soup.prettify(),article=article_obj)

        return HttpResponse("ok")
    return render(request, "blog/add_article.html")



def upload(request):
    obj = request.FILES.get("upload_img")
    print("name", obj.name)
    path = os.path.join(settings.MEDIA_ROOT, "article_img", obj.name)
    with open(path, "wb") as f:
        for line in obj:
            f.write(line)
    res = {
        "error": 0,
        "url": "/media/article_img/" + obj.name
    }
    return HttpResponse(json.dumps(res))





