from django.urls import path
from .views.rest import client

urlpatterns = [
    path("clients/", client.CreateListUserView.as_view()),
]
