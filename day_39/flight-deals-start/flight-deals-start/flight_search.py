import configparser

import requests
import flight_data as data

KIWI_API_URL = "http://tequila-api.kiwi.com"
LOCALE = "en-US"
NIGHTS_FROM = 5
NIGHTS_TO = 21
CURRENCY = "USD"
MAX_STOPOVERS = 0

config = configparser.ConfigParser()
config.read("config.ini")
kiwi_key = config["DEFAULT"]["kiwi_key"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_url = KIWI_API_URL
        self.locale = LOCALE
        self.headers = {"apiKey": kiwi_key}

    def find_city_code(self, name):
        query = f"{self.api_url}/locations/query"
        params = {
            "term": name,
            "locale": self.locale,
            "types": "city",
            "active_only": True,
        }

        response = requests.get(url=query, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"]

    def find_flights(self, origin, destination, date_from, date_to):
        """Takes flight details as STRs and returns a flight_data object."""
        search_url = f"{self.api_url}/v2/search"
        params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": NIGHTS_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "flight_type": "round",
            "curr": CURRENCY,
            "one_for_city": 1,
            "max_stopovers": MAX_STOPOVERS,
        }
        response = requests.get(url=search_url, params=params, headers=self.headers)
        # also just raise an error, this will returns a "HTTPError" if credentials are not set properly
        response.raise_for_status()
        # only use the first result, if any
        data = response.json()["data"][0]
        flight = data.FlightData(
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            leave_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            price=data["price"],
        )

        return flight
