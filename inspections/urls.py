from django.urls import path

from . import views

urlpatterns = [
    path('', views.inspection_list, name='inspection_list'),
    path('<int:pk>/delete/', views.InspectionDeleteView.as_view(), name='inspection_delete'),
]
