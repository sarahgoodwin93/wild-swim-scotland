from . import views
from django.urls import path
from .views import (SwimList, AddSwimView, SwimDeleteView)


urlpatterns = [
    path('', views.SwimList.as_view(), name='home'),
    path("swim/add", AddSwimView.as_view(), name="add_swim"),
    path("delete/<int:id>/", views.SwimDeleteView.as_view(), name="delete_swim"),  # noqa
]
