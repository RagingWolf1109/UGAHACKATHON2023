###Calls flights api

#o1 input, airport code of first orgin
Flights_o1 = input("Airport code of first orgin: ")

#d1 input, airport code of destination
Flights_d1 = input("Airport code of destination: ")

#dd1 departure date from first orgin yyy-MM-dd
Flights_dd1 = input("Departure Date: ")

#number of people (1-4)
Flights_ta = int(input("How many people: "))

# Cabin code set to economy 
Flights_c = 0

import requests

url = "https://travel-advisor.p.rapidapi.com/flights/create-session"

querystring = {"o1":Flights_o1,"d1":Flights_d1,"dd1":Flights_dd1,"currency":"USD","ta":Flights_ta,"c":"0"}

headers = {
	"X-RapidAPI-Key": "15b606d8f6mshf739bef48fc913bp1b1505jsn67251d13d9f9",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
