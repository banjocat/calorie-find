FROM postgres:9

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./extensions.sql /docker-entrypoint-initdb.d/extensions.sql

