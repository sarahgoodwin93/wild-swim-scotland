from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import SwimPosts, JoinSwim
from .forms import AddSwimForm, EditSwimForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


# Swim List View
class SwimList(generic.ListView):
    """
    Returns swim list in :model:`home.SwimPosts``
    and displays them to the home page
    """

    queryset = SwimPosts.objects.all()
    model = SwimPosts
    template_name = "home/swim_posts.html"


# AddSwim View
class AddSwimView(LoginRequiredMixin, CreateView):
    """
    Shows the AddSwimForm so that staff users can make new posts,
    once the post is added, it will take you back to the homepage so
    that you can view your new post. It adds a success message from the
    messages framework however if the form is successful it will be
    redirector to home as outlined by the success_url above so the message
    is not often shown. If the form is not valid you will recieve an
    error message, it also renders the response using the form and
    heading when the form is invalid, however there is error handling with
    the form to now allow an invalid form to be submitted so this
    error message is not often shown.
    """

    model = SwimPosts
    template_name = "home/add_swim.html"
    form_class = AddSwimForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, "Thanks for adding a new swim")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with the form.")
        return self.render_to_response(
            self.get_context_data(form=form, heading="Add Swim")
        )


# Delete Swim View
class SwimDeleteView(LoginRequiredMixin, DeleteView):
    """
    Shows the delete swim page so that the authenticated user can delete
    their own swims. Once the swim has been delete it will redirect back
    to the homepage using the success_url
    """

    model = SwimPosts
    template_name = "home/delete_swim.html"
    success_url = reverse_lazy("home")

    def swim_delete(self, request):
        messages.success(self, request, "Swim has been deleted")
        return super().delete(request)


# Edit Swim View
class EditSwimView(LoginRequiredMixin, UpdateView):
    """
    Shows the edit swim page so that the authenticated user can edit
    their own swims, once the user has edited the swim sucssefully it will
    redirect back to the homepage using the success_url
    """

    model = SwimPosts
    template_name = "home/edit_swim.html"
    form_class = EditSwimForm
    success_url = reverse_lazy("home")

    def swim_edit(self, request):
        messages.success(self, request, "Swim has been updated")
        return response


# Join Swim View
class JoinSwimView(generic.ListView):
    """
    Shows the user the swims they have chosen to join by taking them to
    the joined_swims.html page. It filters the swims that only the user has
    requested to join.
    """

    template_name = "home/joined_swims.html"
    context_object_name = "joined_swims"
    model = JoinSwim

    def get(self, request):
        return super().get(request)

    def get_queryset(self):
        return JoinSwim.objects.filter(user=self.request.user)
        return queryset


# Join Swim List
class JoinSwimList(View):
    """
    This view handles the process of a user joining a swim and
    redirects them to the 'joined_swims' page by using the primary
    key of the user that wants to join the swim. It checks if the user
    has already joined the swim, if the user has not yet joined
    they will be taken to the joined_swims.html page to see
    their joined swim.
    """

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        swim = get_object_or_404(SwimPosts, pk=pk)
        user = request.user

        if JoinSwim.objects.filter(user=user, swim=swim).exists():
            messages.warning(request, "You have already joined this swim")
        else:
            JoinSwim.objects.create(user=user, swim=swim)
            messages.success(request, "You have joined this swim")

        return HttpResponseRedirect(reverse("joined_swims"))


# Remove Joined Swim
class RemoveJoinedSwimView(View):
    """
    Allows users to removew a swim from their joined swims list.
    When a user clicks on the 'Remove this swim' button, it
    triggers a POST request to this view, which then removes the
    specified swim from the user's list.
    """

    def post(self, request, pk):
        join_swim = JoinSwim.objects.filter(user=request.user, swim__pk=pk).first()
        if join_swim:
            join_swim.delete()
        return HttpResponseRedirect(reverse("joined_swims"))


# Handle 404 View
def handle404(request, exception):
    """
    404 error page.
    """
    return render(request, "404.html", status=404)


# Handle 500 View
def handle500(request):
    """
    500 error page.
    """
    return render(request, "500.html", status=500)
