# OC-Lettings 2.0

Welcome to the OC-Lettings 2.0 project! This repository contains the restructured source code for the Orange County Lettings website.

![deployed-on-Render](/badges/deployed-on-render.svg),
![built-with-Django](/badges/build-with-django.svg),
![using-sentry](/badges/using-sentry.svg),
![contenering-in-docker](/badges/contenering-in-docker.svg),

See the website deployed [here](https://oc-lettings-2-0.onrender.com).

See the complete documentation[here](https://python-oc-lettings-20.readthedocs.io/en/latest/index.html).

Deployed on Render with a free instance. The first time you visit this address, the website may take some time to load.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [Database](#database)
- [Docker](#docker)

## Prerequisites

- GitHub Account
- Git CLI
- SQLite3 CLI
- Python, version 3.6 or higher
- Docker Account (if you want to pull the Docker image)
- Sentry Account
- Render Account

Make sure you have access to the following environment variables:
- SECRET_KEY: the secret key from Django app
- SENTRY_DSN: the link to Sentry
- DB_HOSTNAME: the Hostname for the distant database
- DB_PASSWORD: The password for the distant database
- RENDER_DEPLOY_URL: The secret Render deploy hook.

In the rest of the documentation for local development, it is assumed that the `python` command in your OS shell runs the Python interpreter above (unless a virtual environment is activated).

## Contributing

### Clone the Repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/DarkExplorer31/Python-OC-Lettings-2.0`

### Create Environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv env`
- Activate the virtual environment with the following command: `source env/bin/activate` or `env\Scripts\activate` ( with PowerShell )
- Confirm the Python version is 3.6 or higher by running: `python --version`
- To deactivate the environment, simply use: `deactivate

### Run website

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a web browser.

### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source env/bin/activate` or `env\Scripts\activate` ( with PowerShell )
- `flake8`

### Unit tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate` or `env\Scripts\activate` ( with PowerShell )
- `pytest -v` or `pytest --cov=.` ( if you want to see the coverage, currently at 83% )

### Admin Panel

- Navigate to: `http://localhost:8000/admin`
- Sign in with the following credentials: 
  - Username: `admin`
  - Password: `Abc1234!`
[Back to table of content](#table-of-contents)

## Databases

### Local Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a PowerShell session: `sqlite3`
- Connect to the database: `.open oc-lettings-site.sqlite3`
- Show tables in the database: `.tables`
- Show columns in the profile table: `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query in the profile table: `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- Use `.quit` to exit.

### Distant Database

The distant database was created with PostgreSQL, exclusively online, on the Render website.
It was named: `oc_lettings_site_vaog`.
To add data to it:
- Run this command: `python manage.py shell`
- Import the model: `from letting.models import Address`
- Create a new model: `address1 = Address.objects.create(...)`
- To exit the Django shell, simply use: `exit()`
[Back to table of content](#table-of-contents)

## Docker

You can find the Docker image for this project on [Docker Hub](https://hub.docker.com/repository/docker/darkmessiah31/oc-lettings/general).

To install Docker, follow the instructions [here](https://docs.docker.com/engine/install/).

### Use this image

-Clone the image: `docker pull darkmessiah31/oc-lettings:latest`
-Run the image: `docker run darkmessiah31/oc-lettings:latest`
-Now you can access the application locally by navigating to [http://localhost:8000](http://localhost:8000).

**Note:** Please be aware that the data in this image is from a SQLite3 database, so it may differ from the data in the deployed website.
[Back to table of content](#table-of-contents)