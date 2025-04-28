# Weather Data Explorer

## Project Description

The Weather Data Explorer is a web application that provides users with access to current and historical weather information. It's designed to be a user-friendly dashboard, presenting data in a clear and informative way. This project integrates data from a weather API, stores it in a database, and generates an HTML page to display the information.

## Key Features

* **Data Acquisition:** Fetches weather data from a third-party API (e.g., OpenWeatherMap API).
* **Database Storage:** Stores weather data in a database.
* **Data Retrieval:** Retrieves weather data from the database for display.
* **HTML Generation:** Generates an HTML page to visualize the weather data.
* **Current Conditions:** Displays current weather conditions, including:
    * Condition icon and description
    * Temperature
    * Humidity
    * Wind speed
    * Pressure
* **Historical Data:** Provides a table of historical weather data, including:
    * Date
    * Maximum Temperature
    * Minimum Temperature
* **Responsive Design:** The web application is designed to be responsive and viewable on different screen sizes.

## Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python
* **Database:** PostgreSQL
* **API:** OpenWeatherMap API
* **Libraries:**
    * requests, json (for fetching data from the API)
    * supabase (for interacting with the Supabase database)
    * dotenv, os (for managing environment variables)

## Database Implementation

The project uses a PostgreSQL database to store weather data. The database schema includes a table (e.g., `weather_data`) with columns such as:

* `created_at`: Timestamp of when the data was recorded.
* `temperature_c`: Temperature in Celsius.
* `humidity`: Humidity percentage.
* `wind_speed`: Wind speed in kilometers per hour.
* `pressure`: Pressure in hPa
* `condition_text`: A short description of the weather condition.

## Setup Instructions

1.  **Prerequisites:**

    * Python 3.x
    * A PostgreSQL database.
    * A OpenWeatherMap API account and API key.

2.  **Clone the repository:**

    ```
    git clone <your_repository_url>
    cd weather-data-explorer
    ```

3.  **Set up environment variables:**

    * Create a `.env` file in the project root.
    * Add the following variables to the `.env` file:

        ```
        SUPABASE_URL=<your_supabase_url>
        SUPABASE_KEY=<your_supabase_key>
        API_KEY=<your_weather_api_key>
        ```

    * Replace the placeholder values with your actual database URL, key, and OpenWeatherMap API key.


4.  **Set up the database:**

    * Ensure that your database is set up with the necessary schema.

5.  **Run the application:**

    ```
    python main.py
    ```

6.  **View the dashboard:**

    * Open the `index.html` file in your web browser.
