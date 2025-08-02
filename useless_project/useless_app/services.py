from google import genai
from django.conf import settings
import os

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

def get_content():
    prompt = (
        "Generate a deeply philosophical, thought-provoking, and original quote "
        "about life, existence, or consciousness."
    )
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
    )
    return response.text
