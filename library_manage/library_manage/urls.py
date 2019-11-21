from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from library import views



urlpatterns = [

    path('', views.Login.as_view()),
    path('login/', views.Login.as_view()),

    path('index/', views.index),
    path('library/', include('library.urls')),



    path('many/', views.many),
    path('test/', views.test),
]
