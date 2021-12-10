# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from datetime import time
from typing import TYPE_CHECKING

# Third party libs

# Project libs
from apps.orders.models import Order, OrderMenuItem
from apps.utils.time import now

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


class ValidateOrderService:
    def __init__(self, order_dict: "Dict[str, Any]", do_validate_time: bool = True):
        self.order_dict = order_dict
        self.do_validate_time = do_validate_time

    def validate(self):
        self.validate_min_order_menu_items()
        self.validate_client_address_is_owner_by_client()
        if self.do_validate_time:
            self.validate_time()

    def validate_min_order_menu_items(self) -> None:
        """
        Check that at least two items are ordered.
        """
        if len(self.order_dict["order_menu_items"]) < 2:
            raise ValueError(
                {
                    "order_menu_items": "La orden debe contener al menos 2 "
                    "elementos del menu"
                }
            )

    def validate_client_address_is_owner_by_client(self) -> None:
        """
        Check that the client address is owned by the client.
        """
        if self.order_dict["client_address"].client != self.order_dict["client"]:
            raise ValueError(
                {"client_address": "Client address is not owned by the client"}
            )

    def validate_time(self) -> None:
        if now().time() < time(16, 0) or now().time() > time(21, 0):
            raise ValueError(
                "Invalid schedule, the working time is from 16:00 to 21:00."
            )


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
