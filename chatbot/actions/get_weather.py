# actions/get_weather.py
import requests
import os

#gets the weather information by getting the lat/long of the city inputted then using an weather api to check the weather
class GetWeather:
    def execute(self, user_input=None):
        if not user_input:
            return "Please specify a city for the weather lookup."

        # Try to extract a city name from the user input
        words = user_input.lower().split()
        city_keywords = ["in", "for", "at"]
        city = None

        for keyword in city_keywords:
            if keyword in words:
                idx = words.index(keyword)
                if idx + 1 < len(words):
                    city = " ".join(words[idx + 1:])
                    break

        # fallback: try using last word as city
        if not city and len(words) >= 1:
            city = words[-1]

        if not city:
            return "Sorry, I couldn't understand which city you meant."

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

            if temp is None or wind is None:
                return f"Couldn't retrieve current weather for {city.title()}."

            desc = f"{temp}°C with wind speed of {wind} km/h"
            return f"The current weather in {city.title()} is {desc}."

        except Exception as e:
            return f"Something went wrong while fetching the weather: {e}"
