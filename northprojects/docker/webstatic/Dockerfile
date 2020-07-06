FROM python:3.7
LABEL maintainer="support@aldowntown.com"

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

RUN python manage.py collectstatic --settings=northprojects.settings.build --no-input

FROM nginx:alpine

COPY --from=0 /code/static /usr/share/nginx/html/static