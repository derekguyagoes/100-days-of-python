import datetime as dt

import data_manager as dm
import flight_search as fs
import notification_manager as nm

ORIGIN_CODE = "SLC"

data_manager = dm.DataManager()
flight_search = fs.FlightSearch()
notification_manager = nm.NotificationManager()

sheet = data_manager.get_sheets()

for city in sheet:
    if city["iataCode"] == "":
        query = flight_search.find_city_code(city["city"])
        city["iataCode"] = query[0]["code"]
        data_manager.update_entry(city)

for city in sheet:
    today = dt.datetime.now()
    tomorrow = today + dt.timedelta(days=1)
    in_six_months = today + dt.timedelta(days=(6 * 30))
    flight = flight_search.find_flights(
        origin=ORIGIN_CODE,
        destination=city["iataCode"],
        date_from=tomorrow.strftime("%d/%m/%Y"),
        date_to=in_six_months.strftime("%d/%m/%Y"),
    )

    if flight.price <= city["lowestPrice"]:
        notification_manager.send_sms(flight)
