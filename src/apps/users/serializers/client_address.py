# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from apps.users.models import ClientAddress

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


class ClientAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "client",
            "street",
            "num_ext",
            "num_int",
            "neighborhood",
            "zip_code",
        ]
        model = ClientAddress


class ClientAddressRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "client_address_id",
            "street",
            "num_ext",
            "num_int",
            "neighborhood",
            "zip_code",
        ]
        model = ClientAddress
