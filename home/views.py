from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .models import SwimPosts, JoinSwim, Review
from .forms import AddSwimForm, EditSwimForm, ReviewForm, EditReviewForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView  # noqa


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
    This method sets the contributer to the current user making the request
    It adds a success message from the messages framework however if the form
    is successful it will be redirector to home as outlined by the success_url
    above so the message is not often shown.
    If the form is not valid you will recieve an error message, it also renders
    the response using the form and heading when the form is invalid.
    """
    model = SwimPosts
    template_name = "home/add_swim.html"
    form_class = AddSwimForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for adding a new swim")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(self.get_context_data(form=form, heading='Add Swim'))  # noqa


# Delete Swim View
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


# Edit Swim View
class EditSwimView(UpdateView):
    """
    Shows the edit swim page so that the authenticated user can edit
    their own swims
    """
    model = SwimPosts
    template_name = "home/edit_swim.html"
    form_class = EditSwimForm
    success_url = reverse_lazy('home')

    def swim_edit(self, request):
        messages.success(self, request, "Swim has been updated")
        return response


# Join Swim View
class JoinSwimView(generic.ListView):
    """
    Shows the user the swims they have chosen to join
    """
    template_name = 'home/joined_swims.html'
    context_object_name = 'joined_swims'
    model = JoinSwim

    def get(self, request):
        return super().get(request)

    def get_queryset(self):
        return JoinSwim.objects.filter(user=self.request.user)
        return queryset


def JoinSwimList(request, pk):
    swim = get_object_or_404(SwimPosts, pk=pk)
    user = request.user

    if JoinSwim.objects.filter(user=user, swim=swim).exists():
        messages.warning(request, "You have already joined this swim")
    else:
        JoinSwim.objects.create(user=user, swim=swim)
        messages.success(request, "You have joined this swim")
    
    return HttpResponseRedirect(reverse("joined_swims"))


class ReviewView(CreateView):
    model = Review
    template_name = "home/review.html"
    form_class = ReviewForm
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Thanks for adding a review")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(self.get_context_data(form=form))  # noqa


class ReviewList(generic.ListView):
    """
    Returns review list in :model:`home.Review``
    and displays them to the page
    """
    model = Review
    template_name = "home/review.html"
    ordering = "created_on"
    context_object_name = "reviews"

    def get_queryset(self):
        return Review.objects.all()


# Delete Review View
class DeleteReviewView(DeleteView):
    """
    Shows the delete review page so that the authenticated user can delete
    their own reviews
    """
    model = Review
    template_name = "home/delete_review.html"
    success_url = reverse_lazy('review_list')

    def review_delete(self, request):
        messages.success(self, request, "Review has been deleted")
        return super().delete(request)


# Edit Review View
class EditReviewView(UpdateView):
    """
    Shows the edit review page so that the authenticated user can edit
    their own reviews
    """
    model = Review
    template_name = "home/edit_review.html"
    form_class = EditReviewForm
    success_url = reverse_lazy('review_list')

    def review_edit(self, request):
        messages.success(self, request, "Review has been updated")
        return response