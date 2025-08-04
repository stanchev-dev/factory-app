from django.urls import path

from . import views


urlpatterns = [
    path("", views.suggestion_list, name="suggestion_list"),
    path("vote/<int:pk>/<str:vote>/", views.vote_suggestion, name="vote_suggestion"),
    path(
        "status/<int:pk>/<str:status>/",
        views.change_suggestion_status,
        name="change_suggestion_status",
    ),
    path("delete/<int:pk>/", views.delete_suggestion, name="delete_suggestion"),
    path("history/", views.suggestion_history, name="suggestion_history"),
]
