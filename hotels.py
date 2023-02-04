import requests
import json
import pandas 


#
url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"

hot_headers = {
    "content-type": "application/json",
	"X-RapidAPI-Key": "5e1f8d911dmshb5aa1f1b7f0b470p198d8djsn21c588b9da4a",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}
#

#Ask the user for a location
location = input("Where to dumbass? ")

#
hot_loc_query = {"query":location,"lang":"en_US","units":"mi"}
#
string = str((requests.request("GET", url, headers=hot_headers, params=hot_loc_query)).json())
hot_geo_id = int(string[string.find("\'geoId\':") + 9 : string.find("\'geoId\':") + 14]))
#
hot_query_string = {"currency":"USD","units":"mi","lang":"en_US"}
#
hot_payload = {
	"geoId": hot_geo_id,
	"checkIn": "2022-03-10",
	"checkOut": "2022-03-15",
	"sort": "PRICE_LOW_TO_HIGH",
	"sortOrder": "asc",
	"filters": [
		{
			"id": "deals",
			"value": ["1", "2", "3"]
		},
		{
			"id": "price",
			"value": ["31", "122"]
		},
		{
			"id": "type",
			"value": ["9189", "9201"]
		},
		{
			"id": "amenity",
			"value": ["9156", "9658", "21778", "9176"]
		},
		{
			"id": "distFrom",
			"value": ["2227712", "25.0"]
		},
		{
			"id": "rating",
			"value": ["40"]
		},
	],
	"rooms": [
		{
			"adults": 2,
			"childrenAges": [2]
		},
	],
	"boundingBox": {
		"northEastCorner": {
			"latitude": 12.248278039408776,
			"longitude": 109.1981618106365
		},
		"southWestCorner": {
			"latitude": 12.243407232845051,
			"longitude": 109.1921640560031
		}
	},
	"updateToken": ""
}
#



exit()

response = requests.request("POST", url, json=payload, headers=headers, params=hot_query_string)

print(response.text)

json_response = response.json()



