from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    salary = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
