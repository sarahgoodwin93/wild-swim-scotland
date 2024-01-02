from django.shortcuts import render
from django.views import generic
from .models import SwimPosts


# Create your views here.
class SwimList(generic.ListView):
    queryset = SwimPosts.objects.all()
    template_name = "home/swim_posts.html"
