from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyANEc6CtQ_ODYScaC7Oc7pMr4mTKEjXbk8")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate a random philosophical, deep thought provoking content.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)