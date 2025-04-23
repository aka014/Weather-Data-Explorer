import requests
import json
import os

def fetch_weather_data(api_key):
    """
    Fetches weather data from Wunderground (still not this one) API.

    Args:
        api_key (str): The API key for the weather service.
    Returns:
        dict: A dictionary containing the weather data, or None if an error occurred.
    """

    lat = 45.58
    lon = 9.5

    try:
        # Construct the API URL
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

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
    return api_key


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
        #location_name = weather_data['location']['name']
        lat = weather_data.get("coord", {}).get("lat", "N/A")
        lon = weather_data.get("coord", {}).get("lon", "N/A")
        temperature_c = weather_data.get("main", {}).get("temp", "N/A")
        condition_text = weather_data.get("weather", {})[0].get("description", "N/A")

        # Create a dictionary with the extracted data
        extracted_data = {
            #'location_name': location_name,
            'lat': lat,
            'lon': lon,
            'temperature_c': temperature_c,
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