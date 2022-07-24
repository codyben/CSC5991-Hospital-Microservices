# Cody Benkoski
# hk2327@wayne.edu
import random, time
from flask import Flask, request
from functools import wraps
import requests, os
from Database import Database
app = Flask(__name__)


@app.route('/patient', methods=['GET'])
def get_all_patients():
    pass

@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id:int):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 if os.environ.get("CONTAINER", False) else 5000)
