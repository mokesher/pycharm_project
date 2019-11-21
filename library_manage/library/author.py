from django.shortcuts import render, HttpResponse, redirect
from library import models


def author_list(request):
    author_list = models.Author.objects.all().order_by("id")
    for i in author_list:
        print(i.book)
    return render(request, "library/author/author_list.html", {"author_list": author_list})


def add_author(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        books = request.POST.getlist("books")
        new_author_obj = models.Author.objects.create(name=new_name)
        #############d多对多###############
        new_author_obj.book.set(books)

        return redirect("/library/author_list/")

    ret = models.Book.objects.all()
    return render(request, "library/author/add_author.html", {"book_list": ret})


def edit_author(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_name = request.POST.get("author")
        books = request.POST.getlist("books")
        edit_obj = models.Author.objects.get(id=edit_id)
        edit_obj.name = new_name
        edit_obj.book.set(books)
        edit_obj.save()
        return redirect("/library/author_list/")

    edit_id = request.GET.get("id")
    author_ret = models.Author.objects.get(id=edit_id)
    book_ret = models.Book.objects.all()

    return render(request, "library/author/edit_author.html", {"author": author_ret, "book_list": book_ret})


def delete_author(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Author.objects.filter(id=del_id).delete()

    return redirect("/library/author_list/")

