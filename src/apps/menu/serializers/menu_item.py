# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from apps.menu.models import MenuItem

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


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "menu_item_id",
            "name",
            "description",
            "price",
            "type_of_cuisine",
            "is_available",
        ]
        model = MenuItem
