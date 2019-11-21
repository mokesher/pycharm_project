from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views, user


urlpatterns = [
    path('user/', user.user_list),
    path('teacher/', views.teacher_list),
    path('add_user/', user.add_user),
    path('delete_user/', user.delete_user),

    path('custom/', views.custom),
    path('orm/', views.orm),
    path('many/', views.many),

]
