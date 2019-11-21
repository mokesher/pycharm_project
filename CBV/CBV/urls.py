"""CBV URL Configuration

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
from django.urls import path,re_path
from app01 import views
from app02 import views as views2
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register(r'authors', views2.AuthorModelView)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^publishes/$', views.PublishView.as_view(),name="publish"),
    re_path('^publishes/(\d+)/', views.PublishDetailView.as_view(),name="detailpublish"),
    re_path('books/$', views.BookView.as_view(),name="book"),
    path('books/<int:pk>/', views.BookDetailView.as_view(),name="detailbook"),


    # re_path('authors/$', views2.AuthorModelView.as_view({"get":"list","post":"create"}),name="author"),
    # path('authors/<int:pk>/', views2.AuthorModelView.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name="detailauthor"),

    path('login/', views2.LoginView.as_view(),name="login"),

    path('',include(router.urls)),
]

