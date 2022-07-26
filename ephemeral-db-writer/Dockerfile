FROM ghcr.io/codyben/csc5991-hospital-microservices/hospital-base:develop-cody

ENV SERVICE_NAME ephemeral-db-writer
WORKDIR /app

ADD entrypoint.sh .
COPY *.py .


CMD ["bash", "entrypoint.sh"]