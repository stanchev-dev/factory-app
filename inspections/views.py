from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Inspection  # Ще го направим по-късно

class InspectionListView(ListView):
    model = Inspection
    template_name = 'inspections.html'  # ще създадем и този файл
