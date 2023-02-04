import requests
from requests.exceptions import HTTPError
import json
import pandas 
###############################################################################################################################################################
#http headers
hot_headers = {
    "content-type": "application/json",
	"X-RapidAPI-Key": "5e1f8d911dmshb5aa1f1b7f0b470p198d8djsn21c588b9da4a",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}
###############################################################################################################################################################

#Ask the user for a location
location = input("Where to dumbass? ")

hot_geo_id = 000000
hot_in_date = "04-24-2023" #MM/DD/YYYY
hot_out_date = "04-24-2023" #MM/DD/YYYY
adults = 2

###############################################################################################################################################################
#The url that requests are sent to in order to determine geoID (helluva task for me for some reason)
geo_url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"

#query parameters used to find the geo ID
hot_loc_query = {"query":location,"lang":"en_US","units":"mi"}

#Requests the location's information which includes the geo ID and then converts to string
string = str((requests.request("GET", geo_url, headers=hot_headers, params=hot_loc_query)).json())

#From the request it parses the geoID by finding the location of the leading characters and then adds the 
#default 5 character geo ID length
hot_geo_id = int(string[string.find("\'geoId\':") + 9 : string.find("\'geoId\':") + 14])
print(str(hot_geo_id), "\n\n\n")
###############################################################################################################################################################

#Hotel request url
hot_url = "https://travel-advisor.p.rapidapi.com/hotels/v2/list"

#New query for determining actual hotel information
hot_query_string = {"currency":"USD","units":"mkm","lang":"en_US"}

#All variables that have been passed in are placed into payload
hot_payload = {
	"geoId": hot_geo_id,
	"checkIn": hot_in_date,
	"checkOut": hot_out_date,
	"sort": "PRICE_LOW_TO_HIGH",
	"sortOrder": "asc",
	"filters": [
		{
			"id": "price",
			"value": ["31", "122"]
		},
		{
			"id": "type",
			"value": ["9189", "9201"]
		},
		{
			"id": "rating",
			"value": ["40"]
		},
		{
			"id": "class",
			"value": ["9572"]
		}
	],
	"rooms": [
		{
			"adults": adults,
			"childrenAges": [2]
		},
	],
	"updateToken": ""
}

#request is sent
try:
    response = requests.request("POST", hot_url, json=hot_payload, headers=hot_headers, params=hot_query_string)
    #output response
    print(response.text)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')