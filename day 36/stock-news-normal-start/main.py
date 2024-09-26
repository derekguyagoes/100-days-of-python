import json

import requests
import datetime as dt
import configparser

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY_SEARCH_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

config = configparser.ConfigParser()
config.read("config.ini")
key = config["DEFAULT"]["key"]
news_api = config["DEFAULT"]["news_api"]


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
    url = f"{NEWS_ENDPOINT}?q={COMPANY_SEARCH_NAME}&apiKey={news_api}"
    response = requests.get(url)
    data = response.json()
    three = data["articles"][:3]

    three_articles = {index["title"]: index["content"] for index in three}
    return three_articles


def send_messages(news, percent):
    for key in news:
        message = f"""{STOCK_ENDPOINT}: {percent}%\n
                    Headline: {key}\n
                    Brief: {news[key][:90]}\n                    
                    """
        print(message)


percent = get_stock_difference_percent()
if percent > 5:
    news = get_news(percent)
    send_messages(news)

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
