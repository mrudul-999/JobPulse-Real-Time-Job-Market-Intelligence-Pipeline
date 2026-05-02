import requests
import json

response = requests.get("https://www.arbeitnow.com/api/job-board-api")

data = response.json()

print(data["data"][0].keys())


