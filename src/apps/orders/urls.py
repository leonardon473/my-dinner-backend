from django.urls import path
from .views.rest import order

urlpatterns = [
    path("orders/", order.OrderCreateListView.as_view()),
    path("orders/<int:pk>/", order.OrderRetrieveView.as_view()),
]
