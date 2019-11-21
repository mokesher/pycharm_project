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
    sex = sessionid.get('sex')
    user = sessionid.get('user')
    print(sex,user)

    if sex == "man":
        user_list = models.Man.objects.all()
        # relation_list = models.Relation.objects.filter(man__name=user).order_by("woman__id").select_related("woman")
        relation_list = models.Relation.objects.filter(man__name=user).order_by("woman__id").values("woman__id","woman__name")
    else:
        user_list = models.Woman.objects.all()
        # relation_list = models.Relation.objects.filter(woman__name=user).order_by("man__id").select_related("man")
        relation_list = models.Relation.objects.filter(woman__name=user).order_by("man__id").values("man__id","man__name")

    return render(request, "index.html", {"user_list":user_list,"relation_list": relation_list})

