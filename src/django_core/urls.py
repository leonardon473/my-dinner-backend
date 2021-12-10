from django.urls import include, path


urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("menu/", include("apps.menu.urls")),
]
