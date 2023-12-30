from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SwimPosts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='Swim Description')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(default='Swim Location')



