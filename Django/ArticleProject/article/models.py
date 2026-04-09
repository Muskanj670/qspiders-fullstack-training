from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=None)
    author = models.CharField(max_length=50,default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)