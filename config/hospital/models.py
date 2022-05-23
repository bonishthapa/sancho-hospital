import os

from django.db import models
from django.dispatch import receiver

# Create your models here.

class Banner(models.Model):
    name = models.CharField(max_length=250)



    def __str__(self):
        return self.name

class Department(models.Model):
    department_name = models.CharField(max_length=250)
    department_description = models.TextField()

    def __str__(self):
        return self.department_name

class Notice(models.Model):
    notice_title = models.CharField(max_length=250,blank=True,null=True)
    notice_image = models.ImageField(upload_to='notices')
    notice_description = models.TextField()

    def __str__(self):
        return self.notice_title

@receiver(models.signals.post_delete, sender=Notice)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes photo from filesystem
    when corresponding `Notice` object is deleted.
    """
    if instance.notice_image:
        if os.path.isfile(instance.notice_image.path):
            os.remove(instance.notice_image.path)

@receiver(models.signals.pre_save, sender=Notice)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Notice` object is updated
    with new photo.
    """
    if not instance.pk:
        return False

    try:
        old_file = Notice.objects.get(pk=instance.pk).notice_image
    except Notice.DoesNotExist:
        return False

    new_file = instance.notice_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)                 