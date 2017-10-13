import requests

#Location input/ temporary
location = input("Where are you? ")
#User input for the type of forecast (current/3 day/5 day)
forecastType = input("Please enter 1, 2, or 3: \n1. Current Weather\n2. 3 Day forecast\n")
#Switch statement to customize user options
def switch(forecastType):
	switch_dict = {
		'1': 'http://api.openweathermap.org/data/2.5/weather?q=%s&&appid=cf60deefc07c9d900a6d23609d711c93' %(location),
		'2': 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=cf60deefc07c9d900a6d23609d711c93' %(location)
	}
	return switch_dict.get(forecastType)
url = switch(forecastType)

#GET request for all of the json data
try:
   response = requests.get(url)
except ConnectionError as e:
   print(e)