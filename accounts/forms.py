from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.RoleChoices.choices)
    secret_key = forms.CharField(required=False, help_text="Required if registering as manager.")

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role', 'secret_key')

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        secret_key = cleaned_data.get('secret_key')

        if role == CustomUser.RoleChoices.MANAGER and secret_key != settings.MANAGER_SECRET_KEY:
            raise ValidationError("Invalid secret key for manager registration.")
        return cleaned_data
