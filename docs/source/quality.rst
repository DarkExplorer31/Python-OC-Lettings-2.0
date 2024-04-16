Quality and Maintainability
===========================

In this section, we will discuss the measures taken to ensure code quality and improve maintainability. 

Code quality
------------

To maintain high code quality standards, we have implemented the following practices:

- **Flake8 and Black Formatter**: We utilize Flake8 and Black Formatter extensions in VSCode for Python code. 
Flake8 ensures adherence to PEP8 standards, while Black Formatter enforces consistent code formatting.
These extensions is be used to confirm the respect of PEP on Python

- **djLint for Templates**: For Django templates, we employ djLint to ensure clean and well-structured HTML code.

- **Docstrings**: Throughout the codebase, we extensively use docstrings to provide clear and concise documentation for all functions and methods. 
Docstrings serve as invaluable resources for understanding the purpose and usage of various code components.

These practices help ensure that our codebase remains clean, consistent, and easy to maintain over time. 
By adhering to established coding standards and documenting our code effectively, we enhance readability, facilitate collaboration, and minimize technical debt.

Unit tests
----------

As mentioned in the index, nine tests have been implemented throughout the codebase.

Each application has three tests using pytest, resulting in a total coverage of 83%. 
You can check the coverage using the following command: ``pytest --cov=..``
To run only the tests, use: ``pytest -v``. For more detailed coverage information, use: ``pytest --cov=. --cov-report html``.
This command will generate a directory named ``htmlcov``, where you can view the tested parts of the code in the generated ``index.html`` file.

The Lettings and Profile applications use a conftest.py file. This file defines a fixture used in the application's tests. Here's an example of code in the conftest.py file of the Profile application:

**Lettings and Profile applicaions** use a ``conftest.py``. This file defines a fixture used in the application's tests.
Here's an example of code in the ``conftest.py`` file of the **Profile** application:

.. code-block:: python

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

The tests are organized in a directory named tests in all applications. 
Here's an example of code in the ``test_profile.py`` file:

.. code-block:: python
    @pytest.mark.django_db
    def test_profiles_index_view(profiles_fixture):
        """
        Test the profiles index view.

        Args:
            client: Django test client.
            profiles_fixture: Fixture providing test data.
        """
        user1, user2 = profiles_fixture
        client = Client()
        url = reverse("profiles:profiles_index")
        response = client.get(url)
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

All tests use Client() from ``django.test`` to test database transactions with views.

Sentry
------