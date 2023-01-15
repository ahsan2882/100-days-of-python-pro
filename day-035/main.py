from dotenv import load_dotenv
import os
import requests
from pathlib import Path
from datetime import datetime
import smtplib
import time
import schedule

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()
load_dotenv(DOTENV_PATH)


EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

MY_LAT = 24.9611085
MY_LONG = 67.0731898


def get_forecast():
    now = datetime.now()
    hour = now.hour
    API_KEY = os.getenv(f'OPEN_WEATHER_API_KEY_{hour % 6 + 1}')
    forecast_params = {
        'lat': MY_LAT,
        'lon': MY_LONG,
        'units': 'metric',
        'exclude': 'current,minutely',
        'appid': API_KEY,
    }
    forecast_response = requests.get(
        'https://api.openweathermap.org/data/3.0/onecall', params=forecast_params)
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()
    hourly_forecast = forecast_data['hourly'][:14]
    rain_forecast = [hourly['weather'][0]['id']
                     for hourly in hourly_forecast if hourly['weather'][0]['id'] < 700]
    if len(rain_forecast) > 0:
        send_email('It is going to rain today.')
    else:
        send_email('No rain today.')


def get_weather():
    get_forecast()
    # add more methods in future like AQI


def send_email(message: str):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='ahsanshahid2882@gmail.com',
            msg=f'Subject: Rain Alert\n\n{message}'
        )


schedule.every().day.at('19:13').do(get_weather)

while True:
    schedule.run_pending()
    time.sleep(1)
