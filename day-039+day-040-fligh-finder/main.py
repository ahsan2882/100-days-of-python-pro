# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import time
import schedule
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()

load_dotenv(DOTENV_PATH)

PRODUCTION = os.getenv("PRODUCTION")

ORIGIN_CITY_IATA = "KHI"

dataManager = DataManager()
sheet_data = dataManager.get_destination_data()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flightSearch.get_destination_code(data["city"])
        dataManager.update_destination_code(city=data)
        dataManager.destination_data = sheet_data


def get_min_price():
    sheet_data = dataManager.get_destination_data()
    min_price = {}
    for city in sheet_data:
        cityMinPrice = city["lowestPrice"]
        min_price[city["iataCode"]] = cityMinPrice
    if PRODUCTION == "True":
        step_size = 7
    else:
        step_size = 300
    for destination in sheet_data:
        for i in range(1, 12*30*2, step_size):
            flight = flightSearch.check_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=(datetime.now() + timedelta(days=(i))
                           ).strftime("%d/%m/%Y"),
                to_time=(datetime.now() + timedelta(days=(i+7))
                         ).strftime("%d/%m/%Y")
            )
            print(i, flight.destination_airport, flight.price)
            if flight.price != 0:
                if min_price[flight.destination_airport] == 0:
                    min_price[flight.destination_airport] = flight.price
                if flight.price < min_price[flight.destination_airport]:
                    min_price[flight.destination_airport] = flight.price
            print(min_price)
            print("Waiting for 5 seconds...")
            time.sleep(5)
        print(flight.destination_airport,
              min_price[flight.destination_airport])
        if min_price[flight.destination_airport] == 0:
            min_price[flight.destination_airport] = 25000

    dataManager.upload_min_price(min_price, cities=sheet_data)
    sheet_data = dataManager.get_destination_data()


def check_cheapest_flight():
    for destination in sheet_data:
        flight = flighSearch.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=today,
            to_time=six_month_from_today
        )
        if flight.price < destination["lowestPrice"]:
            notificationManager.send_email(
                f"Low price alert! Only {flight.price}/= PKR to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, on {flight.out_date}.")


get_min_price()
check_cheapest_flight()
schedule.every(7).days.do(check_cheapest_flight)
schedule.every(30).days.do(get_min_price)

while True:
    schedule.run_pending()
    time.sleep(60*60*24)
