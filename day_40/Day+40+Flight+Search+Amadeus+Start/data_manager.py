import configparser
import requests
from requests.auth import HTTPBasicAuth

# Load environment variables from config.ini file

config = configparser.ConfigParser()
config.read("config.ini")
sheet_prices = config["DEFAULT"]["SHEETY_PRICES_ENDPOINT"]

SHEETY_PRICES_ENDPOINT = sheet_prices


class DataManager:

    def __init__(self):
        self._user = config["DEFAULT"]["SHEETY_USRERNAME"]
        self._password = config["DEFAULT"]["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)

    def add_user(self, first_name, last_name, email):
        """Takes the user's details as STRs and add them to the worksheet."""
        body = {
            "user": {"firstName": first_name, "lastName": last_name, "email": email}
        }
        response = requests.post(
            url=self.worksheet_url, json=body, headers=self.headers
        )
        # also just raise an error
        response.raise_for_status()
        # also to have some feedback
        print(
            f'User {first_name} {last_name} has been added to the "{self.worksheet_name}" worksheet.'
        )
