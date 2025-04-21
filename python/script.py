import requests
import json

def fetch_weather_data(api_key):
    """
    Fetches weather data from Wunderground API.

    Args:
        api_key (str): The API key for the weather service.
    Returns:
        dict: A dictionary containing the weather data, or None if an error occurred.
    """

    try:
        # Construct the API URL
        api_url = api_key # ovo ne valja!!!

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





def main():
    print("Hello!")

if __name__ == "__main__":
    main()
