#!/usr/bin/env python3
#
#  [Program]
#
#  API Call then dump files to json 
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.

# import requests HTTP Library module, import json module
import requests
import json


API_KEY = "9afd1eb66741444d53f93555e9008535"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}{city}&appid={API_KEY}"
response = requests.get(requests_url)

#Writes the api to a json file in the following directory
data = response.json()
with open("/Users/drew/Documents/opt/api_call.json", "w") as outfile:
    json.dump(data, outfile)
