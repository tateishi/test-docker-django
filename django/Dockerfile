FROM python:3.12-bookworm

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD https://github.com/tateishi/test-django-hello.git app

WORKDIR /code/app/hello
RUN python manage.py collectstatic

CMD uvicorn hello.asgi:application --host 0.0.0.0 --port 8000
