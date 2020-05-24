#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter(name="split")
def split(s):
    return s.split("/")[-2]


@register.filter(name="list")
def list(name):
    d = {"publisher_list": "出版社列表页", "book_list": "书籍列表页", "author_list": "作者列表页"}
    return d


@register.filter(name="value")
def value(name):
    d = {"publisher_list": "出版社列表页", "book_list": "书籍列表页", "author_list": "作者列表页"}
    return d.get(name)


if __name__ == "__main__":
    print(split("/library/book_list/"))
