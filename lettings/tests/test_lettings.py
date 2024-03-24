import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from lettings.apps import LettingsConfig


@pytest.mark.django_db
def test_lettings_index_view(client, lettings_fixture):
    """
    Test the lettings index view.

    Args:
        client: Django test client.
        lettings_fixture: Fixture providing test data for lettings.
    """
    address1, letting1, address2, letting2 = lettings_fixture
    client = Client()
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
    assert letting1.title.encode() in response.content
    assert letting2.title.encode() in response.content


@pytest.mark.django_db
def test_lettings_view(client, lettings_fixture):
    """
    Test the letting view.

    Args:
        client: Django test client.
        lettings_fixture: Fixture providing test data for lettings.
    """
    address1, letting1, address2, letting2 = lettings_fixture
    client = Client()
    url = reverse("lettings:letting", args=[letting1.id])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
    assert letting1.title.encode() in response.content
    assert address1.street.encode() in response.content


def test_lettings_config():
    """
    Test the configuration of the lettings application.

    Checks that the application configuration is correctly defined.
    Verifies that the name of the application in the configuration matches "lettings".
    """
    app_config = LettingsConfig
    assert app_config.name == "lettings"
