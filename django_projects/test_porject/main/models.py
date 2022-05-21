from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    description = models.TextField()

    def __str__(self):
        return self.title
