import configparser

import requests

SHEETY_API_URL = "https://api.sheety.co"

config = configparser.ConfigParser()
config.read("config.ini")
sheet_url = config["DEFAULT"]["SHEET_URL"]
sheet_token = config["DEFAULT"]["SHEETY_TOKEN"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_url = SHEETY_API_URL + sheet_url
        self.headers = {"Authorization": f"Bearer {sheet_token}"}

    def get_sheets(self):
        response = requests.get(self.sheet_url, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_entry(self, entry):
        edit_url = f"{self.sheet_url}/{entry['id']}"
        body = {
            "price": {
                "iataCode": entry["iataCode"],
            }
        }
        response = requests.put(url=edit_url, json=body, headers=self.headers)
        response.raise_for_status()
