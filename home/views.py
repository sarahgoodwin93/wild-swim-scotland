from django.shortcuts import render
from django.views import generic
from .models import SwimPosts


# Swim List Class View
class SwimList(generic.ListView):
    queryset = SwimPosts.objects.all()
    template_name = "home/swim_posts.html"
