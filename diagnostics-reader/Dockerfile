FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:main

ENV SERVICE_NAME diagnostics-reader
WORKDIR /app

ADD main.py .
ADD Database.py .

EXPOSE 80

CMD ["python", "main.py"]