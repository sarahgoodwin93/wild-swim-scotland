from . import views
from django.urls import path
from .views import (SwimList, AddSwimView)


urlpatterns = [
    path('', views.SwimList.as_view(), name='home'),
    path("swim/add", AddSwimView.asview(), name="add_swim")
]
