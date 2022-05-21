from django.db import models

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