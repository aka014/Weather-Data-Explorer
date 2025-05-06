# Weather Data Explorer

## Project Description

The Weather Data Explorer is a web application that provides users with access to current and historical weather information. It's designed to be a user-friendly dashboard, presenting data in a clear and informative way. This project integrates data from a weather API, stores it in a database, and generates an HTML page to display the information.

## Key Features

* **Data Acquisition:** Fetches weather data from a third-party API (e.g., OpenWeatherMap API).
* **Database Storage:** Stores weather data in a database.
* **Data Retrieval:** Retrieves weather data from the database for display.
* **HTML Generation:** Generates an HTML page to visualize the weather data.
* **Automated Updates:**  Automatically updates the weather data every two hours using GitHub Actions.
* **Current Conditions:** Displays current weather conditions, including:
    * Condition icon and description
    * Temperature
    * Humidity
    * Wind speed
    * Pressure
* **Historical Data:**
    * Provides a table of historical weather data for the past 24 hours, mirroring the current conditions data.
    * Provides a table of historical weather data, including:
        * Date
        * Maximum Temperature
        * Minimum Temperature
* **Responsive Design:** The web application is designed to be responsive and viewable on different screen sizes.

## Automated Updates

The `script.py` file is run every two hours through a scheduled GitHub Actions workflow. This automation ensures that the weather data displayed on the dashboard is always up-to-date. The workflow is configured in `.github/workflows/run-script-and-push.yml`.

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
* `pressure`: Pressure in mbar.
* `condition_text`: A short description of the weather condition.

## Setup Instructions

1.  **Prerequisites:**

    * Python 3.9
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
        LAT=<your_latitude>
        LON=<your_longitude>
        ```

    * Replace the placeholder values with your actual database URL, key, OpenWeatherMap API key and location coordinates.


4.  **Set up the database:**

    * Ensure that your database is set up with the necessary schema.
    
5.  **Requirements**

    * This project uses a `requirements.txt` file to manage its Python dependencies. Follow the steps below to set up the project:

        1. Ensure you have Python **3.9** (or compatible versions like **3.9.13**) installed. You can download Python from [python.org](https://www.python.org/).

        2. Install the dependencies listed in `requirements.txt` using the following command:

    ```bash
    pip install -r python/requirements.txt

6.  **Run the application:**

    ```
    python python/script.py
    ```

7.  **View the dashboard:**

    * Open the `index.html` file in your web browser.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
