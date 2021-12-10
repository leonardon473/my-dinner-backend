from django.urls import path
from .views.rest import client

urlpatterns = [
    path("clients/", client.CreateListUserView.as_view()),
    path("clients/<int:pk>/", client.UserRetrieveUpdateView.as_view()),
]
