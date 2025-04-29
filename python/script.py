import data_utils as du
import db_utils as db
import dashboard_generator as dash_gen

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

    test = db.count_rainy_days(db_client)

    test2 = db.hour_avg_temp(db_client)

    test5 = db.count_warm_days(db_client)
    test6 = db.count_cold_days(db_client)

    if db_weather_data:
        html_content = dash_gen.generate_html(db_weather_data)

        with open("..\docs\index.html", "w") as f:
            f.write(html_content)
        print("Successfully generated HTML file.")
    else:
        print("Failed to retrieve weather data from Supabase.")


if __name__ == "__main__":
    main()
