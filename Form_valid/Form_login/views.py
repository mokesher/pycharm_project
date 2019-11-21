from django.shortcuts import render, redirect, HttpResponse
from django.forms import fields
from django.forms import Form
from django.views.decorators.csrf import csrf_protect


class LoginForm(Form):
    user = fields.CharField(
        required=True,
    )

    password = fields.CharField(
        required=True,
        max_length=16,
        min_length=3,
    )


# @csrf_protect
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    obj = LoginForm(request.POST)
    if obj.is_valid():
        print(obj.cleaned_data)
        return HttpResponse("ok")
    else:
        print(obj.errors)

        return render(request, "login.html", {"obj": obj})


def ajax_login(request):
    if request.method == "GET":
        obj = LoginForm()
        return render(request, "login.html", {"obj": obj})
    import json
    ret = {'status': True, 'msg': None}
    obj = LoginForm(request.POST)
    if obj.is_valid():
        print(obj.cleaned_data)
        return HttpResponse("ok")
    else:
        # print(obj.errors)
        ret['status'] = False
        ret['msg'] = obj.errors
    v = json.dumps(ret)
    return HttpResponse(v)
            # return render(request, "login.html", {"obj": obj})


class TestForm(Form):
    t1 = fields.CharField(
        required=True,
        min_length=4,
    )
    t2 = fields.IntegerField()


def test(request):
    if request.method == "GET":
        obj = TestForm()
        return render(request, "test.html", {"obj": obj})
    else:
        obj = TestForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return HttpResponse("ok")
        else:
            # print(obj.errors)
            return render(request, "test.html", {"obj": obj})
