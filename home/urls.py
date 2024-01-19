from . import views
from django.urls import path
from .views import (SwimList, AddSwimView, SwimDeleteView)


urlpatterns = [
    path('', views.SwimList.as_view(), name='home'),
    path("swim/add", AddSwimView.as_view(), name="add_swim"),
    path("article/delete/<int:pk>/", SwimDeleteView.as_view(), name="delete_swim"),  # noqa
    path("article/edit/<int:pk>/", EditSwimView.as_view(), name="edit_swim"),  # noqa
]
