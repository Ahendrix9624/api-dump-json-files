"""
USAGE - The code imports the requests, json and os modules. It retrieves an API key from the 
        environment variables stored in the system, prompts the user to enter a city name, and 
        concatenates the city name and API key to create a request URL. The requests module 
        is used to make a GET request to the API URL, and the response is saved in a JSON 
        file named "api_call.json" in the current directory.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

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
with open("api_call.json", "w") as outfile:
    json.dump(data, outfile)
