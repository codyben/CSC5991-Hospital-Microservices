FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:develop-cody

ENV SERVICE_NAME diagnostics-microservice
WORKDIR /app

ADD main.py .
COPY dashboard/* ./dashboard/

EXPOSE 80

CMD ["python", "main.py"]