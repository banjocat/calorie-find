FROM python:3.6-slim

RUN pip install django==1.9.7
RUN pip install django-extensions
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
RUN pip install django-rest-swagger

RUN mkdir -p /opt/api/
COPY ./calorie_find /opt/api
WORKDIR /opt/api/

