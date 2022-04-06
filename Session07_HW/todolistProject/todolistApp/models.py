from django.db import models
from datetime import date

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    due = models.DateField()

    def __str__(self):
        return self.title