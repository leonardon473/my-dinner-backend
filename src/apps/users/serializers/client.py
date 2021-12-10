# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from src.apps.users.models import Client

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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "email",
            "full_name",
            "mobile_number",
            "password",
        ]
        model = Client

    def to_representation(self, instance: Client):
        return RetrieveUserSerializer(instance).data


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "email",
            "full_name",
            "mobile_number",
        ]
        model = Client
