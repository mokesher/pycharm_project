from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from publish import views

urlpatterns = [
    path('publisher/', views.publisher_list),
    path('add_publisher/', views.add_publisher),
    path('delete_publisher/', views.delete_publisher),
    path('edit_publisher/', views.edit_publisher),

]
