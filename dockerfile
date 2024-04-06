FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY load_env.sh /app/
RUN chmod +x /app/load_env.sh

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2", "oc_lettings_site.wsgi:application"]
