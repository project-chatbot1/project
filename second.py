
import requests
import os

api_key = os.environ.get("OPENAI_API_KEY")  # Replace with your actual API key

url = "https://api.openai.com/v1/usage"

headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
