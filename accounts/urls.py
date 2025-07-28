from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, LogoutConfirmView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
