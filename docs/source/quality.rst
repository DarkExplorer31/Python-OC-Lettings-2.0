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

Security
--------
For optimal security, certain practices have been implemented:

- All sensitive variables are defined as environment variables in the .env file, which we retrieve using the Python dotenv module, so in case of collaboration, make sure to possess this file. They are also defined in the GitHub repository's secrets and as environment variables in Render.

- Different Admin for production and local: The admin created on Render is very different from the one implemented locally. This allows to keep a secret administrator in production but accessible locally.
    Locally, here is the admin used:
        - Go to ``http://localhost:8000/admin``;
        - Log in with the user ``admin``, password ``Abc1234!``;

- Error templates 404 and 500 have been implemented to control what is displayed to the user.

- Logs are customized in key functions."

Sentry
------

Error tracking with Sentry has also been implemented to ensure optimal maintainability. (see in the settings.py file)

.. code-block:: python
    # Initialize Sentry
    sentry_dsn = os.getenv("SENTRY_DSN")
    if sentry_dsn:
        sentry_sdk.init(
            dsn=sentry_dsn,
            enable_tracing=True,
            traces_sample_rate=0.1,
            profiles_sample_rate=0.1,
        )
    else:
        logger.warning(
            "The SENTRY_DSN environment variable is not defined."
            + " Please contact the previous developer to obtain the link."
        )

Explanation:

``sentry_sdk.init(``:  This function initializes Sentry in your application. It takes several parameters:
    ``dsn``: The Sentry connection URL that we retrieved earlier.
    ``enable_tracing``: This parameter enables performance tracing in Sentry. It is set to True here to enable tracing.
    ``traces_sample_rate``: This parameter controls the sampling rate of performance traces. It is set to 0.1, which means that only 10% of requests will be sampled for performance tracing.
    ``profiles_sample_rate)``: This parameter controls the sampling rate of performance profiles. It is also set to 0.1, which means that only 10% of profiles will be sampled.
