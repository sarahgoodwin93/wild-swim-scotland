from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class SwimPosts(models.Model):
    """
    Swim Post Model stores information about the swim post, including
    its title, creator, image, description, date, time, location,
    swim difficulty, and timestamps.
    """
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='swim_post')  # noqa
    post_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    swim_difficulty = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0), ])  # noqa
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class JoinSwim(models.Model):
    """
    The Join Swim Model stores information about a user
    joining a swim post, including the swim post they joined,
    the user who joined, and the timestamp when they joined.

    """
    swim = models.ForeignKey('SwimPosts', on_delete=models.CASCADE, related_name='swims_joined')  # noqa
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_swim')  # noqa
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} joined {self.swim.title}"
