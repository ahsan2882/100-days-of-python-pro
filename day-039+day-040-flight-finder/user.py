import time
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


class User:
    def __init__(self, user, flightSearch: FlightSearch):
        self.email = user["email"]
        self.originCity = user["iataCodeOrigin"]
        self.dataManager = DataManager()
        self.userName = f'{user["firstName"]} {user["lastName"]}'
        if user["role"] == "Admin":
            page = "prices"
        else:
            page = "otherPrices"

        self.sheet_data = self.dataManager.get_destination_data(page=page)
        self.flightSearch = flightSearch
        self.notificationManager = NotificationManager()
        self.check_cheapest_flight()

    def check_cheapest_flight(self):
        print(f"Checking cheapest flight for user {self.userName}...")
        for destination in self.sheet_data:
            if self.originCity != destination["iataCode"]:
                flight = self.flightSearch.check_flights(
                    self.originCity,
                    destination["iataCode"],
                    from_time=datetime.now().strftime("%d/%m/%Y"),
                    to_time=(datetime.now() + timedelta(days=7)
                             ).strftime("%d/%m/%Y")
                )
                print(flight.destination_airport, flight.price)
                if flight.price <= destination["lowestPrice"] and flight.price != 0:
                    bookingLink = f'https://www.google.com/travel/flights?q=Flights%20to%20{flight.destination_airport}%20from%20{flight.origin_airport}%20on%20{flight.out_date}%20oneway'
                    self.notificationManager.send_email(
                        message=f"Low price alert! Only {flight.price}/= PKR to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, on {flight.out_date}.\nClick the link  below to book your flight: \n{bookingLink}",
                        email=self.email
                    )
