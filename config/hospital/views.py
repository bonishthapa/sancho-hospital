from django.shortcuts import render
from django.views.generic import ListView
from hospital.models import Banner

# Create your views here.

class HomePageView(ListView):
    model = Banner
    template_name = "home.html"