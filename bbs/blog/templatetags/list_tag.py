#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django import template
from blog import models
from django.db.models import Count

register = template.Library()


@register.inclusion_tag("common/left_tag.html")
def left_panel(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # category_list = models.Category.objects.filter(blog=user.blog)
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")

    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    return {
        "blog": blog,
        "category_list": category_list,
        "tag_list": tag_list,
        "archive_list": archive_list,
    }