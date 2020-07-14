from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from web_DJdemo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'blog/', include('blog.urls')),
    path(r'publish/', include('publish.urls')),
    path(r'', include('Test.urls')),

    url(r'^$', views.index),
    path('index/', views.index),
    path('login/', views.Login.as_view()),


    # path('test/<int:page>', views.test, name="test_page"),
    # url(r'test/(?P<page>\d+)', views.test, name="test_page"),

]
