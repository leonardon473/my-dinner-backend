from django.urls import path
from rest_framework import routers

from .views.rest import menu_item
from .views.rest import type_of_cuisine

router = routers.SimpleRouter()
router.register(r"menu-items", menu_item.MenuItemViewSet)
router.register(r"type-of-cuisine", type_of_cuisine.TypeOfCuisineViewSet)

urlpatterns = router.urls
