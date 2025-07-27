from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Inspection, InspectionReport
from .forms import InspectionForm, InspectionReportForm

class InspectionListView(LoginRequiredMixin, ListView):
    model = Inspection
    template_name = 'inspections/inspection_list.html'


class InspectionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Inspection
    form_class = InspectionForm
    template_name = 'inspections/inspection_form.html'
    success_url = reverse_lazy('inspection_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.role == 'manager'


class InspectionReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = InspectionReport
    form_class = InspectionReportForm
    template_name = 'inspections/report_form.html'
    success_url = reverse_lazy('inspection_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.role == 'manager'

