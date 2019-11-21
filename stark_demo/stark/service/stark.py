#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from stark.utils.Pagination import Pagination
from django.db.models import Q
from django.db.models.fields.related import ManyToManyField,ForeignKey

class ShowList:
    def __init__(self,config,request,data_list):
        self.config = config
        self.request = request
        self.data_list = data_list

    def get_action_list(self):
        temp = []
        for action in self.config.new_actions():
            temp.append({
                "name": action.__name__,
                "desc": action.short_description
            })
        return temp

    def get_filter_linktags(self):
        link_dic = {}
        import copy

        for filter_field in self.config.list_filter:
            parms = copy.deepcopy(self.request.GET)
            cid = self.request.GET.get(filter_field,0)
            filter_field_obj = self.config.model._meta.get_field(filter_field)  # app01.Book.publish

            if isinstance(filter_field_obj,ForeignKey) or isinstance(filter_field_obj,ManyToManyField):
                data_list = filter_field_obj.remote_field.model.objects.all()
            else:
                data_list = self.config.model.objects.all().values(filter_field,"pk")

            temp = []

            if parms.get(filter_field):
                del parms[filter_field]
                temp.append(f"<a href='?{parms.urlencode()}'>All</a>")
            else:
                temp.append(f"<a class='active' href='#'>All</a>")

            for obj in data_list:
                if isinstance(filter_field_obj,ForeignKey) or isinstance(filter_field_obj,ManyToManyField):
                    pk = obj.pk
                    text = str(obj)
                    parms[filter_field] = pk
                else:   # data_list= [{"pk":1,"title":"go"},....]
                    pk = int(obj.get("pk"))
                    text = str(obj.get(filter_field))
                    parms[filter_field] = text

                _url = parms.urlencode()

                if cid==str(pk) or cid==text:
                    link_tag = f"<a class='active' href='?{_url}'>{text}</a>"
                else:
                    link_tag = f"<a href='?{_url}'>{text}</a>"

                temp.append(link_tag)

            link_dic[filter_field] = temp

        return link_dic

    def get_header(self):
        header_list = []
        for field in self.config.header_list():
            if callable(field):
                val = field(self.config, is_header=True)
            elif field == "__str__":
                val = self.config.model_name.upper()
            else:
                val = self.config.model._meta.get_field(field).verbose_name
            header_list.append(val)
        return header_list

    def get_body(self):
        body_list = []
        data_count = self.data_list.count()
        current_page = int(self.request.GET.get("page", 1))
        base_path = self.request.path
        # 分页
        self.pagination = Pagination(current_page, data_count, base_path, self.request.GET, per_page_num=3, pager_count=9)
        self.page_data = self.data_list[self.pagination.start:self.pagination.end]

        for obj in self.page_data:
            temp = []
            for field in self.config.header_list():
                if callable(field):
                    val = field(self.config, obj)
                else:
                    try:
                        field_obj = self.config.model._meta.get_field(field)
                        if isinstance(field_obj, ManyToManyField):
                            ret = getattr(obj,field).all()
                            t = []
                            for item in ret:
                                t.append(str(item))
                            val = ",".join(t)
                        else:
                            val = getattr(obj, field)

                        if field in self.config.list_display_links:
                            _url = self.config.get_change_url("change", obj)
                            val = mark_safe(f"<a href='{_url}'>{val}</a>")

                    except Exception as e:
                        val = getattr(obj, field)

                temp.append(val)
            body_list.append(temp)
        return body_list


