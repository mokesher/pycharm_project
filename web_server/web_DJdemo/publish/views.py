from django.shortcuts import render, HttpResponse, redirect
from publish import models


def publisher_list(request):
    ret = models.Publisher.objects.all()
    # ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publish/publisher_list.html", {"publisher_list": ret})


def add_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        models.Publisher.objects.create(name=new_name)
        return redirect("/publisher_list/")

    return render(request, "publish/add_publisher.html")


def delete_publisher(request):
    error_msg = ""
    del_id = request.GET.get('id', None)
    print("1111111", del_id)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id).delete()
        return redirect("/publisher_list/")
    else:
        error_msg = "删除的id不存在!"
    return render(request, "publish/add_publisher.html", {"error": error_msg})


def edit_publisher(request):
    if request.method == "POST":
        new_name = request.POST.get('publisher_name')
        edit_id = request.POST.get('id')
        models.Publisher.objects.filter(id=edit_id).update(name=new_name)
        return redirect("/publisher_list/")

    edit_id = request.GET.get('id')
    if edit_id:
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "publish/edit_publisher.html", {"publisher": edit_obj})
