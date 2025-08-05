"""Forms for managing departments and machines."""

from django import forms

from .models import Department, Machine


class DepartmentForm(forms.ModelForm):
    """Form for creating departments."""

    class Meta:
        model = Department
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class MachineForm(forms.ModelForm):
    """Form for creating machines."""

    class Meta:
        model = Machine
        fields = ["name", "serial_number", "department", "last_maintenance"]
        widgets = {"last_maintenance": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

