from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuggestionListView.as_view(), name='suggestion_list'),
    path('create/', views.SuggestionCreateView.as_view(), name='suggestion_create'),
    path('<int:pk>/', views.SuggestionDetailView.as_view(), name='suggestion_detail'),
    path('<int:pk>/update/', views.SuggestionUpdateView.as_view(), name='suggestion_update'),
]

