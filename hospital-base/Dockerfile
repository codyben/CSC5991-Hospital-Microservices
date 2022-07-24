FROM python:3

WORKDIR /app

ADD HospitalExceptions.py .

ENV CONTAINER TRUE

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
