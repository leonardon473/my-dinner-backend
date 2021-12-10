# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.contrib.auth.base_user import AbstractBaseUser
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


class ClientManager(models.Manager):
    def create(self, **kwargs):
        """
        Create a new object with the given kwargs, saving it to the database
        and returning the created object.
        """
        password = kwargs.pop("password")
        obj = self.model(**kwargs)
        obj.set_password(password)
        self._for_write = True
        obj.save(force_insert=True, using=self.db)
        return obj


class Client(AbstractBaseUser, models.Model):
    client_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=120, unique=True)
    full_name = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=20)

    objects = ClientManager()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.email
