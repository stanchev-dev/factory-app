from django.urls import path
from . import views

urlpatterns = [
    path('', views.InspectionListView.as_view(), name='inspection_list'),
    path('create/', views.InspectionCreateView.as_view(), name='inspection_create'),
    path('report/', views.InspectionReportCreateView.as_view(), name='inspection_report'),
]

