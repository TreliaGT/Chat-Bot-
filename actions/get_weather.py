# actions/get_weather.py
import requests
import os

class GetWeather:
    def execute(self):
        city = input("ChatBot: Which city's weather would you like to check? ").strip()

        # Step 1: Use Nominatim to get lat/lon
        geo_url = os.getenv('LAT_LONG_API')
        geo_params = {
            "q": city,
            "format": "json",
            "limit": 1
        }
        geo_headers = {
            "User-Agent": "ChatBotWeatherApp/1.0 (your_email@example.com)"
        }

        try:
            geo_response = requests.get(geo_url, params=geo_params, headers=geo_headers)
            geo_data = geo_response.json()

            if not geo_data:
                return f"Sorry, I couldn't find location data for '{city}'."

            lat = geo_data[0]["lat"]
            lon = geo_data[0]["lon"]

            # Step 2: Use Open-Meteo to get weather
            weather_url = os.getenv('WEATHER_API')
            weather_params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": "true"
            }

            weather_response = requests.get(weather_url, params=weather_params)
            weather_data = weather_response.json()

            current = weather_data.get("current_weather", {})
            temp = current.get("temperature")
            wind = current.get("windspeed")
            desc = f"{temp}°C with wind speed of {wind} km/h"

            return f"The current weather in {city.title()} is {desc}."

        except Exception as e:
            return f"Something went wrong while fetching the weather: {e}"
