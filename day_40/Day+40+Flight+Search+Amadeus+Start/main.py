import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "SLC"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if (
            cheapest_flight.price != "N/A"
            and cheapest_flight.price < destination["lowestPrice"]
    ):
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )


def add_new_user():
    """Adds a new user to the spreadsheet."""
    print("Welcome to the Flight Club.\nWe find the best flight deals and email you.")
    print("What is your first name?")
    first_name = get_name()
    print("What is your last name?")
    last_name = get_name()
    while True:
        print("What is your email?")
        email = get_email()
        print("Enter your email again.")
        email_check = get_email()
        if email == email_check:
            break
        print("The entered emails do not match.\nPlease try again.")
    # add the user
    users.add_user(first_name=first_name, last_name=last_name, email=email)
    print(
        "Success!\nYour email has been added. You will receive notifications of cheap flights soon!"
    )


def get_name():
    """Asks the user to input a name and returns it as a STR."""
    # the names might or might be from the Simpsons, some of the less naughty ones anyway
    # from https://simpsons.fandom.com/wiki/Bart%27s_prank_calls
    while True:
        name = input("> ")
        # make sure something was entered
        if name == "":
            print("Please enter a name.")
        else:
            return name


def get_email():
    """Asks the user to input an email address and returns it as a STR."""
    while True:
        email = input("> ")
        # make sure something was entered
        if email == "":
            print("Please enter an email address.")
        # check that it looks like an email address
        # just a simple validation, without using regular expressions
        elif email.find("@") == -1 or email.find(".") == -1:
            print("Please enter a valid email address.")
        else:
            return email


prices = data_manager.DataManager("prices")
users = data_manager.DataManager("users")
flight_search = flight_search.FlightSearch()
notification_manager = notification_manager.NotificationManager()

prices_sheet = prices.get_sheet()
users_sheet = users.get_sheet()

# just for some basic interaction
print('Enter "y" if you want to add a new user.')
choice = input("> ").lower()
if choice == "y":
    add_new_user()

# add missing codes
for city in prices_sheet:
    if city["iataCode"] == "":
        query_result = flight_search.find_city_code(city["city"])
        city["iataCode"] = query_result[0]["code"]
        # update the row in the spreadsheet
        prices.update_code(city)

# look for flights
for city in prices_sheet:
    # using the default time zone
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    in_six_months = today + timedelta(days=(6 * 30))
    # get a flight object with the details
    flight = flight_search.find_flights(
        origin=ORIGIN_CITY_IATA,
        destination=city["iataCode"],
        date_from=tomorrow.strftime("%d/%m/%Y"),
        date_to=in_six_months.strftime("%d/%m/%Y"),
    )
