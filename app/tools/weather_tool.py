import requests
from langchain_core.tools import tool

from app.config import WEATHER_API_KEY


@tool
def get_weather(city: str) -> str:
    """
    Fetch the current weather for a city using OpenWeatherMap.
    """

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return f"Unable to fetch weather for {city}."

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        return (
            f"Weather in {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Condition: {description}\n"
            f"Humidity: {humidity}%"
        )

    except Exception as e:
        return f"Weather API Error: {e}"