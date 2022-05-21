from django.db import models

# Create your models here.

class Doctor(models.Model):
    education = [
        ("MBBS","MBBS"),
        ("MD","MD")
    ]
    name = models.CharField(max_length=250)
    dob = models.DateField()
    number = models.IntegerField()
    address = models.CharField(max_length=250)
    qualification = models.CharField(choices=education,max_length=250)

    def __str__(self):
        return self.name


class Nurse(models.Model):
    education = [
        ("BSC NURSING","BSC NURSING"),
        ("STAFF NURSE","STAFF NURSE")
    ]
    name = models.CharField(max_length=250)
    dob = models.DateField()
    number = models.IntegerField()
    address = models.CharField(max_length=250)
    qualification = models.CharField(choices=education,max_length=250)

    def __str__(self):
        return self.name        