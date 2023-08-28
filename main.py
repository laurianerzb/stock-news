import requests
from twilio.rest import Client
import os


# twilio credentials
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
percentage_difference = round(difference / float(yesterday_closing_price) * 100)
print(percentage_difference)
if abs(percentage_difference) > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    print(news_data)
    # Use Python slice operator to create a list that contains the first 3 articles
    news_list = news_data[:3]
    print(news_list)

    # Create a new list of the first 3 articles headline and description using list comprehension
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}"
        f"\nDescription: {article['description']}" for article in news_list
    ]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="TWILIO_VIRTUAL_NUMBER",
            to='TWILIO_VERIFIED_NUMBER'
        )
        print(message.sid)