class ModelStark:
    list_display = ["__str__", ]
    list_display_links = []
    actions = []
    search_fields = []
    list_filter = []
    modelform_class = None


    def __init__(self,model,site):
        self.model = model
        self.site = site
        self.model_name = model._meta.model_name
        self.app_label = model._meta.app_label

    def delete_selected(self,request, queryset):
        if request.method == "POST":
            queryset.delete()

    delete_selected.short_description = "批量删除"

    def get_modelform_class(self):
        if not self.modelform_class:
            from django.forms import ModelForm

            class ModelFormDemo(ModelForm):
                class Meta:
                    model = self.model
                    fields = "__all__"
                    labels={
                        ""
                    }
            return ModelFormDemo
        else:
            return self.modelform_class

    def edit(self,obj=None,is_header=False):
        if is_header:
            return "操作"

        _url = self.get_change_url("change",obj)

        return mark_safe(f"<a href='{_url}'>编辑</a>")

    def deletes(self,obj=None,is_header=False):
        if is_header:
            return "操作"

        _url = self.get_change_url("delete", obj)

        return mark_safe(f"<a href='{_url}'>删除</a>")

    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return mark_safe('<input id="choice" type="checkbox">')

        return mark_safe(f'<input class="choice_item" type="checkbox" name="selected_pk" value="{obj.pk}">')

    def add_view(self, request):
        ModelFormDemo = self.get_modelform_class()
        form = ModelFormDemo()
        for bfield in form:
            from django.forms.models import ModelChoiceField
            if isinstance(bfield.field,ModelChoiceField):
                bfield.is_pop = True
                related_model_name = bfield.field.queryset.model._meta.model_name
                related_app_name = bfield.field.queryset.model._meta.app_label
                _url = reverse(f"{related_app_name}_{related_model_name}_add")
                bfield.url = _url + f"?pop_res_id=id_{bfield.name}"

        if request.method == "POST":
            form = ModelFormDemo(request.POST)
            if form.is_valid():
                obj = form.save()

                pop_res_id = request.GET.get("pop_res_id")
                if pop_res_id:
                    res = {"pk":obj.pk,"text":str(obj),"pop_res_id":pop_res_id}

                    return render(request,"pop.html",{"res":res})

                return redirect(self.get_change_url("list"))

        return render(request, "add_view.html",locals())

    def delete_view(self, request, id):
        url = self.get_change_url("list")
        if request.method == "POST":
            self.model.objects.filter(pk=id).delete()
            return redirect(url)

        return render(request,"delete_view.html",locals())

    def change_view(self, request, id):
        ModelFormDemo = self.get_modelform_class()
        edit_obj = self.model.objects.filter(pk=id).first()
        form = ModelFormDemo(instance=edit_obj)
        if request.method == "POST":
            form = ModelFormDemo(request.POST,instance=edit_obj)
            if form.is_valid():
                form.save()
                return redirect(self.get_change_url("list"))

        return render(request,"change_view.html",locals())

    def get_serach_condition(self,request):
        key_word = request.GET.get("q", "")
        self.key_word = key_word
        search_connection = Q()
        if key_word:
            search_connection.connector = "or"
            for search_field in self.search_fields:
                search_connection.children.append((search_field + "__contains", key_word))

        return search_connection

    def get_filter_condition(self,request):
        filter_condition = Q()
        for field in self.list_filter:
            key_word = request.GET.get(field)
            if key_word:
                filter_condition.children.append((field, key_word))

        return filter_condition

    def list_view(self, request):
        if request.method == "POST":
            action = request.POST.get("action")
            selected_pk = request.POST.getlist("selected_pk")
            action_func = getattr(self, action)
            querry_set = self.model.objects.filter(pk__in=selected_pk)
            ret = action_func(request,querry_set)

            # return ret
        # q

        filter_condition = self.get_filter_condition(request)
        serach_condition = self.get_serach_condition(request)

        data_list = self.model.objects.all().filter(serach_condition).filter(filter_condition)

        showlist = ShowList(self,request,data_list)
        add_url = self.get_change_url("add")

        return render(request, "list_view.html", locals())

    def header_list(self):
        temp=[]
        temp.append(ModelStark.checkbox)
        temp.extend(self.list_display)
        if not self.list_display_links:
            temp.append(ModelStark.edit)
        temp.append(ModelStark.deletes)
        return temp

    def new_actions(self):
        temp = []
        temp.append(self.delete_selected)
        temp.extend(self.actions)

        return temp


    def get_change_url(self,name,obj=None):
        if obj:
            _url = reverse(f"{self.app_label}_{self.model_name}_{name}", args=(obj.pk,))
        else:
            _url = reverse(f"{self.app_label}_{self.model_name}_{name}")

        return _url

    def get_urls_2(self):
        temp = []

        temp.append(url(r"^add/", self.add_view, name=f"{self.app_label}_{self.model_name}_add"))
        temp.append(url(r"^(\d+)/delete/", self.delete_view, name=f"{self.app_label}_{self.model_name}_delete"))
        temp.append(url(r"^(\d+)/change/", self.change_view, name=f"{self.app_label}_{self.model_name}_change"))
        temp.append(url(r"^$", self.list_view, name=f"{self.app_label}_{self.model_name}_list"))

        return temp

    @property
    def urls2(self):
        return self.get_urls_2(),None,None


class StarkSite:
    def __init__(self):
        self._registry = {}

    def get_urls(self):
        temp = []
        for model, admin_class in self._registry.items():
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            temp.append(path(f"{app_label}/{model_name}/",admin_class.urls2))

        return temp

    @property
    def urls(self):
        return self.get_urls(),None,None

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelStark

        self._registry[model] = admin_class(model, self)

site=StarkSite()