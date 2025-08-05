from django.urls import path

from .views import HomeView, department_list, machine_list

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('departments/', department_list, name='department_list'),
    path('machines/', machine_list, name='machine_list'),
]
