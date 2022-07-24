# Cody Benkoski
# hk2327@wayne.edu
import random, time
from flask import Flask, request
import requests, os, socket
from constants import GATEWAY_FQDN
app = Flask(__name__)
random.seed(5991)



@app.route('/dashboard', methods=['GET'])
def return_dashboard():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 if os.environ.get("CONTAINER", False) else 5000)
