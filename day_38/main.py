import datetime

import requests
import configparser

GENDER = "male"
WEIGHT_KG = 172
HEIGHT_CM = 152
AGE = 25

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]
appId = config["DEFAULT"]["appId"]


def send_to_sheety(data):
    to_send = {"workout": data}
    url = "https://api.sheety.co/003a78b079c17374e27750b7f1c46cc4/tracking/workouts"
    res = ""  # requests.post(url, json=to_send)
    print(res)


def extract_data(response):
    today = datetime.datetime.now()
    obj = response["exercises"][0]
    cat = {
        "date": today,
        "time": today.hour,
        "exercise": obj["name"] or "missing name",
        "duration": obj["duration_min"] or 0,
        "calories": obj["nf_calories"] or 0,
    }
    send_to_sheety(cat)


DOMAIN_URL = "https://trackapi.nutritionix.com"
EXERCISE_ROUTE = "/v2/natural/exercise"

AUTH_HEADERS = {"x-app-id": appId, "x-app-key": key}

params = {
    "query": "i bike for 30 minutes today",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(DOMAIN_URL + EXERCISE_ROUTE, json=params, headers=AUTH_HEADERS)
print(response.text)
extract_data(response.json())
