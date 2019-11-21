from django.contrib import admin
from django.urls import path
from login import views
from login import login_func

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),

    path('test/', views.test),
    path('test1/', views.test1),
    path('test2/', views.test2),

    path('login/', login_func.Login.as_view()),
    path('registe/', login_func.registe.as_view()),
    path('logout/', login_func.logout)
]
