import json
import os

from botocore.vendored import requests

def weatherfunc(city_name):
    api_key = os.environ["weatherAPI"]
	# The api is stored as a environment variable with key weatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
	# The base url for openweathermap
    final_url = base_url + "appid=" + api_key + "&q=" + city_name
	# The final URL after passing the aoi key and city name
    
    weather_result = requests.get(final_url)
	# The result of api call 
    x = weather_result.json()
	# Result is converted to a JSON format
    y = x["main"]

    temperature = y["temp"] - 272.15
	# The current temperature is returned in Kelvin. It is converted to celsius by subtracting 272.15 from it

    pressure = y["pressure"]

    humidity = y["humidity"]

    temp_min = y["temp_min"] - 272.15

    temp_max = y["temp_max"] - 272.15

    details = x["weather"]

    weather_desc = details[0]["description"]
    
    final_result = f'It is {temperature} °C in {city_name}. The humidity is {humidity}%. The temperature will be between {temp_min} and {temp_max} °C today. {weather_desc} today in {city_name}'
    
    return final_result

def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["City"]
    
    result = weatherfunc(city)
    
    response = {
          "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content":result
            },
        }
    } 
    
    return response
    
    
    
    
