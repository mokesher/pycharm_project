from django.contrib import admin
from django.utils.safestring import mark_safe

from Xadmin.services.Xadmin import site,ModelsXadmin
from app01.models import *

class BookConfig(ModelsXadmin):
    def edit(self,obj=None,is_header=False):
        if is_header:
            return "操作"

        return mark_safe("<a href='change/%s/'>编辑</a>"%obj.pk)

    list_display = ["nid", "title", "publish", edit]

site.registry(Author)
site.registry(Book,BookConfig)
