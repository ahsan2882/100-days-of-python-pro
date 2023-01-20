from pprint import pprint
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)


SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    def update_destination_code(self, city):
        new_data = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(
            url=f"{SHEETY_ENDPOINT}/{city['id']}",
            json=new_data
        )
        print(response.text)

    def upload_min_price(self, prices, cities):
        for city in cities:
            new_data = {
                'price': {
                    'lowestPrice': prices[city['iataCode']]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
