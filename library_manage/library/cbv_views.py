from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from library import models


def index(request):
    return render(request, "index.html")


def test(request):

    return HttpResponse("ok")


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

    book_list = models.Many.objects.filter(author__name="小明").select_related("book")
    for obj in book_list:
        print(obj.book.title)

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


class Publish(View):

    def publisher_list(self, request):
        ret = models.Publisher.objects.all()
        print(ret)
        # ret = models.Publisher.objects.all().order_by("id")
        return render(request, "library/publisher/publisher_list.html", {"publisher_list": ret})

    def add_publisher(self, request):
        if request.method == "POST":
            new_name = request.POST.get("publisher_name")

            models.Publisher.objects.create(name=new_name)
            return redirect("/publisher_list/")

        return render(request, "library/publisher/add_publisher.html")

    def delete_publisher(self, request):
        error_msg = ""
        del_id = request.GET.get('id', None)
        if del_id:
            del_obj = models.Publisher.objects.get(id=del_id).delete()
            return redirect("/publisher_list/")
        else:
            error_msg = "删除的id不存在!"

        return render(request, "library/publisher/add_publisher.html", {"error": error_msg})

    def edit_publisher(self, request):
        if request.method == "POST":
            new_name = request.POST.get('publisher_name')
            edit_id = request.POST.get('id')
            edit_obj = models.Publisher.objects.get(id=edit_id)
            edit_obj.name = new_name
            edit_obj.save()

            return redirect("/publisher_list/")

        edit_id = request.GET.get('id')
        if edit_id:
            edit_obj = models.Publisher.objects.get(id=edit_id)
            return render(request, "library/publisher/edit_publisher.html", {"publisher": edit_obj})


class Book(View):

    def book_list(self, request):
        all_book = models.Book.objects.all()
        # print(all_book)
        return render(request, "library/book/book_list.html", {"book_list": all_book})

    def add_book(self, request):
        if request.method == "POST":
            new_book = request.POST.get("book_name")
            new_publisher = request.POST.get("publisher")

            models.Book.objects.create(title=new_book, publisher_id=new_publisher)
            return redirect("/book_list/")
        ret = models.Publisher.objects.all()
        return render(request, "library/book/add_book.html", {"publisher_list": ret})

    def edit_book(self, request):
        if request.method == "POST":
            edit_id = request.POST.get("id")
            new_title = request.POST.get("title")
            new_publisher = request.POST.get("publisher")

            edit_obj = models.Book.objects.get(id=edit_id)
            edit_obj.title = new_title
            edit_obj.publisher_id = new_publisher
            edit_obj.save()

            return redirect("/book_list/")

        edit_id = request.GET.get("id")
        edit_book_obj = models.Book.objects.get(id=edit_id)
        ret = models.Publisher.objects.all()
        return render(request, "library/book/edit_book.html", {"publisher_list": ret, "book": edit_book_obj})

    def delete_book(self, request):
        del_id = request.GET.get("id")
        if del_id:
            models.Book.objects.get(id=del_id).delete()

        return redirect("/book_list/")


class Author(View):

    def author_list(self, request):
        ret = models.Author.objects.all()

        return render(request, "library/author/author_list.html", {"author_list": ret})

    def add_author(self, request):
        if request.method == "POST":
            new_name = request.POST.get("name")
            books = request.POST.getlist("books")
            new_author_obj = models.Author.objects.create(name=new_name)

            new_author_obj.book.set(books)

            return redirect("/author_list/")

        ret = models.Book.objects.all()
        return render(request, "library/author/add_author.html", {"book_list": ret})

    def edit_author(self, request):
        if request.method == "POST":
            edit_id = request.POST.get("id")
            new_name = request.POST.get("author")
            books = request.POST.getlist("books")
            edit_obj = models.Author.objects.get(id=edit_id)
            edit_obj.name = new_name
            edit_obj.book.set(books)
            edit_obj.save()
            return redirect("/author_list/")

        edit_id = request.GET.get("id")
        author_ret = models.Author.objects.get(id=edit_id)
        book_ret = models.Book.objects.all()

        return render(request, "library/author/edit_author.html", {"author": author_ret, "book_list": book_ret})

    def delete_author(self, request):
        del_id = request.GET.get("id")
        if del_id:
            models.Author.objects.get(id=del_id).delete()

        return redirect("/author_list/")

