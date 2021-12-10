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


class ClientAddress(models.Model):
    client_address_id = models.AutoField(primary_key=True)
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    num_ext = models.CharField(max_length=50)
    num_int = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Client Address"
        verbose_name_plural = "Client Addresses"

    def __str__(self):
        return self.get_full_address()

    def get_full_address(self):
        address_fields = [
            # 'address_name',
            "street",
            "num_ext",
            "num_int",
            "neighborhood",
            "zip_code",
        ]
        address = [
            getattr(self, field)
            for field in address_fields
            if getattr(self, field) != None and getattr(self, field) != ""
        ]
        return ", ".join(address)
