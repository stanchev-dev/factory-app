from django.urls import path

from .views import (
    HomeView,
    department_list,
    delete_department,
    delete_machine,
    machine_list,
)

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('departments/', department_list, name='department_list'),
    path('departments/<int:pk>/delete/', delete_department, name='delete_department'),
    path('machines/', machine_list, name='machine_list'),
    path('machines/<int:pk>/delete/', delete_machine, name='delete_machine'),
]
