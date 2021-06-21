import requests
import datetime

APP_ID = "APP_ID"
APP_KEY = "APP_KEY"

natural_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = "https://api.sheety.co/bfd7e9451e0cd6ef5cf35a8679fc7470/myWorkoutsDay38/workouts"

SHEETY_USERNAME = "USERNAME"
SHEETY_PASS = "SEETY PASSWORD"
SHEETY_BEARER = {"Authorization": "TOKEN"}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key": APP_KEY
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender":"male",
    "weight_kg": 60,
    "height_cm": 168,
    "age":35
}

response = requests.post(url=natural_endpoint, headers=headers, json=parameters)

result = response.json()
print(result)
exercise_result = result["exercises"]
print(exercise_result)

now = datetime.datetime.now()
date_now = now.strftime("%Y/%m/%d")
time_now = now.strftime("%X")

sheet_response = requests.get(url=SHEETY_API,headers=SHEETY_BEARER)
print(sheet_response.json())


for X in exercise_result:
    body = {
        "workout": {
        "date": date_now,
        "time": time_now,
        "exercise": X["name"].title(),
        "duration": X["duration_min"],
        "calories":X["nf_calories"],
        # "met":X["met"],
        # "compendium":X["compendium_code"]
        }
    }

    # sheet_response = requests.post(url=SHEETY_API, json=body, auth=(SHEETY_USERNAME,SHEETY_PASS))
    sheet_response = requests.post(url=SHEETY_API, json=body, headers=SHEETY_BEARER)

    print(sheet_response.text)