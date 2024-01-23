from django.contrib import admin
from .models import SwimPosts, Review


@admin.register(SwimPosts)
class SwimAdmin(admin.ModelAdmin):
    swim_post_list = ("title", "description", "created_on", "contributer")
    search_fields = ("title", "description", "created_on", "contributer")


@admin.register(Review)
class RegisterAdmin(admin.ModelAdmin):
    swim_post_list = ("title", "review", "creator", "created_on")
    search_fields = ("title", "review", "creator", "created_on")
