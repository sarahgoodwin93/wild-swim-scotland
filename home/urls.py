from . import views
from django.urls import path
from .views import (
    SwimList,
    AddSwimView,
    SwimDeleteView,
    EditSwimView,
    JoinSwimView,
    JoinSwimList,
    RemoveJoinedSwimView,
)

urlpatterns = [
    path("", views.SwimList.as_view(), name="home"),
    path("swim/add", AddSwimView.as_view(), name="add_swim"),
    path(
        "article/delete/<int:pk>/",
        SwimDeleteView.as_view(), name="delete_swim"
    ),
    path("article/edit/<int:pk>/", EditSwimView.as_view(), name="edit_swim"),
    path("swim/join/<int:pk>/", JoinSwimList.as_view(), name="join_swim"),
    path("swim/joined_swims/", JoinSwimView.as_view(), name="joined_swims"),
    path(
        "swim/remove/<int:pk>/",
        RemoveJoinedSwimView.as_view(),
        name="remove_joined_swim",
    ),
]
