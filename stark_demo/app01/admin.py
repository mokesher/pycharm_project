from django.contrib import admin

# Register your models here.
from .models import *


class BookConfig(admin.ModelAdmin):
    list_display = ["title","price"]

    def patch_init(self,request,queryset):
        print(queryset)
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"

    actions = [patch_init]

    list_filter = ["title","publish","authors"]

class UserConfig(admin.ModelAdmin):
    list_display = ["id", "name", "age"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]


admin.site.register(UserInfo,UserConfig)
admin.site.register(Book,BookConfig)
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)