from django.urls import path

from . import views

urlpatterns = [
    path('', views.inspection_list, name='inspection_list'),
]
