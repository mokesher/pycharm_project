from django.urls import path
from django.conf.urls import url
from Test import views


urlpatterns = [
    path('ajax_test/', views.ajax_test),
    path('test/', views.test),


]
