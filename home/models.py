from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class SwimPosts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='swim_post')  # noqa
    post_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    swim_difficulty = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0),])  # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    review_title = models.CharField(max_length=200, default="New Review")
    review_location = models.CharField(max_length=300, default="Where did you swim?")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.user}"


class JoinSwim(models.Model):
    swim = models.ForeignKey('SwimPosts', on_delete=models.CASCADE, related_name='swims_joined')  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_swim')  # noqa
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} joined {self.swim.title}"
