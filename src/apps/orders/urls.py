from django.urls import path

from .views.rest import menu_items_sales_by_type_of_cuisine
from .views.rest import order

urlpatterns = [
    path("orders/", order.OrderCreateListView.as_view()),
    path("orders/<int:pk>/", order.OrderRetrieveView.as_view()),
    path(
        "menu-items-sales-by-type-of-cuisine/",
        menu_items_sales_by_type_of_cuisine.MenuItemsSalesByTypeOfCuisineView.as_view(),
    ),
]
