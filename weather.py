import requests, json, math
import re

f = open('apiKey.txt', 'r') #reading apikey from file
key = f.readline()
key = re.compile(r'\W+', re.UNICODE).split(key)
key = key[0]
f.close() 
api_key = key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = "Granada" #by default

def setCity(city):
    city_name = city

def createURL(base_url, city_name, api_key):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    return complete_url

response = requests.get(createURL(base_url,city_name, api_key))
 
def getJSON(response):
    # json method of response object convert json format data into python format data
    response = requests.get(createURL(base_url,city_name, api_key))  
    JSONObject = response.json()

    if JSONObject["cod"] != "404":        
        return JSONObject
    else:
        return None
 
def getWeatherTemperature(x):
    x = getJSON(response)
    y = x["main"]
    current_temperature = y["temp"] #Temperature in Kelvin
    
    return current_temperature

def convertToCelsius(Kelvin):
    Celsius = Kelvin - 273.15

    return math.ceil(Celsius)

def getWeatherPressure(x):
    x = getJSON(response)
    y = x["main"]
    current_pressure = y["pressure"]

    return current_pressure
 
def getWeatherHumidity(x):
    x = getJSON(response)
    y = x["main"]
    current_humidity = y["humidity"]

    return current_humidity 

