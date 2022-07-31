FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:taza

ENV SERVICE_NAME exam-microservice
WORKDIR /app

ADD main.py .
COPY dashboard/* ./dashboard/

EXPOSE 80

CMD ["python", "main.py"]