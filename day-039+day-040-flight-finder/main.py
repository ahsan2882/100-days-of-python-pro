# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
import schedule
from user import User
from data_manager import DataManager
from flight_search import FlightSearch

dataManager = DataManager()
sheet_data = dataManager.get_destination_data('otherPrices')
users = dataManager.get_users()
flightSearch = FlightSearch()

for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flightSearch.get_destination_code(data["city"])
        dataManager.update_destination_code(city=data)

for user_data in users:
    user = User(user_data, flightSearch)
