from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def swim_page(request):
    return HttpResponse("Hello, this will be the swim!")
