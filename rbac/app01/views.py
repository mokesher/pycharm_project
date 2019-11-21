from django.shortcuts import render, HttpResponse,redirect
from curd.models import *
from curd.service.perssions import initial_session


def index(request):

    return render(request, "index.html")


class Per:
    def __init__(self,actions):
        self.actions = actions
    def add(self):
        return "add" in self.actions
    def delete(self):
        return "delete" in self.actions
    def edit(self):
        return "edit" in self.actions
    def list(self):
        return "list" in self.actions




def users(request):
    user_list = User.objects.all()
    per = Per(request.actions)
    id = request.session.get("user_id")
    user = User.objects.filter(pk=id).first()

    return render(request, "users.html", locals())


def add_user(request):

    return HttpResponse("add user.....")


def del_user(request,id):

    return HttpResponse("del"+id)


def roles(request):

    role_list=Role.objects.all()
    id = request.session.get("user_id")
    user = User.objects.filter(pk=id).first()
    per = Per(request.actions)
    return render(request, "roles.html", locals())


def login(request):

    if request.method=="POST":

        user=request.POST.get("user")
        pwd=request.POST.get("pwd")

        user=User.objects.filter(name=user,pwd=pwd).first()
        if user:
            request.session["user_id"] = user.pk

            initial_session(user,request)
            return redirect("/")

    return render(request,"login.html")


def test(request):

    return render(request,"test.html")