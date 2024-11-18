import configparser
import os
import smtplib

from twilio.rest import Client

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]


# Using a config.ini file to retrieve the phone numbers and tokens.


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (config.ini file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"],
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}',
        )
        print(message.sid)

    def notify_users(self, flight, users):
        for user in users:
            receiver = f"{user['firstName']} {user['lastName']} <{user['email']}>"
            message = (
                f"Subject: Low Price Alert from {config.SENDER_NAME}\nTo: {receiver}\nFrom: {self.sender}\n\n"
                f"Low Price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                f" to {flight.destination_city}-{flight.destination_airport}, "
                f"from {flight.leave_date} to {flight.return_date}.\n\n"
                f"https://www.google.co.uk/flights?hl=en#flt="
                f"{flight.origin_airport}.{flight.destination_airport}.{flight.leave_date}*"
                f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
            )
            self.send_email(self.sender, receiver, message)

    def send_email(self, sender, receiver, message):
        try:
            with smtplib.SMTP(self.server, self.port) as server:
                server.starttls()
                server.login(config.SMTP_LOGIN, config.SMTP_PASS)
                server.sendmail(sender, receiver, message)
        except smtplib.SMTPServerDisconnected:
            print(
                "ERROR: Could not connect to the SMTP server. "
                "Make sure the SMTP_LOGIN and SMTP_PASS credentials have been set correctly."
            )
        except smtplib.SMTPDataError:
            # in case too many emails are being sent in a short time
            # handling this properly is really not in the scope of this project
            print(
                f"ERROR: Too many emails per second. The message to {receiver} was not sent."
            )
        else:
            # just to have some feedback
            print(f"The message to {receiver} was sent.")
