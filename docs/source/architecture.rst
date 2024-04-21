============
Architecture
============

Dependencies
============

This section lists the dependencies used in the project along with brief descriptions of their functionalities.
These dependencies play a crucial role in the development, testing, and deployment of the project,
providing various utilities and tools for different aspects of software development.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Package
     - Description
   * - ``asgiref``
     - Library for Django web servers. It provides an ASGI specification for Django web applications, allowing them to handle asynchronous requests.
   * - ``Brotli``
     - Compression library. Brotli is a generic-purpose lossless compression algorithm developed by Google, designed to achieve better compression ratios than existing algorithms such as gzip.
   * - ``certifi``
     - Root certificate authorities. Certifi provides Mozilla's carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while establishing secure connections.
   * - ``click``
     - Library for creating beautiful command-line interfaces. Click is a Python package for creating command-line interfaces with an emphasis on simplicity and ease of use.
   * - ``coverage``
     - Python code coverage measurement tool. Coverage.py measures code coverage during Python test runs, allowing developers to identify areas of code that are not adequately covered by tests.
   * - ``dj-database-url``
     - Tool for loading database parameters from a URL. This package allows Django applications to easily configure database connections using URLs, simplifying deployment and configuration management.
   * - ``entrypoints``
     - Entry point for plugin discovery and automatic configuration. Entrypoints provides a simple interface for discovering and loading plugins in Python applications, enabling automatic configuration and extensibility.
   * - ``iniconfig``
     - INI configuration management for pytest. Iniconfig is a plugin for pytest that allows configuration via INI files, providing an alternative to command-line options and enhancing test configuration flexibility.
   * - ``mccabe``
     - Cyclomatic complexity analyzer for Python. McCabe is a tool for calculating cyclomatic complexity, a metric used to measure the complexity of a program's control flow, aiding in code quality assessment and refactoring.
   * - ``packaging``
     - Packaging utilities for Python. Packaging provides utilities and APIs for Python package management, including creating, distributing, and installing Python packages in various formats.
   * - ``pluggy``
     - Framework for Python plugins. Pluggy is a minimalist framework for managing plugins in Python applications, providing a simple and flexible mechanism for extending application functionality.
   * - ``pycodestyle``
     - Formerly pep8, checks compliance with Python coding conventions. Pycodestyle is a tool for checking Python code against the PEP 8 style guide, helping developers maintain consistent coding styles and improve code readability.
   * - ``pyflakes``
     - Checks for syntax errors, unused variables, etc., in Python programs. Pyflakes is a static analysis tool for detecting common errors in Python code, such as syntax errors, undefined names, and unused variables.
   * - ``pytest``
     - Test framework for Python applications. Pytest is a popular testing framework for Python that supports a wide range of test types and features, including fixtures, parametrization, and plugins.
   * - ``pytest-cov``
     - pytest plugin for measuring code coverage. Pytest-cov is a plugin for pytest that integrates code coverage measurement into test runs, providing insights into the effectiveness of test suites and identifying untested code paths.
   * - ``python-dotenv``
     - Loads environment variables from a .env file. Python-dotenv is a utility for loading environment variables from a .env file into the environment, simplifying configuration management for Python applications.
   * - ``pytz``
     - Python library for manipulating time zones. Pytz provides timezone definitions and utilities for working with time zone information in Python applications, including conversion between different time zones and handling daylight saving time.
   * - ``sqlparse``
     - SQL parser for Python. Sqlparse is a non-validating SQL parser for Python that provides utilities for parsing and formatting SQL queries, enabling analysis and manipulation of SQL code.
   * - ``typing_extensions``
     - Extensions for Python type annotations. Typing_extensions provides additional type hints and utilities for Python's type hinting system, enhancing support for static type checking and improving code readability and maintainability.
   * - ``tzdata``
     - Library for time zone manipulation in Python. Tzdata is a Python library for working with time zone data, providing utilities for accessing and manipulating time zone information, including daylight saving time rules and historical timezone changes.
   * - ``urllib3``
     - HTTP library for Python. Urllib3 is a powerful HTTP client library for Python that provides robust features for making HTTP requests, including connection pooling, SSL/TLS support, and streaming uploads/downloads.
   * - ``uvicorn``
     - ASGI server for deploying asyncio applications. Uvicorn is a lightning-fast ASGI server for Python web applications, designed for deploying asyncio-based applications with optimal performance and scalability.
   * - ``whitenoise``
     - Django middleware for serving static files. Whitenoise is a Django middleware that allows the efficient serving of static files in production environments, improving performance and security.


Structure:
==========

Here, we will detail the project structure.
There are three applications in this project:
1. **Lettings**: Manages Address and Lettings.
2. **oc-_lettings_site**: Contains the settings of the project.
3. **Profile**: Manages Profiles.

Models
------

Address model
~~~~~~~~~~~~~

Represents a physical address.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Attribute (Field)
     - Description
   * - ``number (PositiveIntegerField)``
     - The number part of the address.
   * - ``street (CharField)``
     - The name of the street.
   * - ``city (CharField)``
     - The city.
   * - ``state (CharField)``
     - The state (abbreviated).
   * - ``zip_code (PositiveIntegerField)``
     - The ZIP code.
   * - ``country_iso_code (CharField)``
     - The ISO country code.

