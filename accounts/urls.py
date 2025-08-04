from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView,
    LogoutConfirmView,
    EditProfileView,
    DeleteAccountView,
    ProfileView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/', ProfileView.as_view(), name='view_profile'),
    path('delete/', DeleteAccountView.as_view(), name='delete_account'),
]
