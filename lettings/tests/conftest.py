"""conftest for Lettings app"""

import pytest

from lettings.models import Address, Letting


@pytest.fixture
def lettings_fixture():
    """
    Fixture providing test data for letting-related tests.

    Creates two addresses and their corresponding letting instances.

    Returns:
        tuple: Tuple containing the created Address and Letting instances.
    """
    address1 = Address.objects.create(
        number=65,
        street="Federal St",
        city="Innsmouth",
        state="MA",
        zip_code=11345,
        country_iso_code="USA",
    )
    address2 = Address.objects.create(
        number=456,
        street="Gilman St",
        city="Innsmouth",
        state="MA",
        zip_code=11345,
        country_iso_code="USA",
    )
    letting1 = Letting.objects.create(title="Marsh Office", address=address1)
    letting2 = Letting.objects.create(title="Gilman Hotel", address=address2)
    return address1, letting1, address2, letting2
