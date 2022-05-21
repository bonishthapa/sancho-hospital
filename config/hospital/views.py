from django.shortcuts import render
from django.views.generic import ListView

from hospital.models import Banner
from staff.models import Doctor, Nurse

# Create your views here.

class HomePageView(ListView):
    model = Banner
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        doctor = Doctor.objects.all()
        nurse = Nurse.objects.all()
        context={
            "doctor":doctor,
            "nurse":nurse
        }
        return super().get_context_data(**context)

# def handler404(request):
#     return render(request,'404.html')