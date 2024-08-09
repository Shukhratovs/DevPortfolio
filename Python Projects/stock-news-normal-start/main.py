import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "5GWA187WFPAC4KZP"
NEWS_API_KEY = "593a6e75e9f845a6ac0b7b626e0224dd"
account_sid = 'ACe77b3844ac224451a746506b3d02d2c3'
auth_token = '52c3d99995d10ee94b791192bae586d1'

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
# print(stock_data)

data_list = [data for (key, data) in stock_data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]
# print(yesterdays_closing_price)

the_day_before_yesterdays_data = data_list[1]
the_day_before_yesterdays_closing_price = the_day_before_yesterdays_data["4. close"]
# print(the_day_before_yesterdays_closing_price)

difference = abs(float(yesterdays_closing_price) - float(the_day_before_yesterdays_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round(difference / float(yesterdays_closing_price) * 100)

if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"][:3]
    three_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)
    for article in three_articles:
        message = client.messages.create(
            from_='+18556052350',
            body=article,
            to='+15204359192'
        )

