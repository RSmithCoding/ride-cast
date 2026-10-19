import requests
import os

def clear():
    os.system('clear')

clear()    
print("Welcome to Ride Cast")

url = "https://api.open-meteo.com/v1/forecast"

params = {
    
    "latitude": 55.6467,
    "longitude": -3.1395,
    "current": ["temperature_2m","precipitation", "wind_speed_10m","wind_direction_10m", "wind_gusts_10m", "weather_code"],

}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

#print(data["current"])

bikepark = "Glentress Bike Park"
current = data["current"]
units = data["current_units"]

print()
print(f"Current Weather Data for {bikepark}\n")
print(f"Temperature: {current['temperature_2m']} {units['temperature_2m']}\t"
    f"Percipitation: {current['precipitation']} {units['precipitation']}\n")
print(f"Wind Speed: {current['wind_speed_10m']} {units['wind_speed_10m']}\t"
    f"Wind Direction: {current['wind_direction_10m']} {units['wind_direction_10m']}\t" 
    f"Wind Gust Speed: {current['wind_gusts_10m']} {units['wind_gusts_10m']}\n")
print(f"Weather Code: {current['weather_code']}\n")