Methods:
``__str__``: Returns a string representation of the address.

Meta:
Specifies metadata options for the Address model.

.. list-table:: Meta Attributes
   :widths: 35 40
   :header-rows: 1

   * - Meta Attribute
     - Description
   * - ``verbose_name_plural``
     - The plural name used in the Django admin interface.


Letting model
~~~~~~~~~~~~~

Represents a letting.

.. list-table:: Attributes
   :widths: 30 25
   :header-rows: 1

   * - Attribute (Field)
     - Description
   * - ``title (CharField)``
     - The title of the letting.
   * - ``address (OneToOneField)``
     - The address of the letting.

Methods:
``__str__``: Returns a string representation of the letting.

Meta:
Specifies metadata options for the Letting model.
Same attribute as in the previous model.

Profile model
~~~~~~~~~~~~~

Represents a user profile associated with a Django User.

.. list-table:: Attributes
   :widths: 30 25
   :header-rows: 1

   * - Attribute (Field)
     - Description
   * - ``user (OneToOneField)``
     - The associated User instance.
   * - ``favorite_city (CharField, optional)``
     - The favorite city of the user.

Methods:
``__str__``: Returns a string representation of the profile.

Views
-----

There are four views in this project in total. First, both applications have their index view, built like this:

Index views (for Lettings and Profiles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Retrieves all lettings/profiles from the database and passes them to the template.
   Args:
       request (HttpRequest): HttpRequest object representing the HTTP request.
   Returns:
       HttpResponse: Rendered HTML response.

   **Example**:

.. code-block:: python
  
   def index(request):
       lettings_list = Letting.objects.all()
       context = {"lettings_list": lettings_list}
       return render(request, "lettings/index.html", context)

Letting view
~~~~~~~~~~~~

   Retrieves the letting with the given ID from the database and passes its
   title and address to the template.
   Args:
       request (HttpRequest): HttpRequest object representing the HTTP request.
       letting_id (int): The ID of the letting to display.
   Returns:
       HttpResponse: Rendered HTML response.

   **Code**:

.. code-block:: python

   def letting(request, letting_id):
       letting = Letting.objects.get(id=letting_id)
       context = {
           "title": letting.title,
           "address": letting.address,
       }
       return render(request, "lettings/letting.html", context)

Profile view
~~~~~~~~~~~~

   Retrieves the profile with the given username from the database.
   Args:
        request: HttpRequest object representing the HTTP request.
        username (str): Username of the user whose profile is to be displayed.
   Returns:
       HttpResponse: Rendered HTML response.

   **Code**:

.. code-block:: python

   def profile(request, username):
      profile = Profile.objects.get(user__username=username)
      context = {"profile": profile}
      return render(request, "profiles/profile.html", context)

URLs
----

The URLs of the project are defined in three separate Django applications: oc_lettings_site, lettings, and profiles.

oc_lettings_site URLs
~~~~~~~~~~~~~~~~~~~~~

In the "oc_lettings_site" application:

**Code**:

.. code-block:: python

   from django.urls import path
   from . import views

   app_name = "profiles"

   urlpatterns = [
       path("", views.index, name="profiles_index"),
       path("<str:username>/", views.profile, name="profile"),
   ]

lettings URLs
~~~~~~~~~~~~~

In the "lettings" application:

**Code**:

.. code-block:: python

   from django.urls import path
   from . import views

   app_name = "lettings"

   urlpatterns = [
       path("", views.index, name="lettings_index"),
       path("<int:letting_id>/", views.letting, name="letting"),
   ]

profiles URLs
~~~~~~~~~~~~~

In the "profiles" application:

**Code**:

.. code-block:: python

   from django.urls import path
   from . import views

   app_name = "profiles"

   urlpatterns = [
       path("", views.index, name="profiles_index"),
       path("<str:username>/", views.profile, name="profile"),
   ]


Local Database
==============

The database underwent refactoring using migration files, maintaining the same data objects as before. All existing data remains intact.

As this is a local database, you have the flexibility to experiment with models in any way you prefer. However, 
it's important to note that any changes made here will not reflect on the deployed website, which utilizes a separate database hosted with Render.

To utilize this local database, ensure that the ``DEBUG`` setting is set to ``True`` in your ``settings.py`` file. If it's not already set, you can make this adjustment as follows:

.. code-block:: python

   DEBUG = True

Once you've configured the ``DEBUG`` setting appropriately, you can perform CRUD operations on this database using the Django shell. Simply run the following command:

.. code-block:: shell

   python manage.py shell

Here's an example demonstrating how to create objects in the database:

.. code-block:: python

   address1 = Address.objects.create(
       number=65,
       street="Federal St",
       city="Innsmouth",
       state="MA",
       zip_code=11345,
       country_iso_code="USA",
   )
   letting1 = Letting.objects.create(title="Marsh Office", address=address1)

This example creates an address object and a letting object, linking them together as needed.




