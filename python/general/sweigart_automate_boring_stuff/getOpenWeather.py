#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
# Edited with different weather api bc OpenWeatherMap is paid

APPID = 'YOUR_APPID_HERE'

import json, requests, sys

# Compute location from command line arguments.
# if len(sys.argv) < 2:
#     print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
#     sys.exit()
# location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
# Download the JSON data from OpenWeatherMap.org's API.
# url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
url ='https://api.open-meteo.com/v1/forecast?latitude=52.2297&longitude=21.0122&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)   

# TODO: Load JSON data into a Python variable.
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# print('weatherData: ', weatherData)

# Print weather descriptions.
# w = weatherData['list']
w = weatherData
# print('w: ', w)
print('Current weather in latitude %s, : longitude %s' % (w['latitude'], w['longitude']))
print("Temp min: ",  min(w['daily']['temperature_2m_min']))
print("Temp min: ",  max(w['daily']['temperature_2m_max']))
# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])

# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
# print()
# print('Tomorrow:')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
# print()
# print('Day after tomorrow:')
# print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])