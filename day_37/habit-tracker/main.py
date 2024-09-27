import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]

# curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": key,
    "username": "derguy",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
