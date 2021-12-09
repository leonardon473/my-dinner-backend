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


class MenuItem(models.Model):
    menu_item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    type_of_cuisine = models.ForeignKey("menu.TypeOfCuisine", on_delete=models.PROTECT)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
