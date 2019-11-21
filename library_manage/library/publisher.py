from django.shortcuts import render, HttpResponse, redirect
from library import models


def publisher_list(request):
    publisher_list = models.Publisher.objects.all().order_by("id")
    return render(request, "library/publisher/publisher_list.html", {"publisher_list": publisher_list})


def add_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        obj = models.Publisher.objects.filter(name=new_name)
        if obj:
            error_msg = "重复的名字"
            return render(request, "library/publisher/add_publisher.html", {"error_msg": error_msg})
        models.Publisher.objects.create(name=new_name)
        return redirect("/library/publisher_list/")

    return render(request, "library/publisher/add_publisher.html")


def delete_publisher(request):
    error_msg = ""
    del_id = request.GET.get('id', None)
    if del_id:
        models.Publisher.objects.get(id=del_id).delete()
        return redirect("/library/publisher_list/")
    else:
        error_msg = "删除的id不存在!"

    return render(request, "library/publisher/add_publisher.html", {"error": error_msg})


def edit_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get('publisher_name')
        edit_id = request.POST.get('id')
        models.Publisher.objects.filter(id=edit_id).update(name=new_name)
        return redirect("/library/publisher_list/")

    edit_id = request.GET.get('id')
    if edit_id:
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "library/publisher/edit_publisher.html", {"publisher": edit_obj})
