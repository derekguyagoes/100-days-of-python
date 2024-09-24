import requests

# https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=113cd993a406a4382f9a012fca93100b
api_key = "113cd993a406a4382f9a012fca93100b"
lat = 40.569710
lon = -111.897278
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {"lat": lat, "lon": lon, "appid": api_key, "cnt": 4}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


# can send through email or twillio
def send_comms():
    print("umbrella")


if will_rain:
    send_comms()
