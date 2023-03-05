import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import smtplib
import schedule
import time

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()
load_dotenv(DOTENV_PATH)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2"


def get_stock_data():
    stock_params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK_NAME,
        'apikey': os.getenv('STOCK_API_KEY')
    }
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()
    stock_result = stock_response.json()['Time Series (Daily)']
    stock_data_list = [value for (key, value) in stock_result.items()]
    yesterday_data = stock_data_list[0]
    yesterday_closing_price = float(yesterday_data['4. close'])
    day_before_yesterday_data = stock_data_list[1]
    day_before_yesterday_closing_price = float(
        day_before_yesterday_data['4. close'])
    difference = yesterday_closing_price - day_before_yesterday_closing_price

    diff_percent = round((abs(difference) / yesterday_closing_price) * 100, 2)
    if abs(diff_percent) > 20:
        formatted_articles = get_news_data(difference)
        send_email(formatted_articles)


def get_news_data(difference: float) -> list:
    up_down = None
    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"
    news_params = {
        'apiKey': os.getenv('NEWS_API_KEY'),
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'language': 'en'
    }
    news_response = requests.get(
        f'{NEWS_ENDPOINT}/everything', params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][0:3]
    return [
        f"{STOCK_NAME}:{up_down}{difference}%\nHeadline: {article['title']}. \nBrief:{article['description']}"
        for article in news_data
    ]


def send_email(formatted_articles: list):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=os.getenv('EMAIL'),
                         password=os.getenv('PASSWORD'))
        for article in formatted_articles:
            msg = f"Subject: {STOCK_NAME} Alert\n\n{article}"
            connection.sendmail(
                from_addr=os.getenv('EMAIL'),
                to_addrs=os.getenv('TO_EMAIL'),
                msg=msg.encode('utf-8'))


schedule.every().day.at("04:00").do(get_stock_data)

while True:
    schedule.run_pending()
    time.sleep(3600)
