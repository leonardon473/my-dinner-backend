# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs

# Project libs
from apps.orders.models import Order, OrderMenuItem

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class CreateOrderService:
    def __init__(self, order_dict: "Dict[str, Any]"):
        self.order_dict = order_dict

    def create(self) -> "Order":
        order_payload = self.get_order_payload()
        order = Order.objects.create(**order_payload)
        for i in self.order_dict["order_menu_items"]:
            order_menu_item_payload = self.get_order_menu_item_payload(i, order)
            OrderMenuItem.objects.create(
                **order_menu_item_payload,
            )

        return order

    def get_order_payload(self):
        total_amount = sum(
            [
                i["menu_item"].price * i["quantity"]
                for i in self.order_dict["order_menu_items"]
            ]
        )
        return {
            "client": self.order_dict["client"],
            "client_address": self.order_dict["client_address"],
            "total_amount": total_amount,
        }

    def get_order_menu_item_payload(
        self,
        omi_dict: "Dict[str, Any]",
        order: "Order",
    ):
        """
        omi_dict: Order menu item creation dict
        """
        subtotal = omi_dict["menu_item"].price * omi_dict["quantity"]
        return {
            "order": order,
            "menu_item": omi_dict["menu_item"],
            "quantity": omi_dict["quantity"],
            "unit_price": omi_dict["menu_item"].price,
            "subtotal": subtotal,
        }
