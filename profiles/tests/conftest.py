"""conftest for Profile app"""

import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.fixture
def profiles_fixture():
    """
    Fixture providing test data for profile-related tests.

    Creates two users and their corresponding profiles with different favorite cities.

    Returns:
        tuple: Tuple containing the created User instances.
    """
    user1 = User.objects.create(username="user1")
    user2 = User.objects.create(username="user2")
    Profile.objects.create(user=user1, favorite_city="New York")
    Profile.objects.create(user=user2, favorite_city="Paris")
    return user1, user2
