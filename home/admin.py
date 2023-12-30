from django.contrib import admin 
from .models import SwimPosts, Comment


# Register your models here.
admin.site.register(SwimPosts)
admin.site.register(Comment)