from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, UpdateView
from django.urls import reverse_lazy

from .forms import RegistrationForm, EditProfileForm


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')  # could redirect to login if preferred

    def form_valid(self, form):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            role=form.cleaned_data['role'],
            profile_picture=form.cleaned_data['profile_picture'],
        )
        login(self.request, user)
        return super().form_valid(form)


class LogoutConfirmView(TemplateView):
    template_name = 'accounts/logout_confirm.html'


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/delete_account.html'

    def post(self, request, *args, **kwargs):
        request.user.delete()
        return redirect('index')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
