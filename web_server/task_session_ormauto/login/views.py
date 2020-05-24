from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from login import models
from functools import wraps


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # if request.COOKIES.get("token"):
        if request.session.get('user_info'):
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            print(next_url)
            return redirect(f"/login/?next={next_url}")

    return inner


@check_login
def index(request):
    sessionid = request.session.get('user_info')
    gender = sessionid.get('gender')
    user = sessionid.get('user')
    if gender == 1:
        user_list = models.UserInfo.objects.filter(gender=1)
        relation_list = user_list.filter(username=user).first().m.values("id", "username")
    else:
        user_list = models.UserInfo.objects.filter(gender=2)
        obj = user_list.filter(username=user).first()
        if obj:
            relation_list = obj.userinfo_set.values("id", "username")
        else:
            relation_list = {}
    return render(request, "index.html", {"user_list": user_list, "relation_list": relation_list})


@check_login
def test1(request):
    # boys = models.UserInfo.objects.filter(gender=1,id=1).first()
    # girls = models.UserInfo.objects.filter(gender=2,id=4).first()
    # models.U2U.objects.create(b_id=boys.id,g_id=girls.id)
    # 传对象
    # models.U2U.objects.create(b=boys,g=girls)

    # models.U2U.objects.create(b_id=3, g_id=5)
    # x = models.UserInfo.objects.filter(id=1).first()
    # result = x.girls.all()
    # for u in result:
    #     print(u.g.username)
    # print(x.girls.values("g_id", "g__username"))

    return HttpResponse("ok")


@check_login
def test2(request):
    # 自关联查第一列
    # x = models.UserInfo.objects.filter(id=1).first()
    # result = x.m.all()
    # for u in result:
    #     print(u.username)

    # 二
    # x = models.UserInfo.objects.filter(id=4).first()
    # result = x.userinfo_set.all()
    # for u in result:
    #     print(u.username)
    #
    return HttpResponse("ok")


@check_login
def test(request):
    return HttpResponse("ok")
