import os
from flask import Flask, render_template, request, flash
import requests

# 1. Initialize the Flask Application
app = Flask(__name__)

# A secure secret key is required by Flask to handle session-based "flash" error notifications.
app.secret_key = "admin210506"

# 2. Configure Your API Key
# Replace the string below with your actual active API Key from OpenWeatherMap.
API_KEY = "0f2d79b8659d32a3e9cc9a11366e1caa"


# 3. Define the Core Application Route
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    
    # Check if the user has submitted a form looking up a city
    if request.method == "POST":
        # Capture text input and strip away accidental leading/trailing blank spaces
        city = request.form.get("city").strip()
        
        if city:
            # Endpoint 1: The Geocoding API converts text city names into precise Lat/Lon coordinates
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
            
            try:
                geo_response = requests.get(geo_url).json()
                
                # Verify that the geocoding service successfully found coordinates for the city
                if geo_response and len(geo_response) > 0:
                    lat = geo_response[0]["lat"]
                    lon = geo_response[0]["lon"]
                    city_name = geo_response[0]["name"]
                    country = geo_response[0]["country"]
                    
                    # Endpoint 2: The Weather API uses the Lat/Lon data to pull atmospheric details
                    # "units=metric" ensures temperature values are in Celsius and wind speed is in m/s
                    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
                    weather_response = requests.get(weather_url).json()
                    
                    # Structure the raw JSON payload into a tidy dictionary for the HTML page
                    weather_data = {
                        "city": f"{city_name}, {country}",
                        "temp": round(weather_response["main"]["temp"]),
                        "humidity": weather_response["main"]["humidity"],
                        "description": weather_response["weather"][0]["description"].title(),
                        "icon": weather_response["weather"][0]["icon"],
                        "wind": weather_response["wind"]["speed"]
                    }
                else:
                    # Trigger an error message if the user enters an unrecognized city name
                    flash("City not found. Please double-check your spelling!", "error")
            
            except requests.exceptions.RequestException:
                # Catch physical machine network drops or API server timeouts gracefully
                flash("Network connectivity issue. Failed to reach the weather service.", "error")
                
    # Render the index.html template. If weather_data is populated, it displays; otherwise, it stays hidden.
    return render_template("index.html", weather=weather_data)


# 4. Local Development Server Execution Block
if __name__ == "__main__":
    # debug=True allows the server to automatically restart when code changes are saved
    app.run(debug=True)