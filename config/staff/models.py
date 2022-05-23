import os

from django.db import models
from django.dispatch import receiver

from hospital.models import Department

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
    photo = models.ImageField(upload_to="doctor", null=True,blank=True)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Doctor)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes photo from filesystem
    when corresponding `Doctor` object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

@receiver(models.signals.pre_save, sender=Doctor)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old photo from filesystem
    when corresponding `Doctor` object is updated
    with new photo.
    """
    if not instance.pk:
        return False

    try:
        old_file = Doctor.objects.get(pk=instance.pk).photo
    except Doctor.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


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
    photo = models.ImageField(upload_to="nurse", null=True,blank=True)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name        

@receiver(models.signals.post_delete, sender=Nurse)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes photo from filesystem
    when corresponding `Nurse` object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

@receiver(models.signals.pre_save, sender=Nurse)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Nurse` object is updated
    with new photo.
    """
    if not instance.pk:
        return False

    try:
        old_file = Nurse.objects.get(pk=instance.pk).photo
    except Nurse.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)