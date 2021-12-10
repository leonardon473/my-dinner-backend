# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from apps.menu.models import TypeOfCuisine

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


class TypeOfCuisineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "type_of_cuisine_id",
            "name",
        ]
        model = TypeOfCuisine
