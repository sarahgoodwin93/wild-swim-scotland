from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .models import SwimPosts
from .forms import AddSwimForm
from django.views.generic.edit import CreateView, DeleteView


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

    """
    This method sets the contributer to the current user making the request
    It adds a success message from the messages framework however if the form
    is successful it will be redirector to home as outlined by the success_url
    above so the message is not often shown.
    """

    def form_valid(self, form):
        form.instance.contributer = self.request.user
        messages.success(self.request, "Thanks for adding a new swim")
        return super().form_valid(form)

    """
    If the form is not valid you will recieve an error message, it also renders
    the response using the form and heading when the form is invalid.
    """

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(self.get_context_data(form=form, heading='Add Swim'))  # noqa


class SwimDeleteView(DeleteView):
    """
    Shows the delete swim page so that the authenticated user can delete
    their own swims
    """
    model = SwimPosts
    template_name = "home/delete_swim.html"
    success_url = reverse_lazy('home')

    def swim_delete(self, request):
        messages.success(self, request, "Swim has been deleted")
        return super().delete(request)
