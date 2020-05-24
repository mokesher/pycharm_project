from django.shortcuts import render, HttpResponse, redirect
from library import models


def book_list(request):
    book_list = models.Book.objects.all().order_by("id")
    return render(request, "library/book/book_list.html", {"book_list": book_list})


def add_book(request):
    if request.method == "POST":
        new_book = request.POST.get("book")
        new_publisher = request.POST.get("publisher")

        models.Book.objects.create(title=new_book, publisher_id=new_publisher)
        return redirect("/library/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, "library/book/add_book.html", {"publisher_list": ret})


def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_title = request.POST.get("title")
        new_publisher = request.POST.get("publisher")

        edit_obj = models.Book.objects.get(id=edit_id)
        edit_obj.title = new_title
        edit_obj.publisher_id = new_publisher
        edit_obj.save()

        return redirect("/library/book_list/")

    edit_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request, "library/book/edit_book.html", {"publisher_list": ret, "book": edit_book_obj})


def delete_book(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Book.objects.get(id=del_id).delete()

    return redirect("/library/book_list/")
