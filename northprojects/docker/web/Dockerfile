FROM python:3.7
LABEL maintainer="support@aldowntown.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV prod
ENV DJANGO_SETTINGS_MODULE northprojects.settings.production 

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn psycopg2-binary

COPY . /code/
WORKDIR /code/

ENV DJANGO_SECRET_KEY tmp
RUN python manage.py collectstatic --settings=northprojects.settings.build --no-input
RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec gunicorn northprojects.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level "info"
