#Gets weather in form of JSON based on user entered location
import sys
import json
import requests
import time

#Location input/ temporary
location = input("Where are you? ")

#Get JSON from openweather.org
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&appid=cf60deefc07c9d900a6d23609d711c93' %(location)

#GET requests to open weather to grab the JSON data
try:
   response = requests.get(url)
except ConnectionError as e:
   print(e)

#Function to quickly convert kelvin data from JSON into Farenheit
#TO:DO add functionality for Calsius depending on location
def kelvinToFahrenheit(temp):
	f = ((temp * 9/5) - 459.67)
	return round(f)

#Actually grab the JSON data 
weatherData = json.loads(response.text)

#Set variables for easier readability
currentTemperature = kelvinToFahrenheit(weatherData['main']['temp'])
lowTemperature = kelvinToFahrenheit(weatherData['main']['temp_min'])
highTemperature = kelvinToFahrenheit(weatherData['main']['temp_max'])

#Take epoch time and convert it into HMS format for sunrise and sunset
sunriseTime = time.strftime("%H:%M:%S",time.localtime(weatherData['sys']['sunrise']))
sunsetTime = time.strftime("%H:%M:%S",time.localtime(weatherData['sys']['sunset']))

#Display the data
print("\n\n\n***********************************************************************")
print("Current weather in {}: {} ".format(weatherData['name'],weatherData['weather'][0]['description']))
print("Current temperature in {}: {} with a low of {} and a high of {}".format(weatherData['name'], currentTemperature, lowTemperature, highTemperature))
print("Sunrise: {} | Sunset: {}".format(sunriseTime, sunsetTime))
print("***********************************************************************\n\n\n")


