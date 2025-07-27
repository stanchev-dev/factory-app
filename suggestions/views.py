from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Suggestion
from .forms import SuggestionForm, SuggestionStatusForm


class SuggestionListView(LoginRequiredMixin, ListView):
    model = Suggestion
    template_name = 'suggestions/suggestion_list.html'
    context_object_name = 'suggestions'


class SuggestionDetailView(LoginRequiredMixin, DetailView):
    model = Suggestion
    template_name = 'suggestions/suggestion_detail.html'


class SuggestionCreateView(LoginRequiredMixin, CreateView):
    model = Suggestion
    form_class = SuggestionForm
    template_name = 'suggestions/suggestion_form.html'
    success_url = reverse_lazy('suggestion_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class SuggestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Suggestion
    form_class = SuggestionStatusForm
    template_name = 'suggestions/suggestion_status_form.html'
    success_url = reverse_lazy('suggestion_list')

    def test_func(self):
        return self.request.user.role == 'manager'
