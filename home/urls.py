from . import views
from django.urls import path
from .views import (SwimList, 
AddSwimView, SwimDeleteView, EditSwimView, 
JoinSwimView, JoinSwimList, 
ReviewView, ReviewList, EditReviewView, DeleteReviewView)  # noqa


urlpatterns = [
    path('', views.SwimList.as_view(), name='home'),
    path("swim/add", AddSwimView.as_view(), name="add_swim"),
    path("article/delete/<int:pk>/", SwimDeleteView.as_view(), name="delete_swim"),  # noqa
    path("article/edit/<int:pk>/", EditSwimView.as_view(), name="edit_swim"),  # noqa
    path("swim/join/<int:pk>/", JoinSwimList, name="join_swim"),
    path("swim/joined_swims/", JoinSwimView.as_view(), name="joined_swims"),  # noqa
    path("swim/review", ReviewView.as_view(), name="review"),
    path("swim/reviews", ReviewList.as_view(), name="review_list"),
    path("article/delete_review/<int:pk>/", DeleteReviewView.as_view(), name="delete_review"),  # noqa
    path("article/edit_review/<int:pk>/", EditReviewView.as_view(), name="edit_review"),  # noqa
]
