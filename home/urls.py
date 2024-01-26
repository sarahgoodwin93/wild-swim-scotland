from . import views
from django.urls import path
from .views import (SwimList, AddSwimView, SwimDeleteView, EditSwimView, JoinSwimView, join_swim)  # noqa


urlpatterns = [
    path('', views.SwimList.as_view(), name='home'),
    path("swim/add", AddSwimView.as_view(), name="add_swim"),
    path("article/delete/<int:pk>/", SwimDeleteView.as_view(), name="delete_swim"),  # noqa
    path("article/edit/<int:pk>/", EditSwimView.as_view(), name="edit_swim"),  # noqa
    path("swim/join/<int:pk>/", join_swim, name="join_swim"),
    path("swim/joined_swims/", JoinSwimView.as_view(), name="joined_swims"),  # noqa
]
