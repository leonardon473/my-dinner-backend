# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from datetime import date, time
from typing import TYPE_CHECKING

# Third party libs
import psycopg2
from django.db import connection as conn

# Project libs
from apps.orders.models import Order, OrderMenuItem
from apps.utils.time import now

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


class ValidateOrderService:
    def __init__(self, order_dict: "Dict[str, Any]", do_validate_time: bool = True):
        self.order_dict = order_dict
        self.do_validate_time = do_validate_time

    def validate(self):
        self.validate_min_order_menu_items()
        self.validate_client_address_is_owner_by_client()
        self.validate_products_are_available()
        if self.do_validate_time:
            self.validate_time()

    def validate_min_order_menu_items(self) -> None:
        """
        Check that at least two items are ordered.
        """
        if len(self.order_dict["order_menu_items"]) < 2:
            raise ValueError(
                {"order_menu_items": "The order must contain al least two menu items."}
            )

    def validate_client_address_is_owner_by_client(self) -> None:
        """
        Check that the client address is owned by the client.
        """
        if self.order_dict["client_address"].client != self.order_dict["client"]:
            raise ValueError(
                {"client_address": "Client address is not owned by the client"}
            )

    def validate_products_are_available(self):
        for i in self.order_dict["order_menu_items"]:
            if not i["menu_item"].is_available:
                raise ValueError(
                    {
                        "order_menu_items": "Some menu item %s is not available"
                        % i["menu_item"].menu_item_id
                    }
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


def get_menu_items_sales_by_type_of_cuisine(
    from_date: date, to_date: date
) -> "List[Dict[str, Any]]":
    sql = """
    SELECT
    c.name,
    count(*) as number_of_sales,
    sum(omi.subtotal) sales_amount
    FROM "menu_typeofcuisine" c
    INNER JOIN "menu_menuitem" mi on mi.type_of_cuisine_id = c.type_of_cuisine_id
    INNER JOIN "orders_ordermenuitem" omi on omi.menu_item_id = mi.menu_item_id
    INNER JOIN "orders_order" o on o.order_id = omi.order_id
    WHERE o.created::date BETWEEN %s and %s
    GROUP BY c.type_of_cuisine_id
    """
    params = (from_date, to_date)

    conn.ensure_connection()
    with conn.connection.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cursor:
        cursor = conn._prepare_cursor(cursor)
        cursor.execute(sql, params)
        type_of_cuisines = cursor.fetchall()
    cursor.close()
    conn.close()
    return type_of_cuisines
