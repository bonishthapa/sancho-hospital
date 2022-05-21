from django.views.generic import ListView
from django.shortcuts import render

from staff.models import Doctor

# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor-list.html'