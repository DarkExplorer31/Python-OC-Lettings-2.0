"""Profile application unit tests"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from profiles.apps import ProfilesConfig


@pytest.mark.django_db
def test_profiles_index_view(profiles_fixture):
    """
    Test the profiles index view.

    Args:
        profiles_fixture: Fixture providing test data.
    """
    user1, user2 = profiles_fixture
    client = Client()
    url = reverse("profiles:profiles_index")
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view(profiles_fixture):
    """
    Test the profile view.

    Args:
        profiles_fixture: Fixture providing test data.
    """
    user1, user2 = profiles_fixture
    client = Client()
    url = reverse("profiles:profile", args=[user1.username])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
    assert user1.username.encode() in response.content
    assert b"New York" in response.content


def test_profiles_config():
    """
    Test the configuration of the profiles application.

    Checks that the application configuration is correctly defined.
    Verifies that the name of the application in the configuration matches "profiles".
    """
    app_config = ProfilesConfig
    assert app_config.name == "profiles"
