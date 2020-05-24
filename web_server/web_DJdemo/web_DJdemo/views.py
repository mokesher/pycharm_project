from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator


def index(request):
    v = request.session.get("user")
    print(v)
    if v:
        return render(request, "index.html")
    else:
        return redirect("/login/")


def test(request, page):
    # v = reverse("test_page", args=(page,))
    v = reverse("test_page", kwargs={"page": page})

    return HttpResponse(f"page :{page}  reverse: {v}")


@method_decorator(csrf_protect, name='dispatch')
class Login(View):
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        error_msg = ""
        return render(request, "login.html", {'error': error_msg})

    def post(self, request):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if pwd == "123":
            request.session['user'] = user
            return redirect("/index/")
        else:
            error_msg = "邮箱或密码错误"
            return render(request, "login.html", {'error': error_msg})


@csrf_protect
def csrf1(request):
    if request.method == "GET":
        return render(request, "csrf1.html")
    else:
        return HttpResponse("ok")
