# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from apps.orders.models import Order, OrderMenuItem

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict, List

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# --------
#  Create
# --------


class OrderMenuItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "menu_item",
            "quantity",
        ]
        model = OrderMenuItem


class OrderCreateSerializer(serializers.ModelSerializer):
    order_menu_items = OrderMenuItemCreateSerializer(many=True)

    class Meta:
        fields = [
            "client",
            "client_address",
            "order_menu_items",
        ]
        model = Order

    def validate_order_menu_items(
        self, value: "List[Dict[str, Any]]"
    ) -> "List[Dict[str, Any]]":
        """
        Check that at least two items are ordered.
        """
        if len(value) < 2:
            raise serializers.ValidationError(
                "La orden debe contener al menos 2 elementos del menu"
            )
        return value

    def validate(self, attrs: "Dict[str, Any]") -> "Dict[str, Any]":
        """
        Check that the client address is owned by the client.
        """
        if attrs["client_address"].client != attrs["client"]:
            raise serializers.ValidationError(
                {"client_address": "Client address is not owned by the client"}
            )
        return attrs


# ----------
#  Retrieve
# ----------


class OrderMenuItemRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "menu_item",
            "quantity",
            "unit_price",
            "subtotal",
        ]
        model = OrderMenuItem


class OrderRetrieveSerializer(serializers.ModelSerializer):
    order_menu_items = OrderMenuItemCreateSerializer(many=True)

    class Meta:
        fields = [
            "order_id",
            "client",
            "client_address",
            "total_amount",
            "created",
            "order_menu_items",
        ]
        model = Order
