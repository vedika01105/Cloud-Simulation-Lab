import requests
import datetime

url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"

try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    data = response.json()
    print("Data:", data)

    # Try both possible structures
    if "current_weather" in data:
        weather = data["current_weather"]
        temp = weather.get("temperature")
        wind = weather.get("windspeed")
    elif "current" in data:
        weather = data["current"]
        temp = weather.get("temperature_2m")
        wind = weather.get("wind_speed_10m")
    else:
        raise ValueError("Unexpected JSON structure")

    time_now = datetime.datetime.now()
    with open("weather_log.txt", "a") as f:
        f.write(f"{time_now} | Temp: {temp}°C | Wind: {wind} km/h\n")

    print(f"[{time_now}] Logged: Temp={temp}°C, Wind={wind} km/h")

except Exception as e:
    print("Error fetching weather:", response.status_code if 'response' in locals() else "", e)
