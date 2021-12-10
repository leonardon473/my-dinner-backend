# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

# Project libs
from apps.users.models import Client
from apps.users.serializers.client import CreateUserSerializer, RetrieveUserSerializer

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


class CreateListUserView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateUserSerializer


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = RetrieveUserSerializer
