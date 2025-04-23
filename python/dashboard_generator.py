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