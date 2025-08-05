from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import default_storage
from .models import CustomUser
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/svg+xml"}


def validate_image_file(uploaded_file):
    if uploaded_file and uploaded_file.content_type not in ALLOWED_CONTENT_TYPES:
        raise ValidationError("Unsupported file type. Allowed types: JPG, PNG, SVG")


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
    profile_picture = forms.FileField(
        required=False,
        label="Profile Image",
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "svg"]),
            validate_image_file,
        ],
        widget=forms.FileInput(),
        help_text="If you don't upload a photo, your profile picture will be set to default.",
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data["role"]
        uploaded_file = self.cleaned_data.get("profile_picture")
        if uploaded_file:
            filename = default_storage.save(
                f"profile_pictures/{uploaded_file.name}", uploaded_file
            )
            user.profile_picture = default_storage.url(filename)
        else:
            user.profile_picture = settings.DEFAULT_AVATAR_URL
        if commit:
            user.save()
        return user


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
    profile_picture = forms.FileField(
        required=False,
        label="Profile Image",
        validators=[
            FileExtensionValidator(["jpg", "jpeg", "png", "svg"]),
            validate_image_file,
        ],
        widget=forms.FileInput(),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "profile_picture")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_file = self.cleaned_data.get("profile_picture")
        if uploaded_file:
            filename = default_storage.save(
                f"profile_pictures/{uploaded_file.name}", uploaded_file
            )
            instance.profile_picture = default_storage.url(filename)
        if commit:
            instance.save()
        return instance
