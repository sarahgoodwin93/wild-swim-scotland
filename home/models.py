from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SwimPosts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='Swim Description')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(default='Swim Location')


class Comment(models.Model):
    post = models.ForeignKey(
        SwimPosts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
