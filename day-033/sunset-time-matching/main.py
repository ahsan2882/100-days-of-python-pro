import requests
from datetime import datetime

MY_LAT = '24.960979'
MY_LONG = '67.082199'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_time = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise_time)

now = datetime.now()
print(now.hour)
