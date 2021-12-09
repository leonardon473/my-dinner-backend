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


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey("users.Client", on_delete=models.PROTECT)
    client_address = models.ForeignKey("users.ClientAddress", on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=7, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self) -> str:
        return str(self.order_id)
