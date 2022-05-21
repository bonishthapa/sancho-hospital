from django.shortcuts import render
from django.views.generic import ListView
from hospital.models import Banner

# Create your views here.

class HomePageView(ListView):
    model = Banner
    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context={
    #         "apple":"shau",
    #         "mango":"aap"
    #     }
    #     return super().get_context_data(**context)