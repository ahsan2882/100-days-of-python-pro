import os
import time
import smtplib
import requests
import schedule
from datetime import datetime
from dotenv import load_dotenv

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()
load_dotenv(DOTENV_PATH)

MY_LAT = 24.960979
MY_LONG = 67.082199
EMAIL = 'ahsan.shahid.cssfl@gmail.com'
PASSWORD = os.getenv('PASSWORD')

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}


def is_iss_visible():
    iss_response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_dark():
    dark_sky_response = requests.get(
        'https://api.sunrise-sunset.org/json', params=parameters)
    dark_sky_response.raise_for_status()
    dark_sky_data = dark_sky_response.json()

    sunrise_time = int(dark_sky_data['results']
                       ['sunrise'].split('T')[1].split(':')[0])
    sunset_time = int(dark_sky_data['results']
                      ['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.utcnow()
    return time_now.hour > sunset_time or time_now.hour < sunrise_time


def scheduled_job():
    if is_iss_visible() and is_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                to_addrs='ahsanshahid2882@gmail.com',
                msg='Subject:Look up👆\n\nLook up! The ISS is above you!'
            )


schedule.every(60).seconds.do(scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(0.1)
