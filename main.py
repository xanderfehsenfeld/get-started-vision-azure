import os
import base64
from openai import OpenAI
from dotenv import load_dotenv


# Environment variables you set locally or in your app service:


load_dotenv()


client = OpenAI(
    api_key=os.getenv("FOUNDRY_KEY"),
    base_url=os.getenv("ENDPOINT"),
)

with open("./PXL_20251220_135712023.jpg", "rb") as image_file:
    image_url = base64.b64encode(image_file.read()).decode('utf-8')

response = client.responses.create(
    model=os.getenv("MODEL_NAME"),  # your deployment name 
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What is in this image? Provide 3 bullet points."},
                {"type": "input_image", "image_url":  f"data:image/jpg;base64,${image_url}"  }
            ],
        }
    ],
)

print(response.output_text)