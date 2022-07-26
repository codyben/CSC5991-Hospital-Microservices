# Cody Benkoski
# hk2327@wayne.edu
import random, time
from flask import Flask, request
from functools import wraps
import requests, os
app = Flask(__name__)
random.seed(5991)
SERVICES = {
    "sanity-test": "sanity.local"
}
SERVICE_ENDPOINTS = {
    "sanity-test": {}
}

def restrict_to_readers(request):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            vlan = request.remote_addr.split(".")[2]
            if vlan != "0":
                return (
                    {"success": False},
                    403,
                )
        return wrapped
    return decorator

def validate_service(service):
    name = service.get("name")
    hostname = service.get("hostname")

    name_ok = name and (name not in SERVICES.keys())
    hostname_ok = hostname and (hostname not in SERVICES.values())
    new_service = name_ok and hostname_ok
    if not new_service:
        return (
                {"success": False},
                409,
            )
    else:
        SERVICES[name] = hostname
        SERVICE_ENDPOINTS[name] = service.get("endpoints", dict())
    return (
        {
            "success": True,
            "data": {
                    "service": name,
                    "hostname": SERVICES[name],
                    "endpoints": SERVICE_ENDPOINTS[name]
            }
        },
        201,
    )


@restrict_to_readers
@app.route('/discover', methods=['POST'])
def add_service():
    try:
        data = request.get_json()
    except Exception:
        return (
            {"success": False},
            400,
        )
    return validate_service(data)
    
@app.route('/find', methods=['GET'])
def find_services():
    output = []
    for service in SERVICES.keys():
        output.append(
            {
                "service": service,
                "endpoints": SERVICE_ENDPOINTS.get(service),
                "fqdn": SERVICES.get(service)
            }
        )
    return (
        {
            "success": True,
            "data": output
        },
        200
    )

@app.route('/find/<service>', methods=['GET'])
def find_service(service: str):
    service = SERVICES.get(service)
    if not service:
        return (
            {
                "success": False,
                "data": None
            },
            404,
        )
    else:
        return (
            {
                "success": True,
                "data": {
                    "service": service,
                    "endpoints": SERVICE_ENDPOINTS.get(service),
                    "fqdn": SERVICES.get(service)
                }
            },
            200,
        )

@app.route('/proxy/<service>/<path:path>', methods=['GET'])
def proxy_to_reader(service:str, path):
    service = SERVICES.get(service)
    if not service:
        return (
            {
                "success": False,
                "data": None
            },
            404,
        )
    else:
        print(path)
        path_str = str(path)
        try:
            response = requests.get(f"http://{service}/{str(path)}")
        except requests.exceptions.ConnectionError:
            return (
            {
                "success": False,
                "data": {
                    "service": service,
                    "endpoint": path_str
                }
            },
            503,
        ) 
        except:
            return (
            {
                "success": False,
                "data": {
                    "service": service,
                    "endpoint": path_str
                }
            },
            500,
        )

        try:
            response.raise_for_status()
            data = response.json()
        except:
            return (
            {
                "success": False,
                "data": {
                    "service": service,
                    "endpoint": path_str
                }
            },
            500,
        )
        return (
            {
                "success": True,
                "data": data
            },
            200,
        ) 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 if os.environ.get("CONTAINER", False) else 5000)
