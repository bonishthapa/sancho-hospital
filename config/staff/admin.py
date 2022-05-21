from django.contrib import admin
from staff.models import Doctor, Nurse
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','address','number','qualification']

admin.site.register(Nurse)