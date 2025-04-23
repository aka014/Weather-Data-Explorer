from dotenv import load_dotenv
import os
from supabase import create_client, Client


def init():
    """
    Initializes the database connection and creates a client.

    Returns:
        Client: Database connection.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Supabase setup
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")

    # Initialize Supabase client
    if supabase_url and supabase_key:
        supabase_client: Client = create_client(supabase_url, supabase_key)  # Type hint
    else:
        print("Error: SUPABASE_URL or SUPABASE_KEY is not set.")
        supabase_client = None

    return supabase_client

def store_weather_data(weather_data, supabase_client):
    """
    Stores weather data in the Supabase database.

    Args:
        weather_data (dict): A dictionary containing the weather data.
        supabase_client (Client): Database connection.
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

def get_data_from_database(supabase_client):
    """
    Retrieves weather data from the database.

    Args:
        supabase_client (Client): Database connection.

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