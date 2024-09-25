import json

import requests
import datetime as dt
import configparser

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]


def get_stock_difference_percent():
    url = (
        f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={key}"
    )
    r = requests.get(url)

    if "Thank you for using Alpha Vantage!" not in r.text:
        data = r.json()
        yesterday = (dt.date.today() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
        day_before_yesterdays = (dt.date.today() - dt.timedelta(days=2)).strftime(
            "%Y-%m-%d"
        )
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
        yesterday = "2024-09-25"
        day_before_yesterdays = "2024-09-24"

    yesterdays_closing = eval(data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_yesterdays_closing = eval(
        data["Time Series (Daily)"][day_before_yesterdays]["4. close"]
    )
    percent = round(
        (
                abs(yesterdays_closing - day_before_yesterdays_closing)
                / day_before_yesterdays_closing
        )
        * 100.0
    )

    return percent


def get_news():
    return "get news"


percent = get_stock_difference_percent()
if percent > 5:
    print(get_news())

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
