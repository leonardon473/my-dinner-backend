from django.urls import path
from .views.rest import client
from .views.rest import client_address

urlpatterns = [
    path("clients/", client.CreateListUserView.as_view()),
    path("clients/<int:pk>/", client.UserRetrieveUpdateView.as_view()),
    path("clients-addresses/", client_address.ClientAddressCreateListView.as_view()),
    path(
        "clients-addresses/<int:pk>/",
        client_address.ClientAddressRetrieveUpdateView.as_view(),
    ),
]
