FROM python:3.12-bookworm

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN django-admin startproject hello

COPY settings_ex.py .
RUN cat settings_ex.py >> hello/hello/settings.py

WORKDIR /code/hello
RUN python manage.py collectstatic

CMD uvicorn hello.asgi:application --host 0.0.0.0 --port 8000
