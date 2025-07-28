from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, get_user_model
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')  # може и към login, ако предпочиташ

    def form_valid(self, form):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            role=form.cleaned_data['role'],
        )
        login(self.request, user)
        return super().form_valid(form)


class LogoutConfirmView(TemplateView):
    template_name = 'accounts/logout_confirm.html'
