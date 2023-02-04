###Calls flights api

#o1 input, airport code of first orgin
Flight_o1 = input("Airport code of first orgin: ")

#d1 input, airport code of destination
Flight_d1 = input("Airport code of destination: ")

#dd1 departure date from first orgin yyy-MM-dd
Flight_dd1 = input("Departure Date: ")

#number of people (1-4)
Flights_ta = int(input("How many people: "))

# Cabin code set to economy 
Flights_c = 0

import requests

url = "https://travel-advisor.p.rapidapi.com/flights/create-session"

querystring = {"o1":"DMK","d1":"CNX","dd1":"2022-03-15","currency":"USD","ta":"1","c":"0"}

headers = {
	"X-RapidAPI-Key": "15b606d8f6mshf739bef48fc913bp1b1505jsn67251d13d9f9",
	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
