FROM python:2

RUN pip install django==1.9.7
RUN pip install django-extensions
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
RUN pip install django-rest-swagger==0.3.10

# for postgres
RUN pip install psycopg2

RUN mkdir -p /opt/api/
COPY ./calorie_find /opt/api
WORKDIR /opt/api/
COPY ./wait-for-it.sh /tmp/.

