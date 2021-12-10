# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.db import models

# Project libs

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


class OrderMenuItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.PROTECT,
        related_name="order_menu_items",
    )
    menu_item = models.ForeignKey("menu.MenuItem", on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Order menu item"
        verbose_name_plural = "Order menu items"

    def __str__(self) -> str:
        return self.order_item_id
