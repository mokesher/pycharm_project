#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from stark.service.stark import site, ModelStark
from .models import *
from django.forms import ModelForm
from django.shortcuts import HttpResponse
from django.forms import widgets


class UserConfig(ModelStark):
    list_display = ["id", "name", "age"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["age"]


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "标题",
            "price": "价格",
        }


class BookConfig(ModelStark):
    list_display = ["title", "price", "publishDate", "publish", "authors"]
    list_display_links = ["title"]
    search_fields = ["title", "price"]
    list_filter = ["publish", "authors", "title", "price"]

    modelform_class = BookModelForm

    def patch_init(self, request, queryset):
        queryset.update(price=11)

        # return HttpResponse("批量初始化OK")

    patch_init.short_description = "批量初始化"

    actions = [patch_init]


site.register(UserInfo, UserConfig)
site.register(Book, BookConfig)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)
