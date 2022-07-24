FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:develop-cody

ENV SERVICE_NAME doctor-microservice
WORKDIR /app

ADD main.py .

EXPOSE 80

CMD ["python", "main.py"]