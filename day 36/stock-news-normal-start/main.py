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
up_down = None


def get_stock_difference_percent(offline=False):
    url = (
        f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={key}"
    )
    r = requests.get(url)

    if "Thank you for using Alpha Vantage!" not in r.text or offline:
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
    difference = yesterdays_closing - day_before_yesterdays_closing
    global up_down
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    percent = round((difference / day_before_yesterdays_closing) * 100.0)

    return percent


def get_news():
    news_params = {
        "apiKey": news_api,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, news_params)
    data = response.json()
    three = data["articles"][:3]

    three_articles = {index["title"]: index["content"] for index in three}
    return three_articles


def send_messages(news, percent):
    global up_down
    for key in news:
        message = f"""{STOCK_ENDPOINT}: {up_down} {percent}%
                    Headline: {key}
                    Brief: {news[key][:90]}                    
                    """
        print(message)


percent = get_stock_difference_percent(True)
if abs(percent) > 0:
    news = get_news()
    send_messages(news, percent)
