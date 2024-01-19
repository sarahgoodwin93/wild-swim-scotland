from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class SwimPosts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='swim_post')  # noqa
    post_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(default='Swim Description')
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(default='Swim Location')
    swim_difficulty = models.IntegerField(default=0,
        validators= [
            MaxValueValidator(5),
            MinValueValidator(0),
        ]    
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


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
