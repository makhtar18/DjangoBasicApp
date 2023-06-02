from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add, name='add'),
    re_path(r'^department$', views.departmentApi, name="departmentApi"),
    re_path(r'^department/([0-9]+)$', views.departmentApi, name="departmentApi"),
]