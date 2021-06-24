import requests
import json

from datetime import datetime

data = {}

api_key = 'abfd78679af71eeb3cefd279f3c841dc'
location = input("Enter the name of the City: ")

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

data['Location'] = location
data['Date & Time'] = date_time
data['Temperature'] = temp_city
data['Weather desc'] = weather_desc
data['Humidity'] = hmdt
data['Wnd Speed'] = wind_spd


print("----------------------------------------------------------------")
print("Weather Stats for - {}  ||  {}".format(location.upper(), date_time))
print("----------------------------------------------------------------")
print("Current Temperature is: {:.2f} deg C".format(temp_city))
print("Current Weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current Wind speed    :", wind_spd, 'kmph')

with open('output.txt', 'w') as f:
    f.write(json.dumps(data))