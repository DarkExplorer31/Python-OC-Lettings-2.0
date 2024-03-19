from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Represents a physical address.

    Attributes:
        number (PositiveIntegerField): The number part of the address.
        street (CharField): The name of the street.
        city (CharField): The city.
        state (CharField): The state (abbreviated).
        zip_code (PositiveIntegerField): The ZIP code.
        country_iso_code (CharField): The ISO country code.

    Methods:
        __str__: Returns a string representation of the address.

    Meta:
        Specifies metadata options for the Address model.

    Attributes:
        verbose_name_plural (str): The plural name used in the Django admin interface.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Specifies metadata options for the Address model.
        """

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting (e.g., property for rent).

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The address of the letting.

    Methods:
        __str__: Returns a string representation of the letting.

    Meta:
        Specifies metadata options for the Letting model.

    Attributes:
        verbose_name_plural (str): The plural name used in the Django admin interface.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        """
        Returns a string representation of the letting.
        """
        return self.title

    class Meta:
        """
        Specifies metadata options for the Letting model.
        """

        verbose_name_plural = "Lettings"
