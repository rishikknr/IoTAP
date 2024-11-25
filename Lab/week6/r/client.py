import requests

# Server URL
SERVER_URL = "http://192.168.29.123:5000/temperature"

# Fetch temperature data from the server
try:
    response = requests.get(SERVER_URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Temperature: {data['temperature']} {data['unit']}")
    else:
        print("Failed to retrieve data. Server responded with:", response.status_code)
except Exception as e:
    print("Error connecting to server:", e)