FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:develop-cody

ENV SERVICE_NAME nurse-reader
WORKDIR /app

ADD main.py .
ADD Database.py .
ADD NurseModel.py .

EXPOSE 80

CMD ["python", "main.py"]