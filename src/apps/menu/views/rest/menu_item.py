# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import viewsets

# Project libs
from apps.menu.models import MenuItem
from apps.menu.serializers.menu_item import MenuItemSerializer

# If type checking, __all__
if TYPE_CHECKING:
    pass

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    CRUD for MenuItem instances.
    """

    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
