
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OMNIROUTE_API_KEY"),
    base_url=os.getenv("OMNIROUTE_BASE_URL"),
)

response = client.chat.completions.create(
    model=os.getenv("OMNIROUTE_MODEL"),
    messages=[
        {"role": "user", "content": "Explain Python decorators in simple terms."}
    ],
)

print("\n--- MODEL INFORMATION ---")
print("Requested model:", "ai-fallback")
print("Response model:", response.model)
print("Response ID:", response.id)

print("\n--- GENERATED RESPONSE ---")
print(response.choices[0].message.content)

print("\n--- TOKEN USAGE ---")
print(response.usage)
