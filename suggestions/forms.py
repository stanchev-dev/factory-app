from django import forms
from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'description', 'machine']


class SuggestionStatusForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['status']

