# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import viewsets

# Project libs
from apps.menu.models import TypeOfCuisine
from apps.menu.serializers.type_of_cuisine import TypeOfCuisineSerializer

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


class TypeOfCuisineViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing TypeOfCuisine instances.
    """

    serializer_class = TypeOfCuisineSerializer
    queryset = TypeOfCuisine.objects.all()
