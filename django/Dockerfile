FROM python:3.12-bookworm

ARG DJANGO_SUPERUSER_NAME
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_EMAIL

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD https://github.com/tateishi/test-django-hello.git app

WORKDIR /code/app/hello

RUN python manage.py migrate
RUN python manage.py createsuperuser \
    --username ${DJANGO_SUPERUSER_NAME} \
    --email ${DJANGO_SUPERUSER_EMAIL} \
    --no-input
RUN python manage.py collectstatic

CMD uvicorn hello.asgi:application --host 0.0.0.0 --port 8000
