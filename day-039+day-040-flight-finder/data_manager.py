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
        pass

    def get_destination_data(self, page):
        return requests.get(
            url=f"{SHEETY_ENDPOINT}/{page}").json()[f'{page}']

    def get_users(self):
        return requests.get(url=f"{SHEETY_ENDPOINT}/users").json()["users"]

    def update_destination_code(self, city):
        new_data = {
            "otherprice": {
                "iataCode": city["iataCode"]
            }
        }
        response = requests.put(
            url=f"{SHEETY_ENDPOINT}/otherPrices/{city['id']}",
            json=new_data
        )
        print(response.text)
        return None
