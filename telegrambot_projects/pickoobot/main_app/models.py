from enum import unique
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length= 50, unique = True)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_id = models.IntegerField(max_length=25, unique = True)

    