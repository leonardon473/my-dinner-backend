# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework.generics import ListCreateAPIView

# Project libs
from src.apps.users.models import Client
from src.apps.users.serializers.client import CreateUserSerializer

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


class CreateListUserView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateUserSerializer
