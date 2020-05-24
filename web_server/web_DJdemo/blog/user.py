from blog import models
from django.shortcuts import redirect, render, HttpResponse


def user_list(request):
    ret = models.UserInfo.objects.all()
    return render(request, "blog/user_list.html", {"user_list": ret})


def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("username", None)
        models.UserInfo.objects.create(name=new_name)
        return redirect("/user_list/")
    return render(request, "blog/add_user.html")


def delete_user(request):
    del_id = request.GET.get('id', None)
    if del_id:
        models.UserInfo.objects.get(id=del_id).delete()
        return redirect("/user_list/")
    else:
        return HttpResponse("删除的id不存在!")
