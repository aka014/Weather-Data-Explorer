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
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY) # Type hint
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

def get_data_from_database():
    """
    Retrieves weather data from the database.

    Returns:
        list: A list of dictionaries containing the weather data.
    """

    if not supabase_client:
        print("Error: Supabase client is not initialized. Data not retrieved.")
        return None

    table_name = "weather_data"

    try:
        # Fetch all rows from the weather_data table
        response = supabase_client.table(table_name).select("*").execute()

        if response.data:
            print("Data successfully retrieved from Supabase.")
            return response.data
        else:
            print("Error fetching data from Supabase.")
    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return None

def generate_html(weather_data_list):
    """
    Generates a simple HTML page to display the weather data.

    Args:
        weather_data_list (list): A list of dictionaries, where each dictionary
                                represents a row of weather data from the database.

    Returns:
        str: A string containing the generated HTML.
    """

    if not weather_data_list:
        return "<p>No weather data available.</p>"

    # Basic HTML structure
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather data from Supabase</title>
        <style>
            body {
                font-family: sans-serif;
                background-color: #f0f0f0;
                padding: 20px;
                text-align: center;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #f0f0f0;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
            padding: 8px;
            border-bottom: 1px solid #ddd;
            text-align: left;
            }
            th {
            background-color: #f0f0f0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Weather data</h1>
            <table>
                <tr>
                    <th>lat</th>
                    <th>lon</th>
                    <th>temperature_c</th>
                    <th>condition_text</th>
                    <th>created_at</th>
                </tr>
    """

    # Add rows for each weather data entry
    for data in weather_data_list:
        html_content += f"""
                <tr>
                    <td>{data.get('lat', "Error")}</td>
                    <td>{data.get('lon', "Error")}</td>
                    <td>{data.get('temperature_c', "Error")}</td>
                    <td>{data.get('condition_text', "Error")}</td>
                    <td>{data.get('created_at', "Error")}</td>
                </tr>
        """

    html_content += """
            </table>
        </div>
    </body>
    </html>
    """

    return html_content

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

    db_weather_data = get_data_from_database()
    if db_weather_data:
        html_content = generate_html(db_weather_data)

        with open("index.html", "w") as f:
            f.write(html_content)
        print("Successfully generated HTML file.")
    else:
        print("Failed to retrieve weather data from Supabase.")


if __name__ == "__main__":
    main()
