"""stark_demo URL Configuration

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
from django.urls import path
from stark.service.stark import site
from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, "index.html")


def add(request):
    if request.method == "POST":
        return HttpResponse("ok")

    return render(request, "add_book.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    path('stark/', site.urls),
    path('add_book/', add)

]

# path('stark/', ([
#                     path("app01/book", book),
#                     path("stark/author", author),
#                 ], None, None
# ))
