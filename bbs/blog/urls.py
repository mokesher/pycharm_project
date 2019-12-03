#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path
from blog import views


urlpatterns = [
    path("<str:username>/", views.ArticleListView.as_view()),
    path("<str:username>/article/<int:article_id>/", views.ArticleDetailView.as_view()),
    path("func/up_down/", views.up_down),
    path("func/comment/", views.comment),
    path("comment_tree/<int:article_id>", views.comment_tree),
    path("<str:username>/article/<int:article_id>/func/del_comment/<int:del_id>", views.del_comment),
    path("func/change_comment/<int:pk>", views.change_comment),

    path("backend/add_article/", views.add_article),
]

