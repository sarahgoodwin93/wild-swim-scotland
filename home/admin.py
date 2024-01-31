from django.contrib import admin
from .models import SwimPosts


@admin.register(SwimPosts)
class SwimAdmin(admin.ModelAdmin):
    swim_post_list = ("title", "description", "created_on", "contributer")
    search_fields = ("title", "description", "created_on", "contributer")
