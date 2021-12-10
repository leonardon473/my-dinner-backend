from django.urls import include, path


urlpatterns = [
    path("orders/", include("apps.orders.urls")),
    path("users/", include("apps.users.urls")),
    path("menu/", include("apps.menu.urls")),
]
