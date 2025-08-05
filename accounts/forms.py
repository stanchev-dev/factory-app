from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from urllib.parse import urlparse


def validate_image_url(value: str):
    if not value:
        return
    allowed_extensions = [".jpg", ".jpeg", ".png", ".svg"]
    if not any(value.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError("URL must end with .jpg, .jpeg, .png, or .svg")
    if value.startswith("/static/"):
        return
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https"):
        raise ValidationError("Enter a valid URL or static path.")
    # The previous implementation attempted to perform a HEAD request to the
    # provided URL to ensure the resource exists and is an image.  Relying on
    # network access in validation caused registration to fail in environments
    # without internet access.  Instead, we now trust the URL's extension and
    # scheme without making any external requests.
    return


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        help_text="Required. 30 characters or fewer. Letters, digits and underscores only.",
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z0-9_]+$",
                message=_("Username may contain only letters, digits and underscores."),
            )
        ],
        error_messages={"max_length": _("Username may be up to 30 characters long.")},
    )
    role = forms.ChoiceField(choices=CustomUser.RoleChoices.choices)
    secret_key = forms.CharField(
        required=False, help_text="Required if registering as manager."
    )
    profile_picture = forms.CharField(
        required=False,
        label="Profile Image URL",
        validators=[validate_image_url],
        widget=forms.URLInput(),
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password1",
            "password2",
            "role",
            "secret_key",
            "profile_picture",
        )

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        secret_key = cleaned_data.get("secret_key")

        if (
            role == CustomUser.RoleChoices.MANAGER
            and secret_key != settings.MANAGER_SECRET_KEY
        ):
            raise ValidationError("Invalid secret key for manager registration.")
        return cleaned_data

    def clean_profile_picture(self):
        value = self.cleaned_data.get("profile_picture", "")
        return value or settings.DEFAULT_AVATAR_URL


class CustomUserCreationForm(UserCreationForm):
    """Admin form for creating users with a role."""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("role",)


class CustomUserChangeForm(UserChangeForm):
    """Admin form for updating users with the role field."""

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = "__all__"


class EditProfileForm(forms.ModelForm):
    profile_picture = forms.CharField(
        required=False,
        label="Profile Image URL",
        validators=[validate_image_url],
        widget=forms.URLInput(),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "profile_picture")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
        self.fields["profile_picture"].initial = (
            self.instance.profile_picture or settings.DEFAULT_AVATAR_URL
        )

    def clean_profile_picture(self):
        value = self.cleaned_data.get("profile_picture", "")
        return value or settings.DEFAULT_AVATAR_URL
