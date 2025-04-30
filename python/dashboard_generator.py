def generate_html(weather_data):
    """
    Generates a simple HTML page to display the weather data.

    Args:
        weather_data (dict): A dictionary of dictionaries, where each dictionary
                                represents a certain part of the site.

    Returns:
        str: A string containing the generated HTML.
    """

    if not weather_data:
        return "<p>No weather data available.</p>"

    try:

        # Create static dashboard using HTML and CSS
        html_content = ("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Weather Dashboard</title>
                <style>
                    body {
                        font-family: sans-serif;
                        background-color: #f0f0f0;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        min-height: 100vh;
                    }
                    .container {
                        width: 90%;
                        max-width: 800px;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    }
                    h1 {
                        text-align: center;
                        color: #555;
                    }
                    #current-conditions {
                        display: flex;
                        justify-content: space-around;
                        align-items: center;
                        margin-bottom: 20px;
                        border-bottom: 1px solid #ddd;
                        padding-bottom: 20px;
                    }
                    #current-conditions div {
                        text-align: center;
                    }
                    #temperature {
                        font-size: 2em;
                        color: #e67e22;
                    }
                    #humidity {
                        font-size: 2em;
                        color: #000;
                    }
                    #wind {
                        font-size: 2em;
                        color: #000;
                    }
                    #pressure {
                        font-size: 2em;
                        color: #000;
                    }
                    #condition-icon {
                        width: 100px;
                        height: 100px;
                        margin: 0 auto;
                    }
                    #historical-data {
                        margin-top: 20px;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 10px;
                    }
                    th, td {
                        padding: 8px;
                        border-bottom: 1px solid #ddd;
                        text-align: center;
                    }
                    th {
                        background-color: #f0f0f0;
                    }
                    @media (max-width: 600px) {
                        #current-conditions {
                            flex-direction: column;
                        }
                        table {
                            display: block;
                            overflow-x: auto;
                        }
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Weather Dashboard</h1>
                    <div id="current-conditions">
                        <div>
                            <img id="condition-icon" src=\"""" + get_condition_image(
                                weather_data.get('last_data', {})[0].get('condition', "N/A")) + """\" alt=\"""" +
                        weather_data.get('last_data', {})[0].get('condition', "N/A") + """\">
                            <p>""" + weather_data.get('last_data', {})[0].get('condition', "N/A") + """</p>
                        </div>
                        <div>
                            <p id="temperature">""" + str(weather_data.get('last_data', {})[0].
                                                          get('temp', "N/A")) + """&degC</p>
                            <p>Temperature</p>
                        </div>
                        <div>
                            <p id="humidity">""" + str(weather_data.get('last_data', {})[0].
                                                       get('hum', "N/A")) + """%</p>
                            <p>Humidity</p>
                        </div>
                        <div>
                            <p id="wind">""" + str(weather_data.get('last_data', {})[0].
                                                   get('wind', "N/A")) + """ m/s</p>
                            <p>Wind</p>
                        </div>
                        <div>
                            <p id="pressure">""" + str(weather_data.get('last_data', {})[0].
                                                       get('press', "N/A")) + """ mbar</p>
                            <p>Pressure</p>
                        </div>
                    </div>
                    <div id="historical-data">
                        <h2>Weather History for the Previous 24 Hours</h2>
                        <table>
                            <tr>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Temperature</th>
                                <th>Humidity</th>
                                <th>Wind</th>
                                <th>Pressure</th>
                                <th>Condition</th>
                            </tr>
            """)

        # Add rows for each weather data entry
        for i in range(0, 12):
            html_content += f"""
                            <tr>
                                <td>{weather_data.get('last_data', {})[i].get('d', "N/A")}</td>
                                <td>{weather_data.get('last_data', {})[i].get('t', "N/A").split('.')[0]}</td>
                                <td>{"{:.2f}".format(round(weather_data.get('last_data', {})[i].get('temp', "N/A"), 2))}
                                &degC</td>
                                <td>{weather_data.get('last_data', {})[i].get('hum', "N/A")}%</td>
                                <td>{"{:.2f}".format(round(weather_data.get('last_data', {})[i].get('wind', "N/A"), 2))}
                                m/s</td>
                                <td>{weather_data.get('last_data', {})[i].get('press', "N/A")} mbar</td>
                                <td>{weather_data.get('last_data', {})[i].get('condition', "N/A")}</td>
                                </tr>
                            """



        html_content += """
                        </table>
                    </div>
                    <div id="historical-data">
                        <h2>Weather History for the Previous 7 Days</h2>
                        <table>
                            <tr>
                                <th>Date</th>
                                <th>Maximum Temperature</th>
                                <th>Minimum Temperature</th>
                            </tr>
                    
            """

        # Add rows for each weather data entry
        for data in weather_data.get('seven_days', {}):
            html_content += f"""
                            <tr>
                                <td>{data.get('ts', 'N/A')}</td>
                                <td>{"{:.2f}".format(round(data.get('min_temp', 'N/A'), 2))}&degC</td>
                                <td>{"{:.2f}".format(round(data.get('max_temp', 'N/A'), 2))}&degC</td>
                            </tr>
                        """

        html_content += """
                        </table>
                    </div>
                </div>
            </body>
            </html>
            """
        return html_content

    except Exception as e:
        print("Error generating html due to lack of data")
        return "Error generating html due to lack of data."

# Slike nisu dovrsene kako treba

def get_condition_image(condition_text):
    """
    Returns the URL of the weather condition icon based on the condition text.

    Args:
        condition_text (str): The weather condition text (e.g., "Clear", "Clouds", "Rain").

    Returns:
        str: The URL of the corresponding weather icon.
    """

    if "Clear" == condition_text:
        return "https://cdn.weatherapi.com/weather/64x64/day/113.png"  # Clear
    elif "Clouds" == condition_text:
        return "https://cdn.weatherapi.com/weather/64x64/day/116.png"  # Clouds
    elif "Rain" == condition_text:
        return "https://cdn.weatherapi.com/weather/64x64/day/302.png"  # Rain
    elif "Snow" == condition_text:
        return "https://cdn.weatherapi.com/weather/64x64/day/338.png"  # Snow
    elif "Thunderstorm" == condition_text or "storm" in condition_text:
        return "https://cdn.weatherapi.com/weather/64x64/day/200.png"  # Thunderstorm
    else:
        return "https://cdn.weatherapi.com/weather/64x64/day/116.png"  # Default to Clouds if no match