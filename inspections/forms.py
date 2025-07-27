from django import forms
from .models import Inspection, InspectionReport
from suggestions.models import Machine


class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['name', 'machine', 'interval_days', 'last_performed', 'next_due']


class InspectionReportForm(forms.ModelForm):
    class Meta:
        model = InspectionReport
        fields = ['inspection', 'performed_at', 'notes']


