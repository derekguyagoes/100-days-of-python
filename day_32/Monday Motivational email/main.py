import smtplib
import random
import datetime as dt

my_email = "blahblah@what.com"
password = "password"
MONDAY = 0  # how datetime.weekday sees monday.


def send_email(send=False, sending=""):
    if send:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="there.what.com",
                msg="Subject:Hello\n\nwhere does a body lie?",
            )
    else:
        print(f"Sending this quote: {sending} ")


def get_quote():
    with open("quotes.txt", "r") as quotes:
        random_quote = random.choice(quotes.readlines())
        return random_quote


today = dt.datetime.now().weekday()
if today == MONDAY:
    quote = get_quote()
    send_email(sending=quote)
