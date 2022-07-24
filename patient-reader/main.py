# Cody Benkoski
# hk2327@wayne.edu
import random, time
from flask import Flask, request
from functools import wraps
import requests, os, socket
from Database import Database
app = Flask(__name__)
random.seed(5991)

database = Database()



# This is pretty nice, so borrowing it instead of rolling my own.
# https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    return sorted(output)

def notify_gateway():
    response = requests.post("http://hospital-reader-gateway.local/discover", headers={
        "Content-Type": "application/json"
    }, json = {
        "name": os.environ['SERVICE_NAME'],
        "hostname": socket.getfqdn(),
        "endpoints": list_routes()
    })
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"Exception on notifying gateway: {str(e)}")
        return
    print("Successfully notified gateway!")
    print(f"Response: {response.json()}")



@app.route('/patient', methods=['GET'])
def get_all_patients():
    def query(cursor):
        cursor.execute("SELECT * FROM Patient_info")
    result = database.transaction(query)
    return {
        "success": True,
        "data": [database.parse(r) for r in result]
    }


@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient_by_id(patient_id:int):
    def query(cursor):
        cursor.execute("SELECT * FROM Patient_info WHERE patientID = %d", (patient_id,))
    result = database.transaction(query)
    parsed = database.parse(result)
    if parsed:
        return {
            "success": True,
            "data": parsed
        }
    else:
        return {
            "success": False,
            "data": None
        }, 404


if __name__ == '__main__':
    notify_gateway()
    app.run(host='0.0.0.0', port=80 if os.environ.get("CONTAINER", False) else 5000)
