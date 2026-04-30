from django.db import models

class TODOModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
