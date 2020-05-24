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
from django.urls import path, re_path, include
from blog import views, accounts
from blog import tencent
from django.conf import settings
from django.views.static import serve
from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', accounts.LoginView.as_view()),
    path('register/', accounts.RegisterView.as_view()),
    path('logout/', accounts.logout),
    path('change_pwd/', accounts.change_pwd),
    path('check_username/', accounts.check_username),
    path('set_info/', accounts.set_info),
    path('blog/', include(blog_urls)),

    path('', views.IndexView.as_view()),
    path('index/', views.IndexView.as_view()),

    path('upload/', views.upload),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})

]
