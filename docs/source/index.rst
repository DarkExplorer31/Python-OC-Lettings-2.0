============
Introduction
============

Welcome to the documentation of DarkExplorer31-Python-OC-Lettings-2.0!

This project aims to refactor the original code into three distinct applications, using Django as the main framework. Our goal is to improve code maintainability, security, and quality, while also simplifying project deployment and management.

We have also implemented a comprehensive CI/CD pipeline to automate testing, quality controls, and continuous deployment of the project.

.. seealso::
    original GitHub Repository: `original repository <https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR>`__

The result is accompanied by unit tests, the establishment of a CI/CD pipeline, culminating in the deployment of the project to a public URL.

.. seealso::
    Deployed website: `website <https://oc-lettings-2-0.onrender.com>`__

.. warning::
    Deployed on Render with a free instance. The first time you visit this address, the website may take some time to load.


===========
Refactoring
===========

The refactoring most important points is defined by:

Before Intervention:
====================

1. **Single Application Structure**: Initially, the project was organized within a single application named `oc_letting_site`.
This application contained all the defined models for the site, including Address, Lettings, and Profile.
2. **Lack of Testing**: No unit tests were implemented in the application.
3. **Absence of Internal Documentation**: The application lacked internal documentation such as docstrings or comments.

After Intervention:
===================

1. **Refactored Application Structure**: Following the refactoring process, the project was divided into three applications:
   - `oc-lettings`: Contains site configuration.
   - `lettings`: Contains Address and Lettings models.
   - `profile`: Dedicated to the Profile model.
2. **Unit Testing Implementation**: Nine unit tests were implemented across the applications, achieving a total test coverage of 83%. These tests can be executed using the following command:
    ``pytest -v`` or ``pytest --cov=.``, to view the test coverage percentage.

3. **Addition of Docstrings**: Docstrings were added to each function to enhance code maintainability and facilitate contribution. 
    For example:
    .. autoclass:: 
      def __str__(self):
          """
          Returns a string representation of the profile.
          """
          return self.user.username

The  inclusion of docstrings provides clear descriptions of the function's purpose and usage.

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

``asgiref``: Library for Django web servers.
``Brotli``: Compression library.
``certifi``: Root certificate authorities.
``click``: Library for creating beautiful command-line interfaces.
``coverage``: Python code coverage measurement tool.
``dj-database-url``: Tool for loading database parameters from a URL.
``entrypoints``: Entry point for plugin discovery and automatic configuration.
``iniconfig``: INI configuration management for pytest.
``mccabe``: Cyclomatic complexity analyzer for Python.
``packaging``: Packaging utilities for Python.
``pluggy``: Framework for Python plugins.
``pycodestyle``: Formerly pep8, checks compliance with Python coding conventions.
``pyflakes``: Checks for syntax errors, unused variables, etc., in Python programs.
``pytest``: Test framework for Python applications.
``pytest-cov``: pytest plugin for measuring code coverage.
``python-dotenv``: Loads environment variables from a .env file.
``pytz``: Python library for manipulating time zones.
``sqlparse``: SQL parser for Python.
``typing_extensions``: Extensions for Python type annotations.
``tzdata``: Library for time zone manipulation in Python.
``urllib3``: HTTP library for Python.
``uvicorn``: ASGI server for deploying asyncio applications.
``whitenoise``: Django middleware for serving static files.

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