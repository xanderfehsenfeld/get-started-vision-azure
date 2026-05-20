import base64
import os
from dotenv import load_dotenv

import requests
import json

# Environment variables you set locally or in your app service:

load_dotenv()

with open("./PXL_20251220_135712023.jpg", "rb") as image_file:
    IMAGE_BASE64 = base64.b64encode(image_file.read()).decode('utf-8')


API_KEY = os.getenv("API_KEY")

url = "https://api.moondream.ai/v1/query"

headers = {
    "Content-Type": "application/json",
    "X-Moondream-Auth": API_KEY,
}

payload = {
    "image_url": f"data:image/jpeg;base64,{IMAGE_BASE64}",
    "question": "What is in this image?"
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json()["answer"])

# print(result["answer"])
