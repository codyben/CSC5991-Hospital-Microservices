FROM mysql:8.0.29

WORKDIR /docker-entrypoint-initdb.d

ADD db.sql .
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE HospitalServices
