from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile associated with a Django User.

    Attributes:
        user (OneToOneField): The associated User instance.
        favorite_city (CharField, optional): The favorite city of the user.

    Methods:
        __str__: Returns a string representation of the profile.

    Meta:
        verbose_name_plural (str): The plural name used in the Django admin interface.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.
        """
        return self.user.username

    class Meta:
        """
        Specifies metadata options for the Profile model.
        """

        verbose_name_plural = "Profiles"
