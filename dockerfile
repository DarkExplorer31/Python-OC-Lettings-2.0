FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
