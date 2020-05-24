#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path, re_path
from django.shortcuts import render


class ModelsXadmin:
    list_display = ["__str__", ]

    def __init__(self, model, site):
        self.model = model
        self.site = site

    def list_view(self, request):
        model_name = self.model._meta.model_name
        data_list = self.model.objects.all()
        print("data_list", data_list)

        header_list = []
        for field in self.list_display:
            if isinstance(field, str):
                if field == "__str__":
                    var = self.model._meta.model_name
                else:
                    field_obj = self.model._meta.get_field(field)
                    var = field_obj.verbose_name
            else:
                var = field(self, is_header=True)

            header_list.append(var)

        new_data_list = []
        for obj in data_list:
            temp = []
            for field in self.list_display:
                if isinstance(field, str):
                    val = getattr(obj, field)
                else:
                    val = field(self, obj)

                temp.append(val)
            new_data_list.append(temp)

        return render(request, 'list_view.html', {
            "new_data_list": new_data_list,
            "header_list": header_list,
            "model_name": model_name})

    def add_view(self, request):
        return render(request, 'add_view.html')

    def change_view(self, request, id):
        return render(request, 'change_view.html')

    def delete_view(self, request, id):
        return render(request, 'delete_view.html')

    def get_urls2(self):
        temp2 = []

        temp2.append(re_path("^$", self.list_view))
        temp2.append(re_path("^add/", self.add_view))
        temp2.append(re_path("^change/(\d+)/$", self.change_view))
        temp2.append(re_path("^delete/(\d+)$", self.delete_view))

        print("temp2", temp2)
        return temp2

    @property
    def urls2(self):
        return self.get_urls2(), None, None


class XadminSite:
    def __init__(self, name="admin"):
        self._registry = {}

    def get_urls(self):
        print(self._registry)

        temp1 = []
        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            model_name = model._meta.model_name

            temp1.append(path(f'{app_name}/{model_name}/', admin_class_obj.urls2), )

            '''
               url(r"app01/book",ModelXadmin(Book,site).urls2)
               url(r"app01/publish",ModelXadmin(Publish,site).urls2)
               url(r"app02/order",ModelXadmin(Order,site).urls2)
            '''

        print("temp1", temp1)
        return temp1

    @property
    def urls(self):

        return self.get_urls(), None, None

    def registry(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelsXadmin

        self._registry[model] = admin_class(model, self)  # {Book:ModelAdmin(Book),Publish:ModelAdmin(Publish)}


site = XadminSite()
