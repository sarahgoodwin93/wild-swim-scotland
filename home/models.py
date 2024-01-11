from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SwimPosts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='Swim Description')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(default='Swim Location')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)


class Review(models.Model):
    review = models.ForeignKey(
        SwimPosts, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"
