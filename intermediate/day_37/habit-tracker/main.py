import requests
import configparser
from datetime import datetime

GRAPH_ID = "graph1"

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]
USERNAME = config["DEFAULT"]["username"]

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


def setup_user_account():
    user_params = {
        "token": key,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    # sets up user account
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_config = {
        "id": f"{GRAPH_ID}",
        "name": "Tracking Graph",
        "unit": "Minute",
        "type": "int",
        "color": "shibafu",
    }
    headers = {
        "X-USER-TOKEN": key,
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_entry_in_graph():
    today = datetime.now()
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {"date": today.strftime("%Y%m%d"), "quantity": "50"}
    headers = {
        "X-USER-TOKEN": key,
    }

    response = requests.post(url=graph_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def update_entry_in_graph(date_to_update, quantity):
    date = date_to_update.strftime("%Y%m%d")
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    pixel_data = {"quantity": str(quantity)}
    headers = {
        "X-USER-TOKEN": key,
    }

    response = requests.put(url=graph_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def delete_entry_from_graph(date_to_update):
    date = date_to_update.strftime("%Y%m%d")
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    headers = {
        "X-USER-TOKEN": key,
    }

    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)


# setup_user_account()
# create_graph()
# create_entry_in_graph()


data_to_update = datetime(2024, 9, 30)
update_entry_in_graph(data_to_update, quantity=3)
