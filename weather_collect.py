import requests, datetime, csv, os

url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
filename = "weather_data.csv"

# create csv with header if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "windspeed"])

try:
    res = requests.get(url, timeout=10)
    data = res.json()
    w = data["current_weather"]
    t = w["temperature"]
    ws = w["windspeed"]
    now = datetime.datetime.now()

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([now, t, ws])

    print(f"{now} → logged Temp={t}°C Wind={ws} km/h")

except Exception as e:
    print("Error:", e)
