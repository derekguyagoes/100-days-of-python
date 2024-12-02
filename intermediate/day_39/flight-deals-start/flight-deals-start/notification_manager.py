import configparser

from twilio.rest import Client

config = configparser.ConfigParser()
config.read("config.ini")
kiwi_key = config["DEFAULT"]["twilio_sid"]
kiwi_key = config["DEFAULT"]["twilio_token"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(config.twilio_sid, config.twilio_token)

    def send_sms(self, flight):
        message = (
            f"Low Price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
            f"to {flight.destination_city}-{flight.destination_airport}, "
            f"from {flight.leave_date} to {flight.return_date}."
        )

        print("Sent! I promise!")
        print(message)
