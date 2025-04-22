import requests
import json
from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Supabase setup
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
if SUPABASE_URL and SUPABASE_KEY:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    print("Error: SUPABASE_URL or SUPABASE_KEY is not set.")
    supabase_client = None


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

def store_weather_data(weather_data):
    """
    Stores weather data in the Supabase database.

    Args:
        weather_data (dict): A dictionary containing the weather data.
    """

    if not supabase_client:
        print("Error: Supabase client is not initialized.")
        return

    table_name = "weather_data"

    try:
        # Insert the data into the Supabase table
        response = supabase_client.table(table_name).insert(weather_data).execute()

        ##
        print(f"Supabase response: {response}")
        ##

        if response.data:
            print("Data successfully stored in Supabase.")
        else:
            print("Error inserting data into Supabase.")
    except Exception as e:
        print(f"An error occured while storing data: {e}")


def main():
    data = fetch_weather_data(get_api_key())
    if data:
        extracted_data = extract_data(data)

        if extracted_data:
            store_weather_data(extracted_data)

        else:
            print("Failed to extract weather data.")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    main()
