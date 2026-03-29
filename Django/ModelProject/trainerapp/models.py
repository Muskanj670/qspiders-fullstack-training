from django.db import models

# Create your models here.

class TrainerModel(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    email = models.EmailField()
    address = models.TextField()
