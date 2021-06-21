import requests
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

API_SHEETY = "https://api.sheety.co/bfd7e9451e0cd6ef5cf35a8679fc7470/day39FlightDeals/prices"
APP_ID = "APP_ID"
APP_KEY = "APP_KEY"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key": APP_KEY
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=API_SHEETY, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{API_SHEETY}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)