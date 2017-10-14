from Weather_Json import *
import datetime
#Display the data
print("\n\n\n***********************************************************************")
if forecastType == '1':
	print("Current weather in {}: {} ".format(weatherData['name'], weatherData['weather'][0]['description']))
	print("Current temperature in {}: {} with a low of {} and a high of {}".format(weatherData['name'], currentTemperature, lowTemperature, highTemperature))
	print("Humidity: {} | Wind Speed: {}".format(weatherData['main']['humidity'], weatherData['wind']['speed']))
	print("Next Sunrise: {} | Next Sunset: {}".format(sunriseTime, sunsetTime))
if forecastType == '2':
	print("Current weather in {}: {} ".format(weatherData['city']['name'], weatherData['list'][0]['weather'][0]['description']))
	print("Current temperature in {}: {} with a low of {} and a high of {}".format(weatherData['city']['name'], currentTemperature, lowTemperature, highTemperature))
	print("Weather for {}: {} | Temperature: {}".format(tomorrowDateTime, weatherData['list'][8]['weather'][0]['description'],secondDayTemperature))
	print("Weather for {}: {} | Temperature: {}".format(thirdDateTime, weatherData['list'][16]['weather'][0]['description'],thirdDayTemperature))
print("***********************************************************************\n\n\n")