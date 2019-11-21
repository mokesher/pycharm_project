"""auth_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls import url
from blog import views
from blog import tencent
from django.conf import settings
from django.views.static import serve
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('change_pwd/', views.change_pwd),
    path('check_username/', views.check_username),
    path('set_info/', views.set_info),
    path('blog/', include(blog_urls)),

    re_path('index/', views.index),
    path('', views.index),

    path('upload/',views.upload),

    path('tencent_blog/', tencent.tencent_blog),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})


]





