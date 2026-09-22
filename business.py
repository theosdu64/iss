import requests
from datetime import datetime


def call_api(methode, url):
    try:
        response = requests.request(methode, url, timeout=10)
        return response.json()
    except requests.RequestException as e:
        return f"Call api Error {e}"


def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


def iss_position():
    data = call_api("GET", "http://api.open-notify.org/iss-now.json")

    if data:
        formatted_data = {
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"],
            "timestamp": format_timestamp(data["timestamp"]),
        }
    else:
        return "No data"
    return formatted_data

def astronauts_position():
    data = call_api("GET", "http://api.open-notify.org/astros.json")

    if data:
        astronauts = []
        astronauts_length = len(data["people"])

        astronauts.append(
            f"nombre : {astronauts_length}")

        for i in data["people"]:
            astronauts.append({
                "name": i["name"]
            })

        return astronauts
    else:
        return "No data"

