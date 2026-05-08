from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    ename = models.CharField(max_length=50)
    age = models.IntegerField()
    job = models.CharField(max_length=100)