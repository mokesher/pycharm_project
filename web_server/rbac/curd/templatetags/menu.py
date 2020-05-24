#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag("menu.html")
def menu(request):
    menu_permission_list = request.session["menu_permission_list"]
