from django.urls import path

from . import views


urlpatterns = [
    path("", views.suggestion_list, name="suggestion_list"),
    path("vote/<int:pk>/<str:vote>/", views.vote_suggestion, name="vote_suggestion"),
    path("history/", views.suggestion_history, name="suggestion_history"),
]
