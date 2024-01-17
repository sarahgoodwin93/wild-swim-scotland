from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
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
    model = SwimPosts
    template_name = "home/swim_posts.html"


# AddSwim View
class AddSwimView(CreateView):
    """
    Shows the AddSwimForm so that staff users can make new posts
    once the post is added it will take you back to the homepage
    so that you can view your new post.
    """
    model = SwimPosts
    template_name = "home/add_swim.html"
    form_class = AddSwimForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.contributer = self.request.user
        messages.success(self.request, "Thanks for adding a new swim")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(self.get_context_data(form=form, heading='Add Swim'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Add Swim'
        return context
