from django.urls import path

from . import views

urlpatterns = [
    path('', views.inspection_list, name='inspection_list'),
    path('history/', views.inspection_history, name='inspection_history'),
    path('<int:pk>/check/', views.inspection_check, name='inspection_check'),
    path('<int:pk>/delete/', views.InspectionDeleteView.as_view(), name='inspection_delete'),
]
