import requests
from datetime import datetime
import os

# Nutritionix API details
APP_ID = "d689e26d"
API_KEY = "3216d7a9d4a844126411627d7ca91c70"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_query = {
    "query": input("Tell me which exercise you did?: ")
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_query, headers=headers)
exercises = response.json()["exercises"]

# Sheety API details
SHEETY_ENDPOINT = 'https://api.sheety.co/fc0dc8511e16406ca1f2267b5759e9af/workoutTracking/workouts'

MY_USERNAME = "shukhratov"
MY_PASSWORD = "Humoyun0050@"

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("           %H:%M:%S")

for exercise in exercises:
    sheety_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_data, auth=(MY_USERNAME, MY_PASSWORD))
