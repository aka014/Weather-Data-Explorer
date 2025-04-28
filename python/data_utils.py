import requests
import json
import os

def fetch_weather_data(env):
    """
    Fetches weather data from Wunderground (still not this one) API.

    Args:
        env (dict): A dictionary containing lat, lon and API key for the weather service.
    Returns:
        dict: A dictionary containing the weather data, or None if an error occurred.
    """

    try:
        # Construct the API URL
        api_url = (f"https://api.openweathermap.org/data/2.5/weather?lat={env['lat']}&lon={env['lon']}" +
                   f"&appid={env['api_key']}&units=metric")

        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes

        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print (f"Error fetching weather data: {e}")
        return None
    except json.JSONDecodeError as e:
        print (f"Error parsing JSON response: {e}")
        return None

def get_api_key():
    api_key = os.environ.get("API_KEY")
    lat = os.environ.get("LAT")
    lon = os.environ.get("LON")
    result = {'api_key': api_key, 'lat': lat, 'lon': lon}
    return result


def extract_data(weather_data):
    """
    Extracts relevant weather data from the API response.

    Args:
        weather_data (dict): A dictionary containing the weather data.

    Returns:
        dict: A dictionary containing the extracted data, or None if input is invalid.
    """

    if not isinstance(weather_data, dict):
        print("Error: Invalid weather data format.")
        return None

    try:
        # Extract data
        temperature_c = weather_data.get("main", {}).get("temp", "N/A")
        pressure = weather_data.get("main", {}).get("pressure", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        wind_speed = weather_data.get("wind", {}).get("speed", "N/A")
        condition_text = weather_data.get("weather", {})[0].get("main", "N/A")

        # Create a dictionary with the extracted data
        extracted_data = {
            'temperature_c': temperature_c,
            'pressure': pressure,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'condition_text': condition_text
        }

        ##
        print(extracted_data)
        ##

        return extracted_data

    except KeyError as e:
        print(f"Error: Missing key in weather data: {e}")
        return None
    except TypeError as e:
        print(f"Error: Type error accessing weather data: {e}")
        return None