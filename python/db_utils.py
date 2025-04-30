from dotenv import load_dotenv
import os
from supabase import create_client, Client
import datetime


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
        print("Supabase client not initialized.")
        return None

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
        dict: A dictionary of lists containing the weather data.
    """

    if not supabase_client:
        print("Supabase client not initialized.")
        return None

    dictionary = {}

    dictionary['seven_days'] = get_last_seven_days(supabase_client)
    dictionary['last_data'] = get_last_data(supabase_client)

    return dictionary

def get_last_data(supabase_client):
    """
    Retrieves last 12 rows from the database.

    Args:
        supabase_client (Client): Database connection.

    Returns: list: A list of dictionaries containing the last 12 rows.
    """

    table_name = "weather_data"

    try:
        # Fetch last 12 rows from the weather_data table
        response = supabase_client.rpc('get_last_data').execute()

        if response.data:
            print("Data successfully retrieved from Supabase.")
            return response.data
        else:
            print("Error fetching data from Supabase.")
            return None

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return None


def get_last_seven_days(supabase_client):
    """
        Retrieves some weather data for the previous seven days.

        Args:
            supabase_client (Client): Database connection.

        Returns: list: A list of dictionaries containing the data.
        """

    table_name = "weather_data"

    try:
        # Fetch last seven days' data from the weather_data table
        response = supabase_client.rpc('get_last_seven_days', {}).execute()

        if response.data:
            print("Data successfully retrieved from Supabase.")
            return response.data
        else:
            print("Error fetching data from Supabase.")
            return None

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return None


def count_rainy_days(supabase_client, prev_flag = False):
    """
    Returns the number of rainy days in a current or previous month.

    Args:
        supabase_client (Client): Database connection.
        prev_flag (bool): True if previous month's days should be counted.

    Returns:
        int: Number of rainy days in a current or previous month, depending on the flag.

    Videcemo sta ce tacno vracati ova f-ja.
    """

    now = datetime.datetime.now()

    current_month = now.month
    current_year = now.year

    # Ovde bi moglo da se pristedi na sistemskim pozivima da se negde pre poziva svih funkcija pozove now
    if prev_flag:
        current_month -= 1
        if current_month == 0:
            current_year -= 1

    table_name = "weather_data"

    try:
        # Call stored function using RPC
        response = supabase_client.rpc('get_rainy_days', {'current_month': current_month,
                                                          'current_year' : current_year}).execute()

        if response.data:
            print(response.data)
            return response.data
        else:
            # print("Error retrieving data from Supabase.")
            return 0

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return -1


def hour_avg_temp(supabase_client, prev_flag = False):
    """
    Computes average temperature in Celsius during current or previous month's hour.

    Args:
        supabase_client (Client): Database connection.
        prev_flag (bool): True if previous month's data should be used.

    Returns:
        float: Average temperature in Celsius during current or previous month's hour.

    Videcemo hoce li ostati ovako
    """

    now = datetime.datetime.now()

    current_hour = now.hour
    current_month = now.month
    current_year = now.year

    # Ovde bi moglo da se pristedi na sistemskim pozivima da se negde pre poziva svih funkcija pozove now
    if prev_flag:
        current_month -= 1
        if current_month == 0:
            current_year -= 1

    table_name = "weather_data"

    try:
        # Call stored function using RPC
        response = supabase_client.rpc('hour_avg_temp', {'current_hour' : current_hour,
                                                         'current_month': current_month,
                                                         'current_year' : current_year
                                                         }).execute()

        if response.data:
            print(response.data)
            return response.data
        else:
            print("Error retrieving data from Supabase.")
            return 0

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return -1


def count_cold_days(supabase_client, prev_flag = False):
    """
    Returns the number of cold days in a current or previous month.

    Args:
        supabase_client (Client): Database connection.
        prev_flag (bool): True if previous month's days should be counted.

    Returns:
        int: Number of cold days in a current or previous month, depending on the flag.

    Videcemo sta ce tacno vracati ova f-ja.
    """

    now = datetime.datetime.now()

    current_month = now.month
    current_year = now.year

    # Ovde bi moglo da se pristedi na sistemskim pozivima da se negde pre poziva svih funkcija pozove now
    if prev_flag:
        current_month -= 1
        if current_month == 0:
            current_year -= 1

    table_name = "weather_data"

    try:
        # Call stored function using RPC
        response = supabase_client.rpc('count_cold_days', {'current_month': current_month,
                                                         'current_year' : current_year
                                                         }).execute()

        if response.data:
            print(response.data)
            return response.data
        else:
            # print("Error retrieving data from Supabase.")
            return 0

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return -1


def count_warm_days(supabase_client, prev_flag = False):
    """
    Returns the number of warm days in a current or previous month.

    Args:
        supabase_client (Client): Database connection.
        prev_flag (bool): True if previous month's days should be counted.

    Returns:
        int: Number of warm days in a current or previous month, depending on the flag.

    Videcemo sta ce tacno vracati ova f-ja.
    """

    now = datetime.datetime.now()

    current_month = now.month
    current_year = now.year

    # Ovde bi moglo da se pristedi na sistemskim pozivima da se negde pre poziva svih funkcija pozove now
    if prev_flag:
        current_month -= 1
        if current_month == 0:
            current_year -= 1

    table_name = "weather_data"

    try:
        # Call stored function using RPC
        response = supabase_client.rpc('count_warm_days', {'current_month': current_month,
                                                         'current_year' : current_year
                                                         }).execute()

        if response.data:
            print(response.data)
            return response.data
        else:
            # print("Error retrieving data from Supabase.")
            return 0

    except Exception as e:
        print(f"An error occured while retrieving data: {e}")
        return -1

