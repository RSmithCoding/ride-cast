import requests
import os

def clear():
    os.system('clear')

clear()

print("Welcome to Ride Cast\n")
print("Available Bike Parks:\n")

bikeparks = {
    "Glentress": (55.6467,-3.1395),
    "Hamsterley Forrest": (54.672, -1.856),
    "Ae Forrest": (55.2333, -3.5833),
    "Fort William": (56.8372, -5.0617),
    "Bike Park Wales": (51.718074, -3.361611),
    "Revolution Bike Park": (52.820472, -3.410595),
    "Morzine": (46.179192, 6.708877)
}

menu = {
    "1": "Glentress",
    "2": "Hamsterley Forrest",
    "3": "Ae Forrest",
    "4": "Fort William",
    "5": "Bike Park Wales",
    "6": "Revolution Bike Park",
    "7": "Morzine"
}

for key in menu:
    
    print(key, menu[key], sep='\t')


choice = input("\n\nSelect first bike park to compare: ")
selection = menu.get(choice)
check = selection

choice2 = input("\nSelect second bike park to compare: ")
selection2 = menu.get(choice2)
check2 = selection2

choice3 = input("\nSelect third bike park to compare: ")
selection3 = menu.get(choice3)
check3 = selection3

result = bikeparks.get(check)
result2 = bikeparks.get(check2)
result3 = bikeparks.get(check3)

if result: 
    lat, long = result

if result2: 
    lat2, long2 = result2
    
if result3: 
    lat3, long3 = result3   


clear()
print("Welcome to Ride Cast\n")


def getweather(lat,long,check):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
    
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "precipitation", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", "weather_code"],
    "wind_speed_unit": "mph",
    "hourly": ["temperature_2m", "weather_code"],
    "daily": ["sunrise", "sunset"],
    "forecast_hours": "9",
    "forecast_days": "1",
    "timezone": "Europe/London"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    bikepark = check

    current = data["current"]
    units = data["current_units"]
    weathercode = current['weather_code']
    winddegrees = current['wind_direction_10m']

    hourly = data["hourly"]
    hourlyunits = data["hourly_units"]
    hourlyweathercode = hourly['weather_code']
    time = hourly['time']
    hourlytemp = hourly['temperature_2m']
    unittemp = hourlyunits['temperature_2m']
    daily = data["daily"]

    weathercoderesults = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        97: "Heavy thunderstorm",
        99: "Thunderstorm with heavy hail"}

    weathercodesymbol = {
        0: "☀️",
        1: "🌤",
        2: "⛅️",
        3: "☁️",
        45: "🌫",
        48: "🌫",
        51: "🌦",
        53: "🌦",
        55: "🌦",
        56: "🌨",
        57: "🌨",
        61: "🌧",
        63: "🌧",
        65: "🌧",
        66: "🌨",
        67: "🌨",
        71: "🌨",
        73: "❄️",
        75: "❄️",
        77: "❄️",
        80: "🌧",
        81: "🌧",
        82: "🌧",
        85: "🌨",
        86: "❄️",
        95: "🌩",
        96: "⛈",
        97: "⛈",
        99: "⛈"
    }

    matchingdata = weathercoderesults.get(weathercode)
    hourlymatchingdata = [weathercoderesults.get(num) for num in hourlyweathercode[1:]]
    matchingsymbol = weathercodesymbol.get(weathercode)
    hourlymatchingsymbol = [weathercodesymbol.get(num) for num in hourlyweathercode[1:]]

    winddirection = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(winddegrees / 45) % 8

    print(f"Current Weather Data for {bikepark}\n")

    print(f"Temperature: {current['temperature_2m']} {units['temperature_2m']}\t"
        f"Percipitation: {current['precipitation']} {units['precipitation']}\t" 
        f"Sunrise: {daily['sunrise'][0][-5:]}\tSunset: {daily['sunset'][0][-5:]}\t"
        f"{matchingdata}\t{matchingsymbol}\n")

    print(f"Wind Speed: {current['wind_speed_10m']} {units['wind_speed_10m']}\t"
#        f"Wind Direction: {current['wind_direction_10m']} {units['wind_direction_10m']}\t"
        f"Wind Direction: {winddirection[index]}\t"
        f"Wind Gust Speed: {current['wind_gusts_10m']} {units['wind_gusts_10m']}\n")

    timeseperated = "\t\t".join(item[-5:] for item in time[1:])
    print(f"{timeseperated}\n")
   
    hourlytempseperated = "\t\t".join(f"{item:.1f} {unittemp}" for item in hourlytemp[1:])
    print(f"{hourlytempseperated}\n")

    hourlysymbolseperated = "\t\t".join(item for item in hourlymatchingsymbol)
    print(f"{hourlysymbolseperated}")
    
#    hourlydataseperated = "\t".join(item for item in hourlymatchingdata)
#    print(f"{hourlydataseperated}")


getweather(**{"lat": lat, "long": long, "check": check})
getweather(**{"lat": lat2, "long": long2, "check": check2})
getweather(**{"lat": lat3, "long": long3, "check": check3})


