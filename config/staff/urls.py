from django.urls import path

from staff.views import DoctorListView

urlpatterns=[
    path('doctor-list', DoctorListView.as_view(), name='doctor_list'),
]