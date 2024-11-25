import requests
import json
payload = {"text": "I love myself"}
header = {"Content-Type": "application/json"}

response = requests.post(
    url="http://127.0.0.1:5000/api",
    data=json.dumps(payload),
    headers=header
)
print(response.text)
