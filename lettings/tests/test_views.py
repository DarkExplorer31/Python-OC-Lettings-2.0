import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_view(client):
    client = Client()
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    assert response.status_code == 200
