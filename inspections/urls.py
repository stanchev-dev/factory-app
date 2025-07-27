from django.urls import path
from . import views

urlpatterns = [
    path('', views.InspectionListView.as_view(), name='inspection_list'),
]
