FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:develop-cody

ENV SERVICE_NAME doctor-reader
WORKDIR /app

ADD main.py .
ADD Database.py .

EXPOSE 80

CMD ["python", "main.py"]