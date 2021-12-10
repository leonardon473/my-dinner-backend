from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path(
        "openapi",
        get_schema_view(title="My Dinner", version="1.0.0"),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="redoc.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="redoc",
    ),
    # rest apis
    path("orders/", include("apps.orders.urls")),
    path("users/", include("apps.users.urls")),
    path("menu/", include("apps.menu.urls")),
]
