"""Unit tests for oc_lettings_site"""

from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from oc_lettings_site.views import index
from oc_lettings_site.apps import OCLettingsSiteConfig


def test_index_view():
    """
    Test the index view of the application.

    Checks that the index view is accessible and returns an HTTP status code 200.
    Also verifies that the "index.html" template is used for the response.
    """
    client = Client()
    url = reverse(index)
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_404_view():
    """
    Test the handler404 view for 404 errors.

    Ensures that the handler404 view is properly configured to return a 404 error page.
    Also verifies that the "404.html" template is used for the response when the requested URL
    does not exist.
    """
    client = Client()
    response = client.get("/page-does-not-exist/")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


def test_oc_lettings_site_config():
    """
    Test the configuration of the oc_lettings_site application.

    Checks that the application configuration is correctly defined.
    Verifies that the name of the application in the configuration matches "oc_lettings_site".
    """
    app_config = OCLettingsSiteConfig
    assert app_config.name == "oc_lettings_site"
