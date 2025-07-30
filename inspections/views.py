from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView

from .models import Inspection

class InspectionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Inspection
    template_name = 'inspections.html'

    def test_func(self):
        return getattr(self.request.user, "role", None) == "manager"
