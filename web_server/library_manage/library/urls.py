#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from library import author, book, publisher

urlpatterns = [

    path('publisher_list/', publisher.publisher_list),
    path('add_publisher/', publisher.add_publisher),
    path('delete_publisher/', publisher.delete_publisher),
    path('edit_publisher/', publisher.edit_publisher),

    path('book_list/', book.book_list),
    path('add_book/', book.add_book),
    path('delete_book/', book.delete_book),
    path('edit_book/', book.edit_book),

    path('author_list/', author.author_list),
    path('add_author/', author.add_author),
    path('edit_author/', author.edit_author),
    path('delete_author/', author.delete_author),
]
