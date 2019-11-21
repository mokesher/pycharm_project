from django.shortcuts import render, HttpResponse, redirect
from library import models
from django.utils.decorators import method_decorator
from django.views import View


def index(request):
    return render(request, "index.html")


class Login(View):
    def get(self, request):
        error_msg = ""
        return render(request, "login.html", {'error': error_msg})

    def post(self, request):
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if pwd == "123" and user == "moke":
            request.session['user'] = user
            return redirect("/index/")
        else:
            error_msg = "邮箱或密码错误"
            return render(request, "login.html", {'error': error_msg})



def many(request):
    # 1自定义
    # obj = models.Author.objects.filter(name="alex").first()
    # book_list = obj.many_set.all()
    # for row in book_list:
    #     print(row.book.title)

    # book_list = models.Many.objects.filter(author__name="小明")
    # for row in book_list:
    #     print(row.book.title)

    # book_list = models.Many.objects.filter(author__name="小明").values("book__title")
    # for item in book_list:
    #     print(item["book__title"])

    # book_list = models.Many.objects.filter(author__name="小明").select_related("book")
    # for obj in book_list:
    #     print(obj.book.title)

    # 2django自动生成
    # obj = models.Author.objects.filter(name="alex").first()
    # print(obj.id,obj.name)
    # obj.book.add(1,2)
    # obj.book.add(*[1,])
    # obj.book.set([1,])    #重设
    # obj.book.remove([1,])
    # obj.book.clear()  #删除
    # book_list = obj.book.all()

    # 反向
    # obj = models.Book.objects.filter(title="Java教程").first()
    # v = obj.author_set.values()
    # print(v)

    return HttpResponse("ok")


