FROM python:3

WORKDIR /app

ADD HospitalExceptions.py .
ADD PatientModel.py .

ENV CONTAINER TRUE

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
RUN pip install requests
RUN pip install mysql-connector-python