from django.contrib import admin
from django.urls import path
from Form_login import views
from Form_login import lists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('test/', views.test),
    path('', views.login),
    path('ajax_login/', views.ajax_login),

    path('class_list/', lists.class_list),
    path('add_class/', lists.add_class),
    path('edit_class/<int:nid>', lists.edit_class),

    path('student_list/', lists.student_list),
    path('add_student/', lists.add_student),
    path('edit_student/<int:nid>', lists.edit_student),

]
