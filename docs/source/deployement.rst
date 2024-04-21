Deployment settings
===================

CI/CD Pipeline
--------------

The CI/CD pipeline has been instantiated in a file called ``django.yml``, located in the ``.github\workflows\`` directory.
It consists of four parts:

**Build**: This stage compiles the project for the first time.
**Test**:  This stage executes the nine unit tests of the application.
**Code_quality**: This stage checks adherence to coding quality rules using Flake8.
**Deploy**: This stage deploys the site including the pushed modifications. Please note that this stage only deploys upon commits to the master branch.

.. seealso::
    GitHub actions: `website <https://docs.github.com/fr/actions>`__

Docker
------

The entire project has been pushed to Docker Hub in its local version, while retaining all the parameters for deployment.
To clone the project locally:

``>>> docker pull darkmessiah31/oc-lettings:latest``
``>>> docker run -it -d -p 8000:8000 darkmessiah31/oc-lettings``

Now you can try it here: ``http://localhost:8000``

.. seealso::
    Published image: `website <https://hub.docker.com/repository/docker/darkmessiah31/oc-lettings/general>`__

Online Database
---------------

The online database is deployed via Render. It is built using PostgreSQL. I won't provide the admin, but the data is completely different between the local database and this one.
To create data, you can simply:

- **Check DEBUG setting**: Make sure that ``DEBUG`` is set to ``False``.
- **Enter the Shell**: Access the Django shell using the command: ``python manage.py shell``.
- **Import the model**: Import the model for which you want to create an object: ``from lettings.models import Address``.
- **Create the object**:

.. code-block:: shell
    
    adresse1 = Address.objects.create(number=9, street="a street", city="City", state="USA"...)


