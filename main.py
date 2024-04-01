import os

import datetime
from dotenv import load_dotenv
import requests
from datetime import datetime, date

load_dotenv()
sheety_post_endpoint = "https://api.sheety.co/83f756b5b637bb7aaefd61fc0a250dde/myWorkouts2024/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"
exercise_header = {
    "x-app-id": os.environ.get("NUTRIX-APPID"),
    "x-app-key": os.environ.get("NUTRIX-KEY")
}

print(os.environ.get("NUTRIX-APPID"))
print(os.environ.get("NUTRIX-KEY"))

exercise_params = {
    'query': "I ran for 30 minutes",
    # "age": int(input("How old are you? "))
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_header)
response.raise_for_status()
exercise_insight = response.json()

print(date.today())
# print(datetime.now().strftime("%H:%M:%S"))
print(exercise_insight["exercises"][0]["user_input"])
print(exercise_insight["exercises"][0]["duration_min"])
print(exercise_insight["exercises"][0]["nf_calories"])

for exercise in exercise_insight["exercises"]:

    work = {
        "workout": {
            "time": datetime.now().strftime("%X"),
            "date": datetime.now().strftime("%d/%m/%Y"),
            "exercise": exercise_insight["exercises"][0]["name"].title(),
            "duration": exercise_insight["exercises"][0]["duration_min"],
            "calories": exercise_insight["exercises"][0]["nf_calories"]
        }
    }
#
r = requests.post(url=sheety_post_endpoint, json=work)

print(r.text)
