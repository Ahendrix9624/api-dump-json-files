import requests
import json
import os

API_KEY = os.environ(["WEATHER_API_KEY"])     
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}{city}&appid={API_KEY}"
response = requests.get(requests_url)

#Writes the api to a json file in the following directory
data = response.json()
with open("/Users/drew/Documents/opt/api_call.json", "w") as outfile:
    json.dump(data, outfile)
