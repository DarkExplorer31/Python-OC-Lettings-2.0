=========
Structure
=========

Dependences
===========

This section details the dependencies used in the project and explains their role and importance.

Main Dependencies:
------------------

Here, we will detail the dependencies used in the project and explain their functionalities.
Here is the complete requirements.txt:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Package
     - Description
   * - ``asgiref``
     - Library for Django web servers.
   * - ``Brotli``
     - Compression library.
   * - ``certifi``
     - Root certificate authorities.
   * - ``click``
     - Library for creating beautiful command-line interfaces.
   * - ``coverage``
     - Python code coverage measurement tool.
   * - ``dj-database-url``
     - Tool for loading database parameters from a URL.
   * - ``entrypoints``
     - Entry point for plugin discovery and automatic configuration.
   * - ``iniconfig``
     - INI configuration management for pytest.
   * - ``mccabe``
     - Cyclomatic complexity analyzer for Python.
   * - ``packaging``
     - Packaging utilities for Python.
   * - ``pluggy``
     - Framework for Python plugins.
   * - ``pycodestyle``
     - Formerly pep8, checks compliance with Python coding conventions.
   * - ``pyflakes``
     - Checks for syntax errors, unused variables, etc., in Python programs.
   * - ``pytest``
     - Test framework for Python applications.
   * - ``pytest-cov``
     - pytest plugin for measuring code coverage.
   * - ``python-dotenv``
     - Loads environment variables from a .env file.
   * - ``pytz``
     - Python library for manipulating time zones.
   * - ``sqlparse``
     - SQL parser for Python.
   * - ``typing_extensions``
     - Extensions for Python type annotations.
   * - ``tzdata``
     - Library for time zone manipulation in Python.
   * - ``urllib3``
     - HTTP library for Python.
   * - ``uvicorn``
     - ASGI server for deploying asyncio applications.
   * - ``whitenoise``
     - Django middleware for serving static files.
     
Structure:
==========

Here, we will detail the project structure.

Models
------

Trois modèles sont implémentés:

**Address model**: Represents a physical address.
   Attributes:
      ``number (PositiveIntegerField)``: The number part of the address.
      ``street (CharField)``: The name of the street.
      ``city (CharField)``: The city.
      ``state (CharField)``: The state (abbreviated).
      ``zip_code (PositiveIntegerField)``: The ZIP code.
      ``country_iso_code (CharField)``: The ISO country code.
   Methods:
       __str__: Returns a string representation of the address.
   Meta:
       Specifies metadata options for the Address model.
   Meta Attributes:
       verbose_name_plural (str): The plural name used in the Django admin interface.

**Letting model**: Represents a letting (e.g., property for rent).
   Attributes:
      ``title (CharField)``: The title of the letting.
      ``address (OneToOneField)``: The address of the letting.

   Methods:
       __str__: Returns a string representation of the letting.

   Meta:
       Specifies metadata options for the Letting model.

   Meta Attributes:
       verbose_name_plural (str): The plural name used in the Django admin interface.

**Profile model**: Represents a user profile associated with a Django User.
   Attributes:
      ``user (OneToOneField)``: The associated User instance.
      ``favorite_city (CharField, optional)``: The favorite city of the user.

   Methods:
       __str__: Returns a string representation of the profile.

   Meta:
       verbose_name_plural (str): The plural name used in the Django admin interface.

Views
-----

URLs
----

Local Database
==============