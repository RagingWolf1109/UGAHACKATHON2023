import requests
import json
import pandas 

url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"

querystring = {"query":"eiffel tower","lang":"en_US","units":"km"}

headers = {
	"X-RapidAPI-Key": "5e1f8d911dmshb5aa1f1b7f0b470p198d8djsn21c588b9da4a",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#response.raise_for_status()
json_response = response.json()

print("Print each key-value pair from JSON response")
