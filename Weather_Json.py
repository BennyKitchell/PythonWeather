#Gets weather in form of JSON based on user entered location
import sys
import json
import time
from Weather_api import *

#Function to quickly convert kelvin data from JSON into Farenheit
#TO:DO  add functionality for Celsius depending on location
#		move function to own file
#		Change name of function to reflect celsius as well (kelvin to local temp)		
def kelvinToFahrenheit(temp):
	f = ((temp * 9/5) - 459.67)
	return round(f)

#Actually grab the JSON data 
weatherData = json.loads(response.text)
#print(weatherData)

#Set variables for easier readability
if forecastType == '1':
	currentTemperature = kelvinToFahrenheit(weatherData['main']['temp'])
	lowTemperature = kelvinToFahrenheit(weatherData['main']['temp_min'])
	highTemperature = kelvinToFahrenheit(weatherData['main']['temp_max'])
	sunriseTime = time.strftime("%A, %-I:%M:%S %p",time.localtime(weatherData['sys']['sunrise']))
	sunsetTime = time.strftime("%A, %-I:%M:%S %p",time.localtime(weatherData['sys']['sunset']))

elif forecastType == '2':
	#We increment here by 8 to always get the current day then the next two
	currentTemperature = kelvinToFahrenheit(weatherData['list'][0]['main']['temp'])
	lowTemperature = kelvinToFahrenheit(weatherData['list'][0]['main']['temp_min'])
	highTemperature = kelvinToFahrenheit(weatherData['list'][0]['main']['temp_max'])
	#Second day temperature
	secondDayTemperature = kelvinToFahrenheit(weatherData['list'][8]['main']['temp'])
	secondDayLow = kelvinToFahrenheit(weatherData['list'][8]['main']['temp_min'])
	secondDayHigh = kelvinToFahrenheit(weatherData['list'][8]['main']['temp_max'])
	#Second Date time
	tomorrowDateTime = time.strftime("%A, %B %d, %Y",time.localtime(time.time() + 24*3600))
	#Third day temperature
	thirdDayTemperature = kelvinToFahrenheit(weatherData['list'][16]['main']['temp'])
	thirdDayLow = kelvinToFahrenheit(weatherData['list'][16]['main']['temp_min'])
	thirdDayHigh = kelvinToFahrenheit(weatherData['list'][16]['main']['temp_max'])
	#Third Date Time
	thirdDateTime = time.strftime("%A, %B %d, %Y",time.localtime(time.time() + 48*3600))
