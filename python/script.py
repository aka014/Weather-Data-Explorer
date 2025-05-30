import data_utils as du
import db_utils as db
import dashboard_generator as dash_gen
import os

def main():
    db_client = db.init()

    data = du.fetch_weather_data(du.get_api_key())
    if data:
        extracted_data = du.extract_data(data)

        if extracted_data:
            db.store_weather_data(extracted_data, db_client)

        else:
            print("Failed to extract weather data.")
    else:
        print("Failed to fetch weather data.")

    db_weather_data = db.get_data_from_database(db_client)

    if db_weather_data:
        html_content = dash_gen.generate_html(db_weather_data)

        # Determine the base path and file path
        base_path = os.path.abspath(".")
        docs_path = os.path.join(base_path, "docs")
        file_path = os.path.join(docs_path, "index.html")

        # Ensure the directory exists
        os.makedirs(docs_path, exist_ok=True)
        
        with open(file_path, "w") as f:
            f.write(html_content)

    else:
        print("Failed to retrieve weather data from Supabase.")


if __name__ == "__main__":
    main()
