from google import genai
from django.conf import settings

client = genai.Client(api_key="AIzaSyANEc6CtQ_ODYScaC7Oc7pMr4mTKEjXbk8")

def get_content():
    prompt = (
        "Generate a deeply philosophical, thought-provoking, and original quote "
        "about life, existence, or consciousness."
    )
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
    )
    return response.text
