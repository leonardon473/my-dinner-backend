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


class TypeOfCuisine(models.Model):
    type_of_cuisine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Type of cuisine"
        verbose_name_plural = "Types of cuisine"

    def __str__(self) -> str:
        return self.name
