======
Index
======

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

Contents
--------

.. toctree::

   architecture
   quality
   deployement

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
   - `oc_lettings_site`: Contains site configuration.
   - `lettings`: Contains Address and Lettings models.
   - `profile`: Dedicated to the Profile model.
2. **Unit Testing Implementation**: Nine unit tests were implemented across the applications, achieving a total test coverage of 83%. These tests can be executed using the following command:
    ``pytest -v`` or ``pytest --cov=.``, to view the test coverage percentage.

3. **Addition of Docstrings**: Docstrings were added to each function to enhance code maintainability and facilitate contribution. 
    For example:
    .. code-block:: python
      def __str__(self):
          """
          Returns a string representation of the profile.
          """
          return self.user.username

The  inclusion of docstrings provides clear descriptions of the function's purpose and usage.

