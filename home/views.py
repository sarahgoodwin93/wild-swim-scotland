from django.shortcuts import render
from django.views import generic
from .models import SwimPosts
from .forms import AddSwimForm
from django.views.generic.edit import CreateView


# Swim List View
class SwimList(generic.ListView):
    """
    Returns swim list in :model:`home.SwimPosts``
    and displays them to the page
     """
    queryset = SwimPosts.objects.all()
    template_name = "home/swim_posts.html"


# AddSwim View
class AddSwimView(CreateView):
    """
    Displays the 'Add Swim' page
    """
    model = SwimPosts
    template_name = "home/add_swim.html"
    form_class = AddSwimForm

    def form_valid(self, form): 
        form.instance.contributer = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Thanks for adding a new swim")

        return Response
